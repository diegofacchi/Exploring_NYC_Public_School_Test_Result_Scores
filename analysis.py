import pandas as pd

schools = pd.read_csv("D:/diego/Documents/MyProjects/Exploring_NYC_Public_School_Test_Result_Scores/schools.csv")
schools.head()

best_math_schools = schools[schools["average_math"] >=640] [["school_name", "average_math"]].sort_values("average_math", ascending=False)

schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools.sort_values("total_SAT", ascending=False)[["school_name", "total_SAT"]].head(10)

boroughs = schools.groupby("borough")["total_SAT"].agg(["count","mean", "std"]).round(2)
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})
