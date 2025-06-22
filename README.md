# Sophos - AI Research Assistant

Sophos is an AI-powered research assistant designed to help users search, summarize, and explore academic topics using the arXiv API and the Gemma3:1b model via Ollama.

## Features

- Extracts core keywords from research questions using AI
- Fetches and summarizes relevant papers from arXiv
- Provides clear, concise, and insightful answers
- Interactive chat interface (Streamlit)

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PrathamGhaywat/Sophos.git
   cd Sophos
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Pull the Gemma3:1b model for Ollama:**
   ```bash
   ollama pull gemma3:1b
   ```

4. **Start the Ollama server:**
   ```bash
   ollama serve
   ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run src/main.py
   ```
6. **Open your browser:**
   Navigate to `http://localhost:8501` to access the app.
## Side notes
The response time may vary based on the complexity of the question and the number of relevant papers found. The AI model will extract keywords and provide answers based on the fetched articles. So it is kinda slow

## Project Structure

```
README.md
requirements.txt
src/
    arxiv_bot.py      # Fetches articles from arXiv
    main.py           # Streamlit app entry point
    model.py          # AI keyword extraction and answering
```

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/)
- [Streamlit](https://streamlit.io/)

## License

MIT License
