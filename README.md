# 🩺 Diabetes Prediction with SVM

This project applies a **Support Vector Machine (SVM)** model to predict whether a patient has diabetes based on medical diagnostic features. It uses data preprocessing, scaling, and model evaluation on the **Pima Indians Diabetes Dataset**.

---

## 📂 Project Structure

├── diabatescli.py # Main script (preprocessing, training, evaluation, prediction)
├── diabetes.csv # Dataset (Pima Indians Diabetes Dataset)
├── requirements.txt # Dependencies
└── README.md # Project documentation

---

## ⚙️ Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
🚀 How to Run

Clone the repository:

git clone https://github.com/omarfoud/diabetes-svm.git
cd diabetes-svm

Run the script:

python diabatescli.py

Outputs:

Console prints:

Training set accuracy

Test set accuracy

Prediction for a sample patient record

🔬 Approach
Data Preprocessing:

Standardizes features using StandardScaler.

Splits dataset into training (80%) and test (20%) sets with stratification.

Model:

Support Vector Machine (SVM) with linear kernel.

Evaluation:

Accuracy on both training and test sets.

Prediction:

Example prediction on a new patient record.

📊 Example Output
markdown
Training Set Performance
--------------------------------------------------
Accuracy: 0.7800

Test Set Performance
--------------------------------------------------
Accuracy: 0.7700

Prediction:
[1]
--------------------------------------------------
Diabetes
(Accuracy values may vary slightly depending on the random split.)

📌 Dataset
The dataset used is the Pima Indians Diabetes Dataset, which contains diagnostic measurements for women aged 21+ of Pima Indian heritage.

Features: Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age

Target: Outcome (1 = diabetes, 0 = no diabetes)

🤝 Contribution
Contributions are welcome! Open an issue or submit a pull request to improve the project.

