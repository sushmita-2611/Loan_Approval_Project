# Loan Approval Prediction System

## About the Project

I developed this project during the AI/ML Summer Internship 2026 to understand how Machine Learning can be used to solve real-world problems such as loan approval prediction. The project covers data preprocessing, visualization, model training, evaluation, and deployment using Streamlit.

---

## Objectives

* To understand the complete Machine Learning workflow.
* To perform data preprocessing and data analysis.
* To build and compare different Machine Learning models.
* To deploy the best-performing model using Streamlit.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Joblib

---

## Machine Learning Models Used

The following models were trained and tested:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

Among these models, **Random Forest** provided the highest accuracy.

**Best Accuracy:** **75.61%**

---

## Dataset

The project uses the Loan Prediction dataset downloaded from Kaggle.

The dataset contains information such as:

* Gender
* Marital Status
* Number of Dependents
* Education
* Self Employment
* Applicant Income
* Co-applicant Income
* Loan Amount
* Loan Amount Term
* Credit History
* Property Area

---

## Project Folder Structure

```
Loan_Approval_Project/
│
├── Dataset/
├── Model/
├── Notebook/
├── Streamlit_App/
├── Documentation/
├── README.md
└── requirements.txt
```

---

## How to Run the Project

### Install the required libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
cd Streamlit_App
streamlit run app.py
```

---

## Project Outcome

The final application allows users to enter applicant details and predicts whether the loan is likely to be approved or rejected.

---

## Developed By

**Sushmita Tiwari**
