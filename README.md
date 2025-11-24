# CAPSTONE-PROJECT
# Community Health Navigator — Kaggle Capstone

## Overview
Community Health Navigator (CHN) is an agent-powered assistant to help people in low-resource communities find clinics, triage symptoms, and create structured referrals / appointment requests.

## Features
- Retrieval-augmented answers grounded in local clinic data and health FAQ.
- Semantic search using embeddings + FAISS.
- Session memory for follow-ups.
- Function-calling to book appointments and generate referrals (JSON).
- Exportable referral / appointment JSON for clinic workflows.

## How to run (Kaggle)
1. Open `kaggle_notebook.ipynb`
2. Ensure `requirements.txt` is installed (Kaggle: use pip install in first cell)
3. Run cells in order: Data load → Build embeddings → Start demo conversation.
4. See `presentation.pdf` and `blog_post.md` for documentation and background.

## Files
- `data/clinics.csv`: sample clinic database
- `data/faq/`: health guides
- `src/`: code modules (embed, retriever, agent_controller, functions)

## Evaluation
- Includes automated JSON schema test for `book_appointment` and `generate_referral`
- Shows sample sessions with source citations and confidence levels.

## License & Ethics
- This is a demo prototype. Not a substitute for professional medical advice. Always encourage users to seek urgent in-person care for emergency symptoms.

## Contact
Your Name — email@example.com
