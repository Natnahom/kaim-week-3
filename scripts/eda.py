import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def descriptive_statistics(df):
    """Calculate descriptive statistics for numerical features."""
    return df.describe()

def univariate_analysis(df, numerical_cols, categorical_cols):
    """Create histograms for numerical columns and bar charts for categorical columns."""
    for col in numerical_cols:
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()

    for col in categorical_cols:
        sns.countplot(x=col, data=df)
        plt.title(f'Count of {col}')
        plt.show()

def correlation_analysis(df):
    """Explore correlation between TotalPremium and TotalClaims."""
    # Convert date columns if needed
    if 'TransactionMonth' in df.columns:
        df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
        df['TransactionMonth'] = df['TransactionMonth'].astype(int) // 10**9  # Convert to Unix timestamp

    # Select numeric columns for correlation
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df_numeric = df[numeric_cols]

    sns.scatterplot(data=df, x='TotalPremium', y='TotalClaims')
    plt.title('TotalPremium vs TotalClaims')
    plt.show()

    correlation_matrix = df_numeric.corr()
    sns.heatmap(correlation_matrix, annot=True)
    plt.title('Correlation Matrix')
    plt.show()