import os
import google.generativeai as genai
from PIL import Image
from io import BytesIO

# Set your Google API Key here
os.environ["GOOGLE_API_KEY"] = "AIzaSyCqktNeWmGsAwEWDkhBWePFAXijEqytx8Q"  # Replace with your key

# Configure Gemini
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def generate_prompt(summary):
    return f"Create a realistic and culturally relevant image representing: {summary}"

def generate_image(summary):
    #model = genai.GenerativeModel("gemini-1.5-flash")
    model="gemini-2.0-flash-preview-image-generation"

    prompt = generate_prompt(summary)

    try:
        response = model.generate_content(prompt, generation_config={"response_mime_type": "image/png"})

        img_data = response.parts[0].data
        image = Image.open(BytesIO(img_data))

        filename = "_".join(summary.lower().split()[:5]) + ".png"
        image.save(filename)
        print(f"Image saved as {filename}")

    except Exception as e:
        print(f"Error generating image: {e}")

if __name__ == "__main__":
    summary = input("Enter summary for image generation: ")
    generate_image(summary)
