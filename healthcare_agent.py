from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from .util import load_instruction_from_file

# --- Sub Agent 1: Symptom Analyzer ---
symptom_analyzer_agent = LlmAgent(
    name="SymptomAnalyzer",
    model="gemini-2.0-flash-001",
    instruction=load_instruction_from_file("symptom_analyzer_instruction.txt"),
    tools=[google_search],
    output_key="analyzed_symptoms",
)

# --- Sub Agent 2: Diagnosis Suggestor ---
diagnosis_suggestor_agent = LlmAgent(
    name="DiagnosisSuggestor",
    model="gemini-2.0-flash-001",
    instruction=load_instruction_from_file("diagnosis_suggestor_instruction.txt"),
    description="Suggest possible medical diagnoses based on analyzed symptoms.",
    output_key="diagnosis_suggestions",
)

# --- Sub Agent 3: Treatment Formatter ---
treatment_formatter_agent = LlmAgent(
    name="TreatmentFormatter",
    model="gemini-2.0-flash-001",
    instruction=load_instruction_from_file("treatment_formatter_instruction.txt"),
    description="Formats the final medical advice report.",
    output_key="final_medical_report",
)

# --- Main Healthcare Agent ---
healthcare_agent = LlmAgent(
    name="HealthcareAdvisorAgent",
    model="gemini-2.0-flash-001",
    instruction=load_instruction_from_file("healthcare_agent_instruction.txt"),
    description="Coordinates symptom analysis, diagnosis, and treatment formatting for healthcare consultation.",
    sub_agents=[symptom_analyzer_agent, diagnosis_suggestor_agent, treatment_formatter_agent],
)

# --- Root Agent ---
root_agent = healthcare_agent
