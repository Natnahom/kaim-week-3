import seaborn as sns
import matplotlib.pyplot as plt

def box_plot(df, numeric_col):
    """Create a box plot to detect outliers."""
    sns.boxplot(x=df[numeric_col])
    plt.title(f'Box Plot of {numeric_col}')
    plt.show()

def creative_plots(df):
    """Create three insightful plots."""
    # Example Plot 1: TotalPremium over Time
    sns.lineplot(data=df, x='TransactionMonth', y='TotalPremium')
    plt.title('Total Premium Over Time')
    plt.show()

    # Example Plot 2: Claims by Citizenship
    sns.barplot(x='Citizenship', y='TotalClaims', data=df)
    plt.title('Total Claims by Citizenship')
    plt.show()

    # Example Plot 3: Premium Distribution by Vehicle Make
    sns.boxplot(x='make', y='TotalPremium', data=df)
    plt.title('Total Premium Distribution by Vehicle Make')
    plt.xticks(rotation=45)
    plt.show()