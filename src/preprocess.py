import pandas as pd
import numpy as np
def load_data(path):
    df = pd.read_csv(path)
    print("Dataset loaded. Shape:", df.shape)
    print(df.head())
    return df
def handle_missing(df):
    df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
    df['StudyHours'] = df['StudyHours'].fillna(df['StudyHours'].median())
    print("Missing values handled.")
    return df
def remove_outliers(df):
    df=df[df['StudyHours'] <= 15]
    df=df[df['Marks'] <= 100]
    print("Outliers removed. Shape:", df.shape)
    return df
def feature_engineering(df):
    conditions= [df['Marks'] >= 80, df['Marks'] >= 60]
    choices= ['Excellent', 'Good']
    df['Performance']= np.select(conditions, choices, default='Needs Improvement')
    df['EffortScore']= df['StudyHours'] * df['Attendance']
    print("Features created: Performance, EffortScore")
    return df
