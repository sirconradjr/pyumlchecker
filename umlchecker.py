import base64
import requests
import json
import sys

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded

def query_gemma3_vision(image_path, prompt=\
    "Evaluate the attached student-submitted Entity-Relationship Diagram (ERD) or Activity Diagram (flowchart) based on the following expectations: \
    1. Represent the system or process accurately (e.g., for an ERD, include correct entities, attributes, and relationships; for an Activity Diagram, show the correct sequence of steps and decisions). \
    2. Use proper notation and symbols (e.g., for an ERD, use rectangles for entities, lines or diamonds for relationships, and clear cardinality; for an Activity Diagram, use UML standards like circles for start/end, diamonds for decisions, and arrows for flow). \
    3. Ensure the diagram is clear and complete (e.g., for an ERD, all necessary components like primary and foreign keys are included; for an Activity Diagram, all steps, decisions, and start/end nodes are present and easy to follow). \
    Use the rubric below to assign a grade: \
    90-100% (A): Exceptional work; fully meets all expectations with accurate representation, correct notation, and a clear, complete diagram, with no errors. \
    80-89% (B): Solid work; meets most expectations with minor errors in representation, notation, or clarity, but the diagram is still functional and mostly complete. \
    70-79% (C): Satisfactory work; meets some expectations but has noticeable errors in representation, notation, or missing components, affecting functionality or clarity. \
    60-69% (D): Below average work; has significant errors in representation, incorrect or missing notation, and lacks clarity or completeness, making the diagram hard to understand. \
    Below 60% (F): Unsatisfactory work; fails to meet expectations with major errors, incorrect notation, and incomplete or unclear components, rendering the diagram unusable. \
    Provide a detailed explanation of the diagram’s strengths and weaknesses based on the expectations, highlighting specific issues (e.g., missing entities, incorrect symbols, or unclear labels). Then, suggest specific, actionable improvements to enhance the student’s work, ensuring the diagram meets the expected standards for database design or process modeling. Finally, assign a grade based on the rubric."):
    
    image_base64 = encode_image_to_base64(image_path)

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "images": [image_base64],
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "No response text returned.")

    except requests.RequestException as e:
        return f"Request failed: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gemma3_vision_insight.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    insights = query_gemma3_vision(image_path)
    print("=== Insights Extracted ===")
    print(insights)


 