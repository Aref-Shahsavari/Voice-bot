import os
import time
import uuid
import logging

from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from openai import OpenAI
from faster_whisper import WhisperModel
import edge_tts

# Configure application-wide logging.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("voicebot")

print("Starting Voice Bot Pro...")

app = FastAPI()

# Define directories for uploaded audio files and generated speech output.
UPLOAD_DIR = "static/uploads"
AUDIO_DIR = "static/audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

# Serve static assets and load Jinja2 templates.
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Configure the OpenAI-compatible client.
OS_OPENAI_KEY = "..."  # Replace with your actual API key or environment variable.
client = OpenAI(api_key=OS_OPENAI_KEY)

# Load the Whisper speech-to-text model.
# If CUDA is unavailable, fall back to CPU execution.
print("Loading Whisper Model...")
try:
    whisper_model = WhisperModel("small", device="cuda", compute_type="float16")
    logger.info("Whisper model loaded on CUDA.")
except Exception as e:
    logger.warning(f"CUDA failed, falling back to CPU: {e}")
    whisper_model = WhisperModel("small", device="cpu", compute_type="int8")
    logger.info("Whisper model loaded on CPU.")


# Render the main web interface.
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )


# Handle incoming voice input and return a spoken response.
@app.post("/process_audio")
async def process_audio(file: UploadFile = File(...)):
    start_time = time.time()

    # Step 1: Save the uploaded audio file to disk.
    try:
        file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.wav")
        with open(file_path, "wb") as f:
            f.write(await file.read())
    except Exception as e:
        logger.error(f"File save error: {e}")
        return JSONResponse({"error": "خطا در ذخیره فایل صوتی"}, status_code=500)

    # Step 2: Convert speech to text using Whisper.
    try:
        segments, info = whisper_model.transcribe(file_path, beam_size=5)
        user_text = " ".join(segment.text for segment in segments).strip()
    except Exception as e:
        logger.error(f"Whisper error: {e}")
        return JSONResponse({"error": "خطا در پردازش صوت"}, status_code=500)

    if not user_text:
        return JSONResponse({"error": "صدایی تشخیص داده نشد"}, status_code=400)

    logger.info(f"User said: {user_text}")

    # Step 3: Generate an LLM response in Persian.
    try:
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {
                    "role": "system",
                    "content": "تو دستیار هوشمند شرکت هستی. پاسخ‌ها را بسیار کوتاه (حداکثر دو جمله) و محترمانه به فارسی بده.",
                },
                {"role": "user", "content": user_text},
            ],
        )
        bot_reply = response.choices[0].message.content
    except Exception as e:
        logger.error(f"LLM error: {e}")
        return JSONResponse(
            {"error": "خطا در ارتباط با مدل هوش مصنوعی (کلید API یا سهمیه را بررسی کنید)"},
            status_code=502,
        )

    logger.info(f"Bot reply: {bot_reply}")

    # Step 4: Convert the generated text into speech.
    try:
        output_filename = f"{uuid.uuid4()}.mp3"
        output_path = os.path.join(AUDIO_DIR, output_filename)

        communicate = edge_tts.Communicate(bot_reply, "fa-IR-DilaraNeural")
        await communicate.save(output_path)
    except Exception as e:
        logger.error(f"TTS error: {e}")
        return JSONResponse({"error": "خطا در تولید صدا"}, status_code=500)

    latency = round(time.time() - start_time, 2)

    # Calculate transcription confidence with a safe fallback for different Whisper versions.
    confidence_val = getattr(info, "language_probability", None)
    confidence_text = f"{round(confidence_val * 100, 1)}%" if confidence_val is not None else "N/A"

    return {
        "user_text": user_text,
        "bot_reply": bot_reply,
        "audio_url": f"/static/audio/{output_filename}",
        "metrics": {
            "latency": f"{latency}s",
            "model": "GPT-5",
            "confidence": confidence_text,
        },
    }


if __name__ == "__main__":
    import uvicorn

    # Start the FastAPI development server.
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
