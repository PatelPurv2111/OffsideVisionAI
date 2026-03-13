# OffsideVisionAI
PitchLaw AI is an AI-powered assistant designed to answer questions about football rules and regulations using the official Laws of the Game published by FIFA and the International Football Association Board.

The system uses Retrieval-Augmented Generation (RAG) to search the rulebook and generate accurate explanations of football laws such as offside, fouls, referee duties, and match procedures.

⸻

📌 Project Overview

Football rules are detailed and sometimes difficult to interpret during live matches or discussions.
PitchLaw AI allows users to ask questions in natural language and receive answers based on the official rulebook.

Example questions:
	•	What is the offside rule?
	•	What are the duties of a referee?
	•	How many players can be on the field?
	•	What happens if the ball hits the referee?

⸻

🧠 Technologies Used
	•	Python
	•	LangChain
	•	FAISS Vector Database
	•	Sentence Transformers (Embeddings)
	•	Transformers (LLM)
	•	Gradio (User Interface)

⸻

🏗️ System Architecture

The system follows a Retrieval-Augmented Generation (RAG) architecture:

PDF Rulebook
↓
Document Loader
↓
Text Chunking
↓
Embeddings Generation
↓
Vector Database (FAISS)
↓
Retriever
↓
Language Model
↓
Answer Generation

This ensures responses are grounded in the official FIFA rulebook.
