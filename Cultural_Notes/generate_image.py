# GOOGLE_API_KEY = "AIzaSyCqktNeWmGsAwEWDkhBWePFAXijEqytx8Q"

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

# === Initialize Gemini Client ===
client = genai.Client()

# === Your prompt ===
contents = (
    'Charminar refers to a historical monument and a popular tourist attraction in the city of Hyderabad, India. It is a massive arch-like structure with four minarets, located in the heart of the city, right at the center of the Chowmahalla Palace and the Golconda Fort.'
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
