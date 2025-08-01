Task # 3

import numpy as np
plt.figure(figsize=(10, 6))
sns.barplot(x='Property_Area', y='LoanAmount', hue='Self_Employed', data=df, estimator=np.median)
plt.title('Median Loan Amount by Property Area and Employment Type')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Dependents', hue='Married', data=df)
plt.title('Dependents Count by Marital Status')
plt.show()

# Visualize key features
plt.figure(figsize=(15,10))

# Loan Amount distribution
plt.subplot(2,2,1)
sns.histplot(df['LoanAmount'], kde=True)
plt.title('Loan Amount Distribution')

# Income vs Loan Amount
plt.subplot(2,2,2)
sns.scatterplot(x='ApplicantIncome', y='LoanAmount', hue='Education', data=df)
plt.title('Income vs Loan Amount by Education')

# Property Area distribution
plt.subplot(2,2,3)
sns.countplot(x='Property_Area', data=df)
plt.title('Loan Approval by Property Area')

plt.tight_layout()
plt.show()