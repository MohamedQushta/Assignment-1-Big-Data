import pandas as pd
import numpy as np
import sys
import math
from sklearn.preprocessing import MinMaxScaler
import subprocess
#Data Cleaning, Data Transformation, Data Reduction, and Data Discretization

def clean_data(df):
    df = df.drop_duplicates()
    # Fill null values with mean for numerical columns and mode for categorical columns
    for column in df.columns:
        if df[column].dtype == 'object':
         # For categorical columns, fill null values with mode
          mode_value = df[column].mode()[0]
          df[column] = df[column].fillna(mode_value)
        else:
        # For numerical columns, fill null values with mean
          mean_value = df[column].mean()
          df[column] = df[column].fillna(mean_value)
    return df

def transform_data(df):
    # #Creating a MinMaxScaler to fit and transform the numerical columns
    # numerical_columns = df.select_dtypes(include=['number']).columns
    # scaler = MinMaxScaler()
    # df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

    # # Log transformation of numerical data
    # for column in df.columns:
    #     if pd.api.types.is_numeric_dtype(df[column]):
    #         df[column] = df[column].apply(lambda x: math.log(x) if x > 0 else 0)

    #Creating "GPA" and "above average" columns 
    df['gender'] = df['gender'].replace({'male':0, 'female':1}).infer_objects(copy=False)
    # Replace values in the "lunch" column
    df['lunch'] = df['lunch'].replace({'standard': 1, 'free/reduced': 0}).infer_objects(copy=False)
    # Replace values in the "lunch" column
    df['test preparation course'] = df['test preparation course'].replace({'completed': 1, 'none': 0}).infer_objects(copy=False)

    df["GPA"]=round((df["math score"]+df["reading score"]+df["writing score"])/3,2)
    Avg_score = df['GPA'].mean()
    df['above average']= np.where(df['GPA']>Avg_score,'above','below')
    df['above average'] = df['above average'].replace({'above': 1, 'below': 0}).infer_objects(copy=False)
    df = pd.get_dummies(df)

    return df

def reduce_data(df):
    # Example data reduction tasks
    # Task 1: Remove unnecessary columns
    #low variance filter
    numeric = df[['math score', 'writing score', 'reading score']]
    var = numeric.var()
    variables = []

    for i in range(len(var)):
        if var[i] >= 10:   # setting the threshold as 10%
          variables.append(numeric.columns[i])
    
    corr = df.corr()['GPA']

    threshold = 0.2

    # Filter out columns with correlation below the threshold
    low_corr_col = corr[abs(corr) < threshold].index
    low_corr_col = [col.strip() for col in low_corr_col]

    # Drop the columns with low correlation
    df = df.drop(columns=low_corr_col[1:])

    return df

# def discretize_data(df):
#     # Example data discretization tasks
#     # Task 1: Binning numerical variables
#     df['binned_column'] = pd.cut(df['numerical_column'], bins=3, labels=['Low', 'Medium', 'High'])
    
#     # Task 2: Discretize categorical variables
#     df['categorical_column'] = pd.qcut(df['categorical_column'], q=3, labels=['Small', 'Medium', 'Large'])
    
#     return df

def save_to_csv(df, file_path):
    df.to_csv(file_path, index=False)

def run_eda(file_path):
    subprocess.run(["python", "eda.py", file_path])

if __name__ == "__main__":
    # Check if the file path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python dpre.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Read the DataFrame from the CSV file
    df = pd.read_csv(file_path)
    
    # Perform Data Cleaning
    df = clean_data(df)
    
    # Perform Data Transformation
    df = transform_data(df)
    
    # Perform Data Reduction
    df = reduce_data(df)
    
    # Perform Data Discretization
    #df = discretize_data(df)
    
    # Save the resulting DataFrame as a new CSV file
    save_to_csv(df, "res_dpre.csv")
    run_eda("res_dpre.csv")