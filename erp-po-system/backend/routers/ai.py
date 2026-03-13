from fastapi import APIRouter
import google.generativeai as genai

router = APIRouter()

genai.configure(api_key="AIzaSyD6fC5p08Uk-aSG-BctbsTY8TJEJ5Mqczg")

model = genai.GenerativeModel("gemini-pro")


@router.get("/ai/generate-description")
def generate_description(product_name: str):

    prompt = f"""
    Write a professional 2 sentence marketing description
    for the product: {product_name}
    """

    response = model.generate_content(prompt)

    return {
        "product": product_name,
        "description": response.text
    }
