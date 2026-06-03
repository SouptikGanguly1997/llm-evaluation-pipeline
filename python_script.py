import pandas as pd
import numpy as np

# 1. Base DataFrames
data_labels = {
    'task_id': [101, 102, 103, 104, 201, 202, 203, 204, 301, 302],
    'category': ['Finance', 'Finance', 'Finance', 'Finance', 'Healthcare', 'Healthcare', 'Healthcare', 'Healthcare', 'Retail', 'Retail'],
    'actual_label': ['Fraud', 'Legitimate', 'Fraud', 'Legitimate', 'Critical', 'Stable', 'Critical', 'Critical', 'Spam', 'Valid'],
    'is_edge_case': [True, True, True, False, True, True, True, True, True, True]
}
df_labels = pd.DataFrame(data_labels)

data_outputs = {
    'task_id': [101, 102, 103, 104, 201, 202, 203, 204, 301, 302],
    'predicted_label': ['Legitimate', 'Fraud', 'Fraud', 'Fraud', 'Stable', 'Stable', 'Critical', 'Critical', 'Spam', 'Valid'],
    'confidence_score': [0.85, 0.90, 0.95, 0.70, 0.88, 0.92, 0.99, 0.91, 0.95, 0.98]
}
df_outputs = pd.DataFrame(data_outputs)

# 2. Merge (Equivalent to SQL JOIN)
df_merged = pd.merge(df_labels, df_outputs, on='task_id', how='inner')

# 3. Filter Rows (Equivalent to SQL WHERE)
df_filtered = df_merged[df_merged['is_edge_case'] == True].copy()

# 4. Create Binary Flag (Equivalent to SQL CASE WHEN)
df_filtered['is_error'] = np.where(df_filtered['actual_label'] != df_filtered['predicted_label'], 1, 0)

# 5. Group and Aggregate (Equivalent to SQL GROUP BY & SELECT aggregation)
df_summary = df_filtered.groupby('category').agg(
    total_edge_cases=('is_error', 'count'),
    error_rate=('is_error', 'mean')  # Mean of 1s and 0s perfectly calculates the percentage rate
).reset_index()

# 6. Apply Group Filtering (Equivalent to SQL HAVING)
df_final = df_summary[df_summary['error_rate'] > 0.0]

# 7. Print Output Cleanly (Strictly without the standard dataframe row index)
print(df_final.to_string(index=False))