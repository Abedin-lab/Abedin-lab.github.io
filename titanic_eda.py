import os
import io
import pandas as pd
# pyrefly: ignore [missing-import]
import numpy as np
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
import seaborn as sns

# Set plotting backend to non-interactive
plt.switch_backend('Agg')

# Set aesthetic styling
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.figsize'] = (10, 6)

# Colors matching premium palette
SURVIVED_PALETTE = {0: '#e74c3c', 1: '#2ecc71'} # Red/Green
SEX_PALETTE = {'male': '#3498db', 'female': '#e91e63'} # Blue/Pink
CLASS_PALETTE = {1: '#ffd700', 2: '#c0c0c0', 3: '#cd7f32'} # Gold/Silver/Bronze

def download_data():
    csv_path = 'titanic.csv'
    if not os.path.exists(csv_path):
        print("Dataset not found locally. Downloading Titanic dataset...")
        import urllib.request
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
        urllib.request.urlretrieve(url, csv_path)
        print("Download complete.")
    else:
        print("Dataset already exists locally.")

def run_eda():
    # ----------------------------------------------------
    # Task 1: Data Loading and Initial Inspection
    # ----------------------------------------------------
    print("\n" + "="*50)
    print("TASK 1: Data Loading & Initial Inspection")
    print("="*50)
    
    df = pd.read_csv('titanic.csv')
    
    print("\n--- First 5 Rows ---")
    print(df.head())
    
    print("\n--- Data Types (.info()) ---")
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    print(info_str)
    
    print("\n--- Descriptive Statistics ---")
    print(df.describe())
    
    print("\n--- Missing Values Count per Column ---")
    missing_counts = df.isnull().sum()
    print(missing_counts)
    
    # ----------------------------------------------------
    # Task 2: Handling Missing Values
    # ----------------------------------------------------
    print("\n" + "="*50)
    print("TASK 2: Handling Missing Values")
    print("="*50)
    
    # Cabin Missing Percentage
    cabin_missing_pct = (df['Cabin'].isnull().sum() / len(df)) * 100
    print(f"Percentage of missing values in 'Cabin': {cabin_missing_pct:.2f}%")
    
    # Embarked Imputation
    embarked_mode = df['Embarked'].mode()[0]
    print(f"Most frequent port of embarkation (mode): {embarked_mode}")
    df['Embarked'] = df['Embarked'].fillna(embarked_mode)
    
    # Age Imputation
    age_median = df['Age'].median()
    print(f"Median age: {age_median}")
    df['Age'] = df['Age'].fillna(age_median)
    
    # Verify imputation
    print("\nMissing values after imputation:")
    print(df[['Age', 'Cabin', 'Embarked']].isnull().sum())
    
    # Ensure plots directory exists
    os.makedirs('plots', exist_ok=True)
    
    # ----------------------------------------------------
    # Task 3: Univariate Analysis
    # ----------------------------------------------------
    print("\n" + "="*50)
    print("TASK 3: Univariate Analysis")
    print("="*50)
    
    # Survival Rate
    survived_count = df['Survived'].value_counts()
    survival_rate = (df['Survived'].mean()) * 100
    print(f"Overall Survival Rate: {survival_rate:.2f}%")
    
    # Plot Survival Rate Count
    plt.figure()
    ax = sns.countplot(data=df, x='Survived', palette=SURVIVED_PALETTE, hue='Survived', legend=False)
    plt.title('Distribution of Passenger Survival', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Survived (0 = No, 1 = Yes)', fontsize=12)
    plt.ylabel('Passenger Count', fontsize=12)
    # Add count labels on top of bars
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    plt.tight_layout()
    plt.savefig('plots/survived_distribution.png', dpi=300)
    plt.close()
    
    # Passenger Class Distribution
    pclass_counts = df['Pclass'].value_counts()
    most_frequent_class = pclass_counts.idxmax()
    print(f"Passenger count by Class:\n{pclass_counts}")
    print(f"Class with most passengers: Class {most_frequent_class}")
    
    plt.figure()
    ax = sns.countplot(data=df, x='Pclass', palette='viridis', hue='Pclass', legend=False)
    plt.title('Distribution of Passenger Class (Pclass)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Ticket Class (Pclass)', fontsize=12)
    plt.ylabel('Passenger Count', fontsize=12)
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    plt.tight_layout()
    plt.savefig('plots/pclass_distribution.png', dpi=300)
    plt.close()
    
    # Age Distribution Histogram
    plt.figure()
    sns.histplot(data=df, x='Age', kde=True, color='#818cf8', bins=30)
    plt.title('Passenger Age Distribution (with Median Imputed)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Age (Years)', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.axvline(age_median, color='red', linestyle='--', label=f'Median Age: {age_median}')
    plt.legend()
    plt.tight_layout()
    plt.savefig('plots/age_distribution.png', dpi=300)
    plt.close()
    
    # ----------------------------------------------------
    # Task 4: Bivariate and Multivariate Analysis
    # ----------------------------------------------------
    print("\n" + "="*50)
    print("TASK 4: Bivariate & Multivariate Analysis")
    print("="*50)
    
    # Survival by Sex
    sex_crosstab = pd.crosstab(df['Sex'], df['Survived'])
    print("\nSurvival by Sex (Count):")
    print(sex_crosstab)
    
    sex_survival_pct = df.groupby('Sex')['Survived'].mean() * 100
    print("\nSurvival Rate by Sex:")
    print(sex_survival_pct)
    
    plt.figure()
    # Grouped count plot of survival by sex
    ax = sns.countplot(data=df, x='Sex', hue='Survived', palette=SURVIVED_PALETTE)
    plt.title('Survival Count by Sex', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Sex', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.legend(title='Survived', labels=['No', 'Yes'])
    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    plt.tight_layout()
    plt.savefig('plots/survival_by_sex.png', dpi=300)
    plt.close()
    
    # Survival by Pclass
    pclass_survival_pct = df.groupby('Pclass')['Survived'].mean() * 100
    print("\nSurvival Rate by Pclass:")
    print(pclass_survival_pct)
    
    plt.figure()
    ax = sns.barplot(data=df, x='Pclass', y='Survived', palette='viridis', hue='Pclass', errorbar=None, legend=False)
    plt.title('Survival Rate by Ticket Class (Pclass)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Ticket Class (Pclass)', fontsize=12)
    plt.ylabel('Survival Rate (Probability)', fontsize=12)
    for p in ax.patches:
        ax.annotate(f'{p.get_height()*100:.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    plt.tight_layout()
    plt.savefig('plots/survival_by_pclass.png', dpi=300)
    plt.close()
    
    # Survival by Age
    plt.figure()
    sns.kdeplot(data=df[df['Survived'] == 0], x='Age', fill=True, color='#e74c3c', label='Died (Survived=0)', alpha=0.5)
    sns.kdeplot(data=df[df['Survived'] == 1], x='Age', fill=True, color='#2ecc71', label='Survived (Survived=1)', alpha=0.5)
    plt.title('Age Distribution comparison: Survivors vs Non-Survivors', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Age (Years)', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.legend()
    plt.tight_layout()
    plt.savefig('plots/survival_by_age.png', dpi=300)
    plt.close()
    
    # Survival by Embarked
    embarked_survival_pct = df.groupby('Embarked')['Survived'].mean() * 100
    print("\nSurvival Rate by Embarked Port:")
    print(embarked_survival_pct)
    
    plt.figure()
    ax = sns.barplot(data=df, x='Embarked', y='Survived', palette='muted', hue='Embarked', errorbar=None, legend=False)
    plt.title('Survival Rate by Port of Embarkation', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Port of Embarkation', fontsize=12)
    plt.ylabel('Survival Rate (Probability)', fontsize=12)
    # Ensure they map correctly
    plt.xticks(ticks=[0, 1, 2], labels=['Southampton (S)', 'Cherbourg (C)', 'Queenstown (Q)'])
    for p in ax.patches:
        ax.annotate(f'{p.get_height()*100:.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    plt.tight_layout()
    plt.savefig('plots/survival_by_embarked.png', dpi=300)
    plt.close()
    
    return df

if __name__ == '__main__':
    download_data()
    df = run_eda()
    print("\nEDA completed. All plots are saved in the 'plots/' directory.")
