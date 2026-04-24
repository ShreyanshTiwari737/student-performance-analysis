import pandas as pd
def basic_stats(df):
    print("\n--- Basic Statistics ---")
    print(df[['StudyHours', 'Attendance', 'Marks']].describe())
def top_students(df, n=5):
    print(f"\n--- Top {n} Students ---")
    print(df.nlargest(n, 'Marks')[['StudyHours', 'Attendance', 'Marks', 'Performance']])
def low_performers(df, threshold=50):
    print(f"\n--- Students with Marks < {threshold} ---")
    low = df[df['Marks'] < threshold]
    print(low[['StudyHours', 'Attendance', 'Marks']])
    print("Count:", len(low))
def group_analysis(df):
    print("\n--- Avg Marks by Attendance Level ---")
    df['AttendanceLevel'] = pd.cut(df['Attendance'], bins=[0,60,80,100],labels=['Low','Medium','High'])
    print(df.groupby('AttendanceLevel', observed=True)['Marks'].mean())
    print("\n--- Avg Marks by Study Category ---")
    df['StudyCategory'] = pd.cut(df['StudyHours'], bins=[0,3,6,15],labels=['Low','Medium','High'])
    print(df.groupby('StudyCategory', observed=True)['Marks'].mean())
def insights(df):
    print("\n--- Key Insights ---")
    corstudy = df['StudyHours'].corr(df['Marks'])
    coratt= df['Attendance'].corr(df['Marks'])
    avgexc= df[df['Performance']=='Excellent']['StudyHours'].mean()
    avgni= df[df['Performance']=='Needs Improvement']['StudyHours'].mean()
    pctlow= (df['Marks'] < 50).mean() * 100
    print(f"1. Correlation of StudyHours with Marks: {corr_study:.2f}")
    print(f"2. Correlation of Attendance with Marks: {corr_att:.2f}")
    print(f"3. Avg study hours — Excellent: {avg_exc:.1f} hrs, Needs Improvement: {avg_ni:.1f} hrs")
    print(f"4. {pct_low:.1f}% of students scored below 50")
    print(f"5. EffortScore (StudyHours × Attendance) top quartile avg marks: "f"{df[df['EffortScore'] >= df['EffortScore'].quantile(0.75)]['Marks'].mean():.1f}")
