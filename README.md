# RAG using Watsonx and MilvusDB

This repository demonstrates a Retrieval-Augmented Generation (RAG) system using Watsonx and MilvusDB. The system leverages LangChain for document loading and querying.

## Setup

1. Clone the repository:

    ```
    git clone https://github.com/ngpinjie/rag-watsonx.git
    cd rag-watsonx
    ```

2. Create and activate a virtual environment:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

4. Create a `.env` file from `.env.example` and fill in your API keys:

    ```
    cp .env.example .env
    ```

## Usage

1. Load the PDF data:

    ```
    python load_pdf.py
    ```

2. Run the main script:

    ```
    python main.py
    ```

## Project Structure

- `load_pdf.py`: Script for loading PDF data and storing it in a vector database.
- `main.py`: Main script for setting up the LangChain interface and running queries.

## Requirements

- Python 3.7+
- IBM Watsonx
- MilvusDB
