"""
LlamaParse Document Ingestion Module

This module provides functionality to parse documents using LlamaParse API
with advanced configuration options for handling tables, spreadsheets, and markdown output.
"""
import os
import json
from pathlib import Path
from typing import List
from dotenv import load_dotenv
from llama_index.core import Document

from llama_parse import LlamaParse

load_dotenv()

# Initialize LlamaParse with advanced configuration
parser = LlamaParse(
    api_key=os.getenv("LLAMA_CLOUD_API_KEY"),

    # Output
    result_type="markdown",
    output_tables_as_HTML=True,

    # Quality / mode
    # premium_mode=True, # Conflicting with parse_mode
    parse_mode="parse_document_with_agent",          # or equivalent agentic preset
    high_res_ocr=True,
    adaptive_long_table=True,

    # Spreadsheets
    spreadsheet_force_formula_computation=True,   # consider disabling in ultra-large sheets
    spreadsheet_extract_sub_tables=True,

    # Layout & pagination
    preserve_layout_alignment_across_pages=True,
    merge_tables_across_pages_in_markdown=True,

    # Optional noise control
    # hide_headers=True,
    # hide_footers=True,

    # Optional for tiny text / diagrams
    preserve_very_small_text=True
)

def save_documents(docs: List[Document], path: str | Path) -> None:
    path = Path(path)
    payload = [doc.dict() for doc in docs]   # full Document, including metadata, images, etc.
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)

def ingest_document(file_path: str):
    """
    Ingest a document using LlamaParse.

    Args:
        file_path (str): Path to the document file to be ingested

    Returns:
        Parsed document content in markdown format with HTML tables

    Raises:
        FileNotFoundError: If the specified file does not exist
        Exception: If parsing fails
    """
    try:
        # Parse the document
        documents = parser.load_data(file_path)
        save_documents(documents, "output/parsed_documents.json")
        return documents
    except FileNotFoundError:
        raise FileNotFoundError(f"Document not found: {file_path}")
    except Exception as e:
        raise Exception(f"Failed to parse document: {str(e)}")


if __name__ == "__main__":
    # Example usage
    import sys

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print("No file provided, using default: input/TestSpreadsheet.xlsx")
        file_path = "input/TestSpreadsheet.xlsx"

    try:
        result = ingest_document(file_path)
        print(f"Successfully parsed document: {file_path}")
        # print(f"Result: {result}") # Commenting out result printing to avoid clutter
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
