# ========================================
# 📊 Basic Data Analysis using Pandas & Matplotlib
# ========================================

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------
# STEP 1: Create or load a CSV file
# ------------------------------------------------

# Let's create a simple sample dataset (so you can test it easily)
data = {
    "Student": ["Student_1", "Student_2", "Student_3", "Student_4", "Student_5"],
    "Hours_Studied": [2, 5, 7, 1, 8],
    "Score": [55, 70, 88, 40, 92],
    "Attendance": [75, 85, 95, 60, 98]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Save as CSV file (you can open it later)
df.to_csv("student_data.csv", index=False)
print("✅ Sample CSV file 'student_data.csv' created!")

# ------------------------------------------------
# STEP 2: Load the CSV using Pandas
# ------------------------------------------------
df = pd.read_csv("student_data.csv")
print("\n📄 Loaded Data from CSV:\n")
print(df)

# ------------------------------------------------
# STEP 3: Perform basic data analysis
# ------------------------------------------------

# Display some summary statistics
print("\n📊 Summary Statistics:\n")
print(df.describe())

# Calculate average of a selected column
average_score = df["Score"].mean()
print(f"\n📈 Average Score: {average_score:.2f}")

# ------------------------------------------------
# STEP 4: Create Visualizations using Matplotlib
# ------------------------------------------------

# Bar Chart - Students vs Scores
plt.figure(figsize=(6, 4))
plt.bar(df["Student"], df["Score"], color="skyblue")
plt.title("Scores of Students")
plt.xlabel("Student")
plt.ylabel("Score")
plt.show()

# Scatter Plot - Hours Studied vs Score
plt.figure(figsize=(6, 4))
plt.scatter(df["Hours_Studied"], df["Score"], color="green")
plt.title("Hours Studied vs Score")
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.show()

# Heatmap (Correlation)
plt.figure(figsize=(5, 4))
correlation = df.corr(numeric_only=True)
plt.imshow(correlation, cmap="coolwarm", interpolation="nearest")
plt.title("Correlation Heatmap")
plt.colorbar()
plt.xticks(range(len(correlation)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation)), correlation.columns)
plt.show()

# ------------------------------------------------
# STEP 5: Observations
# ------------------------------------------------
print("\n🧠 Observations:")
print("- Students who studied more hours generally scored higher.")
print("- There’s a strong positive correlation between Hours Studied and Score.")
print("- Attendance might also influence performance slightly.")
print("- The average score across all students is {:.2f}".format(average_score))