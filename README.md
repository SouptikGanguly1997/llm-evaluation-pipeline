# 📊 MLE-Bench: LLM Output Evaluation & Diagnostics Pipeline

## 🎯 Overview
This project is an automated, modular data analytics pipeline designed to evaluate Machine Learning model inferences against ground-truth benchmarks. It systematically identifies edge-case failure modes, calculates high-confidence error rates, and categorizes model stability across different domains.

The pipeline is built to process relational evaluation data using both **SQL (CTEs, Window Functions, Conditional Aggregation)** and **Python (Pandas, Vectorized NumPy Operations)**, ensuring high-speed diagnostics for ML engineering teams.

## 🏗️ Data Architecture
The evaluation framework relies on two primary relational structures:

1. **`benchmark_labels` (Ground Truth):** Contains the task identifiers, domain categories, actual correct labels, and boolean flags for complex edge-case prompts.
2. **`model_outputs` (Inferences):** Contains the AI's predicted labels and generated confidence scores (0.0 to 1.0) mapped via a `task_id` foreign key.

## 🛠️ Methodology & Execution

### 1. SQL Evaluation Engine
The SQL pipeline utilizes Chained Common Table Expressions (CTEs) to avoid messy subqueries and ensure query plan optimization. 

**Key Operations:**
* **Inner Joins:** Bridging predictions to ground truth.
* **Row-by-Row Evaluation:** Using `CASE WHEN` to binarize success/failure based on strict confidence thresholds (e.g., `confidence_score > 0.90`).
* **Statistical Filtering:** Applying `HAVING COUNT(*) > 2` to eliminate low-sample volatility and prevent skewed accuracy reporting.

### 2. Python Vectorized Validation
To ensure the pipeline can run locally on massive datasets without performance degradation, the Python evaluation script replaces standard `for` loops with hardware-optimized vectorized operations.

**Key Operations:**
* **Boolean Masking:** Filtering distributions for `is_edge_case == True`.
* **Vectorized Scoring:** Utilizing `np.where()` for instant column-wise string comparisons to flag hallucinations.
* **Aggregated Artifacts:** Generating clean, index-free tabular reports for stakeholder review.

