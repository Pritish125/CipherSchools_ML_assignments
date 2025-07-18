
# 🧠 Employee Attrition Predictor

## 📌 Goal
Predict whether an employee is likely to leave the company using machine learning models. This is a binary classification task based on HR data.

## 🔍 Problem Statement
Employee attrition (i.e., when employees quit) is a major concern for HR departments. By analyzing employee data, we aim to identify patterns that contribute to attrition and build predictive models to flag high-risk employees.

## 📂 Dataset
The dataset used contains employee information such as:

| Feature           | Description                            |
|------------------|----------------------------------------|
| MonthlyIncome     | Monthly salary of the employee         |
| Age               | Age of the employee                    |
| JobSatisfaction   | Job satisfaction rating (1–4)          |
| YearsAtCompany    | Number of years the employee has been in the company |
| OverTime          | Whether the employee works overtime (Yes/No) |
| Attrition         | Target variable (Yes = Quit, No = Stay) |

## 📈 Models Used
We train and compare the performance of two classification models:

1. Logistic Regression
2. Decision Tree Classifier

## ⚙️ How to Run the Project

### 📦 Requirements
Make sure you have Python installed along with the following libraries:

```bash
pip install jupyter pandas scikit-learn matplotlib seaborn
```

### ▶️ Steps to Run in PyCharm (Professional Edition)
1. Open the project in PyCharm.
2. Create a new Jupyter Notebook file: `employee_attrition.ipynb`
3. Paste the provided cells (logistic regression, decision tree, etc.)
4. Place the `dataset.csv` file in the same directory.
5. Run each notebook cell in order.

## 📊 Evaluation Metrics
Both models are evaluated using:

- Accuracy
- Confusion Matrix
- Precision / Recall / F1-Score

You can compare the models' performance side by side to choose the best one for production or further tuning.

## 🧠 Real-World Applications
- HR Analytics: Identify high-risk employees and reduce turnover.
- Workforce Planning: Improve retention strategies.
- Resource Allocation: Focus on employees likely to churn.

## 📁 File Structure
```
employee-attrition/
├── dataset.csv
├── employee_attrition.ipynb
├── README.md
```

## 🚀 Future Improvements
- Add feature importance analysis
- Hyperparameter tuning
- Model saving (.pkl)
- Deploy via Flask/Streamlit for HR dashboards
