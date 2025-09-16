# 🌸 Iris Dataset Analysis & Visualization

This project is part of the **PLP Academy Week 7 Assignment**: *Analyzing Data with Pandas and Visualizing Results with Matplotlib*. It demonstrates how to load, clean, analyze, and visualize the classic Iris dataset using Python libraries like `pandas`, `matplotlib`, and `seaborn`.

---

## 📁 Dataset

- **Source**: [Iris Dataset CSV](https://gist.githubusercontent.com/Thanatoz-1/9e7fdfb8189f0cdf5d73a494e4a6392a/raw/iris_dataset.csv)
- **Features**:
  - `sepal length (cm)`
  - `sepal width (cm)`
  - `petal length (cm)`
  - `petal width (cm)`
  - `target` (species)

---

## 🧪 Tasks Performed

### Task 1: Data Loading & Cleaning
- Loaded the dataset using `pandas.read_csv()`
- Displayed the first few rows with `.head()`
- Checked for missing values and data types
- Cleaned the dataset by dropping any missing values

### Task 2: Basic Data Analysis
- Computed descriptive statistics using `.describe()`
- Grouped data by species and calculated mean values
- Identified patterns in feature distributions across species

### Task 3: Data Visualization
Created four customized plots using `matplotlib` and `seaborn`:
1. **Line Chart** – Sepal length trend over simulated time
2. **Bar Chart** – Average petal length per species
3. **Histogram** – Distribution of sepal width
4. **Scatter Plot** – Sepal length vs. petal length by species

---

## 📊 Visualization Highlights

- **Setosa** species has the smallest petal dimensions.
- **Virginica** shows the largest measurements across most features.
- Scatter plot reveals clear clustering, ideal for classification.

---

## 🛠️ Technologies Used

- Python 3.x
- pandas
- matplotlib
- seaborn

---

## 🚀 How to Run

1. Clone this repository or download the `.py` or `.ipynb` file.
2. Ensure required libraries are installed:
   ```bash
   pip install pandas matplotlib seaborn
