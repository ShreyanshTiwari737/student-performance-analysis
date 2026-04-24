import sys
sys.path.insert(0, 'src')
from preprocess import load_data, handle_missing, remove_outliers, feature_engineering
from analysis import basic_stats, top_students, low_performers, group_analysis, insights
import pandas as pd
print("=" * 50)
print("  STUDENT PERFORMANCE ANALYSIS SYSTEM")
print("=" * 50)
df= load_data('data/student_dataset_v2.csv')
df= handle_missing(df)
df= remove_outliers(df)
df= feature_engineering(df)
basic_stats(df)
top_students(df)
low_performers(df)
group_analysis(df)
insights(df)
print("\nAnalysis complete.")
