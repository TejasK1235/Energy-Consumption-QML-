# 🔮 Predicting Energy Consumption using Quantum ML

Energy is one of the most valuable resources today—but it’s also one of the most wasted. This research-driven project aims to predict **total energy consumption** across the world using **both classical machine learning** and **quantum-inspired models**. By comparing performance, the project explores whether **quantum machine learning (QML)** can provide meaningful improvements in complex prediction tasks involving real-world data.

> ⚡️ **Highlight:** Random Forest achieved an R² of **0.92**, followed closely by Quantum Kernel Ridge Regression with an R² of **0.88**, showcasing the promise of QML even in non-quantum environments.

---

## 📌 Motivation

The project was inspired by the growing need for energy efficiency and the emerging potential of quantum computing in machine learning. While quantum hardware is still evolving, **quantum-inspired algorithms** can already be simulated in classical environments to explore their feasibility and effectiveness.

---

## 🧠 Models Used

### 🔁 Classical ML Models
- Linear Regression
- Decision Tree Regressor
- Support Vector Regressor (SVR)
- K-Nearest Neighbors (KNN)
- Gradient Boosting Regressor
- Random Forest Regressor

### 🧬 Quantum-Inspired Models (Implemented from Scratch)
- Quantum Kernel Ridge Regression (QKRR)
- Quantum Linear Regression

> All quantum simulations were coded **from scratch in Python** using custom quantum feature maps and kernels — **no Qiskit or external quantum libraries used**.

---

## 📊 Dataset

- **Source:** [Our World in Data (OWID)](https://github.com/owid/energy-data)
- **Synthetic Data Generator:** OWID provides a script to generate up-to-date synthetic data.
- **Target:** Total Energy Consumption
- For detailed feature descriptions, refer to: `data/owid_energy_codebook.csv` or the [OWID data repository](https://github.com/owid/energy-data).

---

## 📈 Performance Comparison

[Performance Comparison Plot](https://github.com/TejasK1235/Energy-Consumption-QML-/blob/main/artifacts/Performance_Comparison.png)

This plot compares actual vs. predicted energy consumption values across all models used in the project.

---

## 🗂️ Repository Structure

```
├── artifacts/
│ ├── classical models/ (all .pkl files)
│ ├── Quantum Models/
│ └── performance_comparison.jpg
├── data/
│ ├── cleaned.csv
│ ├── quantum_cleaned.csv
│ ├── owid_energy_codebook.csv
│ └── owid_energy_data.csv
├── notebooks/
│ ├── Classic/
│ │ ├── EDA & cleaning.ipynb
│ │ ├── base models.ipynb
│ │ └── Classical Models.ipynb
│ └── Quantum/
│ ├── Quantum EDA & Cleaning.ipynb
│ └── Quantum Models.ipynb
├── make_dataset.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```


---

## ⚙️ Requirements

```bash
pandas
numpy
matplotlib
seaborn
scikit-learn
dill
flask
owid.catalog
openpyxl
```
Install them via:
```
pip install -r requirements.txt
```
# ▶️ How to Use

Since this is a research-focused project, you can explore results and model training in the Jupyter notebooks:

## Open notebooks and explore

To view the final model comparison results, see:

    notebooks/Classic/Classical Models.ipynb

    notebooks/Quantum/Quantum Models.ipynb

    artifacts/performance_comparison.jpg

🏷️ Acknowledgments

    Our World in Data (OWID) – for the dataset and documentation.

# 🧪 Status

The research is currently complete. Future iterations may include deeper quantum circuit simulations or hardware-backed testing.


---
