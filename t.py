# any language -> hindi 
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
audio_file = open("French.mp3", "rb")

translation = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file,
)

# convert it in english
english_text = translation.text
with open("translate.txt", "w") as file:
    file.write(english_text)
print(english_text)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a translator."},
        {"role": "user", "content": f"Translate this English text to Hindi:\n{english_text}"}
    ]
)

hindi_text = completion.choices[0].message.content
with open("translate2.txt", "w", encoding="utf-8") as file:
    file.write(hindi_text)
print(hindi_text)


from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="YOUR_API_KEY",
)
client.text_to_speech.convert(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    output_format="mp3_44100_128",
    text="The first move is what sets everything in motion.",
    model_id="eleven_multilingual_v2",
)
