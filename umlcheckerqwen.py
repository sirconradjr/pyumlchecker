import base64
import requests
import sys

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5vl:7b"

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded

def query_gemma3_vision(image_path, prompt=\
     "Evaluate the attached student-submitted **UML-style Entity-Relationship Diagram (ERD)** using the rubric below. The diagram is expected to conform to **UML standards** and should clearly represent the structure and relationships of a database system based on the problem domain.\n\n\
    The expected elements in a UML ERD include:\n\
    - **Entities (Classes)**: Represented as rectangular boxes with three compartments (class name, attributes, and operations if applicable)\n\
    - **Attributes**: Listed in the middle compartment, including primary keys (usually marked with a stereotype or underscore) and foreign keys\n\
    - **Relationships (Associations)**: Lines connecting entities, optionally with association names and roles\n\
    - **Multiplicity (Cardinality)**: Clearly shown at both ends of each relationship (e.g., 1..*, 0..1)\n\
    - **Generalization/Inheritance** (if present): Shown using a hollow triangle pointing to the superclass\n\
    - **Aggregation/Composition**: Represented using diamonds (hollow for aggregation, filled for composition)\n\
    - **Consistent naming conventions** and **logical structure** that mirrors the intended data model\n\n\
    ---\n\
    **Evaluation Rubric:**\n\
    1. **Structural Clarity** – Assesses legibility, layout, organization, and consistent application of notation (e.g., Chen, Crow's Foot, UML). \n\
       - 4: Highly legible, organized, with precise layout and consistent notation\n\
       - 3: Clear overall, minor clutter or spatial inefficiencies\n\
       - 2: Moderate clutter or ambiguous labels, inconsistent layout\n\
       - 1: Disorganized, illegible, inconsistent or missing notation\n\
    \n\
    2. **Schema Completeness** – Evaluates inclusion of all necessary entities, relationships, attributes, keys, and constraints. \n\
       - 4: Fully complete, includes all required schema elements and constraints\n\
       - 3: Mostly complete, minor omissions\n\
       - 2: Several important elements or constraints missing or ambiguous\n\
       - 1: Lacks most critical components, schema is incomplete\n\
    \n\
    3. **Semantic Accuracy** – Measures how well the diagram models the domain, including logical correctness of mappings, relationships, and keys.\n\
       - 4: Logically sound, correct mappings and constraints, follows normalization\n\
       - 3: Minor logical issues that don’t impede understanding\n\
       - 2: Noticeable logical or mapping errors affecting clarity or correctness\n\
       - 1: Major errors, inaccurate domain modeling, poor normalization\n\
    \n\
    4. **Notational Consistency** – Checks for consistent use of symbols, naming conventions, and formatting across the diagram.\n\
       - 4: Uniform notation and formatting throughout\n\
       - 3: Minor inconsistencies\n\
       - 2: Multiple inconsistencies causing some confusion\n\
       - 1: Inconsistent or missing notation and formatting\n\
    \n\
    ---\n\
    **Instructions:**\n\
    1. Assign a score (1–4) for each of the four rubric categories.\n\
    2. Sum the scores to get a total out of 16.\n\
    3. Report only the total score (e.g., 13/16).\n\
    4. Provide a detailed explanation of the strengths and weaknesses in each category.\n\
    5. Suggest specific, actionable improvements to enhance the diagram’s quality.\n"):

    
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