from pandas_profiling import ProfileReport
import pandas as pd
df = pd.read_csv("credit_data/case_study_devdata.csv")
# display(df.head(5))
df = df.drop(["primary_key","merchant_name"], axis = 1)
profile = ProfileReport(df,minimal=True)
profile.to_file("Analysis.html")