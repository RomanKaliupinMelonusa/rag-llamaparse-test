"""
LlamaParse Document Ingestion Module

This module provides functionality to parse documents using LlamaParse API
with advanced configuration options for handling tables, spreadsheets, and markdown output.
"""

from llama_parse import LlamaParse


# Initialize LlamaParse with advanced configuration
parser = LlamaParse(
    api_key="llx-...",  # Enterprise Key - replace with your actual API key
    result_type="markdown", 
    premium_mode=True,                 
    adaptive_long_table=True,          
    spreadsheet_force_formula_computation=True, 
    spreadsheet_extract_sub_tables=True, 
    output_tables_as_HTML=True         
)


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
        try:
            result = ingest_document(file_path)
            print(f"Successfully parsed document: {file_path}")
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {str(e)}")
            sys.exit(1)
    else:
        print("Usage: python llamaparse_ingest.py <file_path>")
        print("\nNote: Make sure to set your API key in the parser configuration")
