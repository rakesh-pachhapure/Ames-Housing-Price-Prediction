# Ames Housing Price Prediction

A machine learning project that predicts house sale prices using the Ames Housing dataset. The project includes data exploration notebooks, a trained model, and a Streamlit application for interactive predictions.

## Project Overview

The goal is to estimate a property's sale price from housing features supplied to the trained model.

**Project status:** Update this README to match the exact features and metrics implemented in `app.py`.

## Project Files

- `app.py` — Streamlit application and prediction dashboard.
- `house_price_model.pkl` — Saved model, if this is the model loaded by `app.py`.
- `house_prediction.pkl` — Another saved model file; keep only if it is used by your application or needed for comparison.
- `ames_housing_beginner_2000_rows.csv` — Housing dataset used for exploration or training.
- `eda.ipynb` — Exploratory data analysis notebook.
- `main_1.ipynb` — Main modeling / experimentation notebook.
- `requirements.txt` — Python dependencies.
- `.gitignore` — Files and folders Git should ignore.

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Joblib

## Setup

### 1. Clone or download the repository

If using Git:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd houseproject
```

Alternatively, download the repository and open the `houseproject` folder in VS Code.

### 2. Create and activate a virtual environment (recommended)

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`.

## How to Use

1. Start the Streamlit application.
2. Enter the housing features requested by the app.
3. Submit the form to generate a predicted sale price.
4. Review any charts or prediction history provided by the current version of the dashboard.

## Model and Data Notes

- The app's input column names and data types must match those expected by the saved model.
- If preprocessing (such as encoding or scaling) was used during training, ensure the saved artifact includes the complete fitted pipeline, or apply the same preprocessing in the app.
- Model performance metrics should be calculated on held-out evaluation data. Add your actual MAE, RMSE, and R² values here if you want to publish them.
- Do not claim features, charts, or metrics that are not implemented in the current app.

## Deployment

For Streamlit Community Cloud:

1. Push the required project files to a GitHub repository.
2. Open Streamlit Community Cloud and create a new app.
3. Select the repository, branch, and `app.py` as the entry point.
4. Deploy the app.

Ensure `requirements.txt` includes compatible versions of the packages used to train and load the saved model. Avoid uploading secrets or unnecessary temporary files.

## Future Improvements

- Improve dashboard styling and usability.
- Add additional data visualizations.
- Display model evaluation metrics.
- Add prediction history, if useful.
- Document the final feature list and verified model performance.

## Author

Rakesh Pachhapure 

# Ames Housing Price Prediction

## Project Overview
A machine learning project that predicts residential house sale prices using housing-related features from the Ames Housing dataset. The project uses Python and Scikit-learn to build a predictive model and Streamlit to create an interactive web dashboard.

## Objectives
- Explore and understand housing data through Exploratory Data Analysis (EDA).
- Prepare features for machine learning.
- Train a regression model to predict house sale prices.
- Evaluate the model using appropriate regression metrics.
- Build an interactive dashboard for user inputs and predictions.
- Prepare the application for deployment.

## Technologies Used
- **Python** — Programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical computing
- **Matplotlib** — Data visualization
- **Scikit-learn** — Machine learning and model evaluation
- **Joblib** — Saving and loading the trained model
- **Streamlit** — Interactive web dashboard
- **Jupyter Notebook** — Data exploration and experimentation
- **Git and GitHub** — Version control and project hosting

## Dataset
The project includes `ames_housing_beginner_2000_rows.csv`, a housing dataset used for analysis and model development. The model predicts the target variable **SalePrice**, using selected housing features.

## Project Structure
- `app.py` — Streamlit application.
- `ames_housing_beginner_2000_rows.csv` — Dataset.
- `eda.ipynb` — Exploratory Data Analysis.
- `main_1.ipynb` — Model development and experimentation.
- `house_price_model.pkl` — Saved trained model.
- `house_prediction.pkl` — Additional saved model; its purpose depends on how it is used in the project.
- `requirements.txt` — Required Python packages.
- `README.md` — Project documentation.

## Key Features
- Machine learning-based house price prediction.
- Interactive user input through a Streamlit interface.
- Data exploration and visualization.
- Saved model for reuse without retraining every time.
- Deployment-ready project structure.

## How to Run
1. Install the required packages using `pip install -r requirements.txt`.
2. Open the project folder in VS Code.
3. Run `python -m streamlit run app.py`.
4. Open the local URL displayed in the terminal.
5. Enter the required housing features and generate a prediction.

## Model Evaluation
The model should be evaluated using regression metrics such as:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE) or Root Mean Squared Error (RMSE)
- R² Score

Add the actual evaluation results after verifying them on the test dataset.

## Future Enhancements
- Advanced Streamlit dashboard
- Improve the dashboard design and user experience.
- Compare different models



