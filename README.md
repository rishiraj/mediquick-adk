# MediQuick Healthcare AI Agent

## Overview

**MediQuick** is a healthcare AI agent developed using Google's Agent Development Kit (ADK) and Gemini API. The agent assists users by analyzing symptoms, suggesting potential diagnoses, and providing structured medical advice reports in a clear and professional format.

## Features

- **Symptom Analysis:** Clearly summarizes patient-reported symptoms.
- **Diagnosis Suggestions:** Offers potential diagnoses with rationale and prioritization.
- **Structured Reports:** Delivers comprehensive, easy-to-understand Markdown-formatted reports with actionable medical recommendations.

## Prerequisites

- Google Agent Development Kit (ADK)
- Gemini API access

## Installation

Clone the repository:
```bash
git clone https://github.com/rishiraj/mediquick-adk.git
cd mediquick-adk
```

## Running the Agent

### Option 1: Using ADK CLI

Run directly with ADK:

```bash
adk run mediquick-adk/
```

### Option 2: Using ADK Web UI

Start the ADK web interface:

```bash
adk web
```

Then select the `MediQuick Healthcare Advisor Agent` from the UI.

## Project Structure

```
mediquick-adk/
├── agent.py
├── __init__.py
├── instructions/
│   ├── symptom_analyzer_instruction.txt
│   ├── diagnosis_suggestor_instruction.txt
│   ├── treatment_formatter_instruction.txt
│   └── healthcare_agent_instruction.txt
├── util.py
├── requirements.txt
└── README.md
```

## Technologies Used

- Google ADK
- Gemini API
- Python

## Contribution

Contributions and suggestions are welcome! Please open an issue or pull request on GitHub.
