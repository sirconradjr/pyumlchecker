# UML Diagram (ERD/Activity Diagram) Evaluation Script

This Python script, `umlchecker.py`, uses the language-vision model, Gemma, to analyze a given UML diagram and assigns a letter grade and provides feedback.

## Description

`umlchecker.py` takes an image file as input, likely containing a scanned or photographed UML diagram (ERD/Actvity Diagram). It then attempts to identify and extract relevant information such as:

*   **Main Components:** Identifying the primary elements of the diagram, such as entities and relationships for ERDs, or steps and decision points for Activity Diagrams.
*   **Structural Accuracy:** Recognizing whether the diagram correctly represents the system or process (e.g., accurate entity relationships in ERDs or logical flow in Activity Diagrams).
*   **Notation Compliance:** Assessing the use of proper symbols and standards (e.g., rectangles and cardinality for ERDs, UML circles and arrows for Activity Diagrams).
*   **Feedback Generation:** Providing a detailed evaluation of the diagram’s strengths and weaknesses, including specific issues (e.g., missing primary keys or unclear transitions), and suggesting actionable improvements for the student’s work.
  
**Note:** The accuracy of the analysis depends heavily on the quality of the input image and the text within it.  Clear, well-formatted text images will yield the best results.

## Usage

To run the script, use the following command in your terminal:

```bash
python umlchecker.py <filename.jpg>
```
## Sample output
```
=== Insights Extracted ===
Okay, let's evaluate the student-submitted ERD.

**Overall Assessment:** C (72%)

**Detailed Explanation:**

**Strengths:**

*   **Basic Representation:** The diagram attempts to represent a system related to a library or bookstore (based on the entities present). It shows connections between entities like "Book", "Customer", and "Loan".
*   **Use of Rectangles:** The student has used rectangles for entities which is correct notation.
*   **Lines for Relationships:** The use of lines to represent relationships is a basic starting point, although the cardinality is not clearly defined.

**Weaknesses & Issues (Based on the Rubric Expectations):**

1.  **Inaccurate Representation:** The diagram lacks key components necessary for a complete and accurate representation of a library system. Specifically:
    *   **Missing Entities:** Crucially, it’s missing entities like “Author,” “Category,” “Staff,” and “Reservation”.  A library system is far more complex than just “Book”, “Customer”, and “Loan”.
    *   **Incomplete Relationships:** The relationships (lines) connecting entities don't represent the correct cardinality or multiplicity. For instance, it doesn't specify how many books a customer can loan, or how many authors can be associated with a single book. The lack of a ‘Borrowing’ entity and its associated attributes (e.g., due date, loan number) is a significant omission.
    *   **Lack of Primary/Foreign Keys:** There are no indication of primary keys for the entities, or how they link to each other through foreign keys – this is fundamental for a relational database.

2.  **Incorrect Notation:**
    *   **Cardinality Ambiguity:** As mentioned above, the lines connecting the entities are ambiguous.  They need to clearly show 1:1, 1:many, or many-to-many relationships.
    *   **Missing Symbols:**  The diagram doesn't use symbols to indicate primary keys or foreign keys, which are standard practice in ERDs.

3.  **Lack of Clarity & Completeness:**
    *   **Missing Attributes:** The entities lack attributes. For example, “Book” should have attributes like Title, ISBN, Publication Year, and potentially Genre. “Customer” needs attributes like CustomerID, Name, Address, etc.
    *   **Unclear Labels:** While the entity names are generally clear, a more descriptive label for the lines connecting entities would improve understanding.

**Specific Actionable Improvements:**

1.  **Add Missing Entities:** Incorporate the missing entities: “Author,” “Category,” “Staff”, and “Reservation”.
2.  **Define Cardinality:**  Clearly indicate the cardinality of each relationship using standard notations (e.g., crows feet).  For instance, a “Book” can be associated with one or many “Authors”.  A “Customer” can place one or many “Loans”.
3.  **Include Attributes:** Add relevant attributes to each entity (e.g., Title, ISBN, Publication Year for “Book”; CustomerID, Name, Address for “Customer”).
4.  **Define Primary Keys:** Explicitly designate primary keys for each entity (e.g., BookID for “Book,” CustomerID for “Customer”).
5.  **Add Foreign Keys:**  Establish foreign key relationships to link entities, demonstrating how data is related.
6. **Use Standard Notation:** Use proper conventions for primary and foreign key representation.

**Justification for Grade (C):**

The student has taken a basic first step towards representing a database. However, significant errors in representation, notation, and completeness prevent a higher grade. The diagram lacks the necessary components for a functional database design, and the ambiguous relationships make it difficult to understand. The inclusion of the suggested improvements would significantly enhance the diagram’s quality and accuracy.
````

## For improvement
Fee free to improve the prompt or customize a UI.
