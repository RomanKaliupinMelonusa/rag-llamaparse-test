# rag-llamaparse-test

A Python project for document ingestion using LlamaParse API with advanced configuration for RAG (Retrieval-Augmented Generation) systems.

## Features

- Document parsing using LlamaParse with enterprise-grade configuration
- Support for premium parsing mode
- Adaptive long table handling
- Spreadsheet formula computation and sub-table extraction
- HTML table output in markdown format

## Prerequisites

- Python 3.8 or higher
- LlamaParse API key (Enterprise)

## Setup Instructions

### 1. Create Python Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/MacOS:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Edit `llamaparse_ingest.py` and replace `"llx-..."` with your actual LlamaParse Enterprise API key:

```python
parser = LlamaParse(
    api_key="your-actual-api-key-here",
    ...
)
```

Alternatively, you can use environment variables:

```bash
export LLAMA_PARSE_API_KEY="your-actual-api-key-here"
```

And modify the code to use:
```python
import os
parser = LlamaParse(
    api_key=os.getenv("LLAMA_PARSE_API_KEY"),
    ...
)
```

## Usage

### As a Module

```python
from llamaparse_ingest import ingest_document

# Parse a document
documents = ingest_document("/path/to/your/document.pdf")
print(documents)
```

### As a Command-Line Tool

```bash
python llamaparse_ingest.py /path/to/your/document.pdf
```

## Configuration

The LlamaParse parser is configured with the following options:

- **result_type**: `"markdown"` - Output format
- **premium_mode**: `True` - Enable premium parsing features
- **adaptive_long_table**: `True` - Handle long tables adaptively
- **spreadsheet_force_formula_computation**: `True` - Compute formulas in spreadsheets
- **spreadsheet_extract_sub_tables**: `True` - Extract sub-tables from spreadsheets
- **output_tables_as_HTML**: `True` - Output tables in HTML format within markdown

## Supported File Types

LlamaParse supports various document formats including:
- PDF files
- Microsoft Office documents (Word, Excel, PowerPoint)
- Images with text
- And more

## Project Structure

```
rag-llamaparse-test/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── llamaparse_ingest.py     # Main ingestion module
└── .gitignore               # Git ignore rules
```

## License

MIT