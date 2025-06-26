from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

# === Initialize Gemini Client ===
client = genai.Client()

# === Your prompt ===
contents = (
    'The Taj Mahal, an ivory-white marble mausoleum on the bank of the Yamuna River in the city of Agra, is one of the most iconic and beautiful monuments in the world. It was built by Mughal Emperor Shah Jahan in the 17th century as a tomb for his beloved wife, Mumtaz Mahal, who died during childbirth. The monument stands as a magnificent symbol of love and devotion.'
)

# === Generate content ===
response = client.models.generate_content(
    model="gemini-2.0-flash-preview-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE']
    )
)

# === Get current directory ===
current_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_dir, 'gemini-native-image.png')

# === Save and show image ===
for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save(output_path)
        image.show()
        print(f"Image saved at: {output_path}")
