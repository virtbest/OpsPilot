# OpsPilot

OpsPilot is a support incident operations platform being built with Python and FastAPI.

The long-term goal is to help support teams receive, validate, classify, route, and resolve incidents using reliable AI-assisted workflows.

## Current Features

- Health-check endpoint
- Incident creation endpoint
- Automatic request validation
- Structured JSON responses
- Automated API tests

## Technology Stack

- Python
- FastAPI
- Pydantic
- pytest
- Git

## Project Structure

```text
OpsPilot/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_incidents.py
├── .gitignore
├── README.md
└── requirements.txt