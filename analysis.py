import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

print("Student Data")
print(data)

print("\nAverage Marks")
print(data[['Math','Science','English']].mean())

data['Total'] = data[['Math','Science','English']].sum(axis=1)

top_student = data.loc[data['Total'].idxmax()]
print("\nTop Student:")
print(top_student)

data.set_index('Name')[['Math','Science','English']].plot(kind='bar')

plt.title("Student Marks Comparison")
plt.ylabel("Marks")
plt.show()
