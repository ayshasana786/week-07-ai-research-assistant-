# Week 7 - AI Research Assistant

## Overview

This project is an AI Research Assistant built using LangGraph, LangChain, Groq, and a custom Wikipedia research tool.

The assistant accepts a research topic, retrieves relevant information from Wikipedia, processes the retrieved information, and generates a clear summary using an LLM.

## Features

- AI Research Assistant
- LangGraph workflow
- Custom research tool
- Wikipedia information retrieval
- Groq LLM integration
- Automatic research summarization
- Command-line interface

## Technologies Used

- Python
- LangChain
- LangGraph
- Groq
- Wikipedia API
- Requests
- Python-dotenv

## Workflow

User Question
↓
Research Node
↓
Wikipedia Research Tool
↓
Retrieved Information
↓
Summary Node
↓
Groq LLM
↓
Final Summary

## Project Structure

```text
week-07-ai-research-assistant/
│
├── app.py
├── graph.py
├── tools.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md