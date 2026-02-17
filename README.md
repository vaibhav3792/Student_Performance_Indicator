# Student Performance Indicator

An end-to-end machine learning web application that predicts a student's math score based on demographic and academic preparation factors.

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange)

---

## Overview

This project trains and serves a regression model that predicts student math scores given inputs like gender, parental education level, lunch type, test preparation course status, and existing reading/writing scores.

The model was selected after benchmarking 8 different algorithms — **Linear Regression** achieved the best performance on the test set with an **R² of 0.88**.

---

## Demo

> Live at: ``

---

## Features

- Predicts math scores from 6 student features
- Automated model selection — trains and evaluates 8 algorithms, saves the best one
- Full preprocessing pipeline with `StandardScaler` and `OneHotEncoder`
- Clean Flask web interface with a form-based UI
- Deployable to Render, Railway, or PythonAnywhere

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.8+ |
| Web Framework | Flask |
| ML Library | Scikit-learn, XGBoost, CatBoost |
| Data | Pandas, NumPy |
| Frontend | HTML, CSS (Tailwind) |
| Deployment | Render |

---

## Project Structure

```
├── app.py                        # Flask application entry point
├── requirements.txt
├── Procfile                      # For Render deployment
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py     # Loads and splits the dataset
│   │   ├── data_transformation.py# Preprocessing pipeline
│   │   └── model_trainer.py      # Trains and evaluates all models
│   ├── pipeline/
│   │   └── predict_pipeline.py   # Inference pipeline for new inputs
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── artifacts/                    # Generated after training
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   └── test.csv
│
├── notebook/
│   ├── data/stud.csv             # Raw dataset
│   ├── 1___EDA_STUDENT_PERFORMANCE_.ipynb
│   └── 2__MODEL_TRAINING.ipynb
│
└── templates/
    ├── index.html                # Landing page
    └── home.html                 # Prediction form
```

---

## Dataset

- **Source:** [Kaggle — Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Size:** 1,000 rows × 8 columns
- **Target:** `math_score`

| Feature | Type | Description |
|---|---|---|
| `gender` | Categorical | Male / Female |
| `race_ethnicity` | Categorical | Group A – E |
| `parental_level_of_education` | Categorical | High school to Master's degree |
| `lunch` | Categorical | Standard / Free or reduced |
| `test_preparation_course` | Categorical | Completed / None |
| `reading_score` | Numerical | 0 – 100 |
| `writing_score` | Numerical | 0 – 100 |

---

## Model Results

8 models were evaluated on an 80/20 train-test split:

| Model | R² Score |
|---|---|
| **Linear Regression** ✅ | **0.8804** |
| Random Forest | 0.8525 |
| CatBoost Regressor | 0.8516 |
| AdaBoost Regressor | 0.8452 |
| XGBoost | 0.8278 |
| Lasso | 0.8253 |
| K-Neighbors Regressor | 0.7838 |
| Decision Tree | 0.7468 |

Linear Regression was selected as the best model with **RMSE = 5.39** on the test set.

---

## Getting Started

### Prerequisites

```bash
python 3.8+
pip
```

### Installation

```bash
# Clone the repo
git clone https://github.com/vaibhav3792/Student_Performance_Indicator.git
cd Student_Performance_Indicator

# Install dependencies
pip install -r requirements.txt
```

### Train the Model

```bash
python src/components/data_ingestion.py
```

This will run the full pipeline — ingest data, transform features, train all models, and save `model.pkl` and `preprocessor.pkl` to the `artifacts/` folder.

### Run the App

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## Deployment (Render)

1. Push your code including the `artifacts/` folder to GitHub
2. Go to [render.com](https://render.com) → New Web Service → connect your repo
3. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
4. Click **Deploy**

Make sure your `app.py` uses the `PORT` environment variable:

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
```

---

## Key Findings from EDA

- Students who completed the test preparation course scored higher across all three subjects
- Standard lunch correlates with higher scores across every subject
- Students whose parents hold a master's or bachelor's degree tend to perform better
- Reading and writing scores are strong predictors of math — all three scores move together linearly

---

