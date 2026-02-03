# Avant-Garde Designer Recommender

A **fashion recommendation system** built with Python and Streamlit that suggests **avant-garde fashion designers** using similarity-based logic and structured style representations.

This project demonstrates how exploratory data science work can be translated into a **clean, modular, and deployable application**, suitable for real world usage.

---

## What This Project Demonstrates

- Designing a **recommendation system** from scratch
- Translating notebooks into **production-ready Python modules**
- Applying **similarity / embedding concepts** to a non traditional domain
- Building a **user facing web application** on top of data science logic
- Structuring a Python project with clear separation of concerns

---

## Key Features

- **Designer recommendation engine** based on style similarity
- Focus on **avant-garde / experimental fashion aesthetics**
- Interactive **Streamlit web interface**
- Modular architecture separating:
  - UI layer
  - Controller / business logic
  - Core recommendation logic
- Jupyter notebooks used for experimentation and validation

---

## System Overview

1. Designer and fashion data is processed and structured  
2. Similarity logic is applied to generate ranked designer recommendations  
3. The Streamlit app exposes the recommender through a simple, interactive UI  

This workflow mirrors how recommendation systems are typically prototyped and then operationalized in industry settings.

---

## Tech Stack

- **Python**
- **Streamlit** (web application)
- **Pandas / NumPy** (data processing)
- **Similarity / embedding techniques**
- **Jupyter Notebook** (research & prototyping)

---

## Project Structure

Avant_Garde_Designer_Recommender/

│

├── .streamlit/          # Streamlit configuration

├── assets/              # Images / static assets

├── controller/          # Recommendation & controller logic

├── data/                # Datasets (may be excluded if large)

├── notebooks/           # Experiments & exploratory analysis

├── src/                 # Core reusable code

│

├── app.py               # Generalized app

├── app2.py              # Alternate / experimental app entry (still developing)

├── requirements.txt     # Python dependencies

└── README.md            # Project documentation


---

## Engineering Notes

- Notebook code is progressively migrated into reusable modules
- Business logic is decoupled from UI for maintainability
- The project is structured to allow:
- New designers or datasets
- Alternative similarity models

API or backend integration is in development
---

## Development Notes

- Recommendation logic is kept separate from the UI
- Notebooks are used for prototyping before moving logic into src/
- The architecture is designed to be extensible (e.g. new designers, new similarity models)
