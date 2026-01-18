# Linear Regression from Scratch

This project demonstrates **Simple Linear Regression** implemented manually in Python. Instead of using high-level machine learning libraries (like Scikit-Learn's `LinearRegression`), these scripts explicitly define the Cost Function and Gradient Descent algorithms to optimize weights ($w$) and biases ($b$).

## 📂 File Overview

The project consists of two main scripts, each applying the algorithm to a different dataset:

### 1. `electricity_lin_reg.py`
* **Goal:** Predict electricity prices based on units consumed.
* **Dataset Required:** `electricity_bill_data.csv`
* **Hyperparameters:**
    * Learning Rate ($\alpha$): `0.000001` (Set very small to prevent divergence due to large feature values).
    * Iterations: `3000`
* **Visualization:** Plots the cost curve and the regression line against the dataset.

### 2. `linear_regression.py`
* **Goal:** Predict student test scores based on study hours.
* **Dataset Required:** `student_scores.csv`
* **Hyperparameters:**
    * Learning Rate ($\alpha$): `0.01`
    * Iterations: `1500`
* **Feature:** Includes a specific prediction output for a student studying **7 hours**.

---

## 🛠️ Dependencies

To run these scripts, you will need the following Python libraries:

```bash
pip install numpy pandas matplotlib
