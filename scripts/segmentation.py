import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind

def data_segmentation(df):
    """Segment data into control and test groups based on a feature column."""
    required_columns = ['IsVATRegistered', 'Citizenship', 'LegalType', 'Title', 'Language',
                        'Bank', 'AccountType', 'MaritalStatus', 'Gender', 'Country', 
                        'Province', 'PostalCode', 'TotalPremium', 'TotalClaims']
    
    # Check for required columns
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"Missing columns: {missing_columns}")
        return None, None  # Return None if required columns are missing
    
    # Segment data into groups based on the 'IsVATRegistered' column
    group_a = df[df['IsVATRegistered'] == 'FALSE']  # Control group
    group_b = df[df['IsVATRegistered'] == 'TRUE']  # Test group
    
    return group_a, group_b

def statistical_testing(df):
    """Conduct statistical tests for categorical data."""
    # Example: Testing risk differences across provinces
    contingency_table = pd.crosstab(df['Province'], df['TotalClaims'])
    
    # Unpack all four return values
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)

    print("Chi-squared test p-value for risk differences across provinces:", p_value)
    if p_value < 0.05:
        print("Reject the null hypothesis: Risk differences exist across provinces.")
    else:
        print("Fail to reject the null hypothesis: No significant risk differences across provinces.")
    
    return p_value

def test_for_numerical(group_a, group_b):
    """Conduct statistical tests for numerical data."""
    # Example: Testing profit margin differences between groups
    total_premium_a = group_a['TotalPremium']
    total_premium_b = group_b['TotalPremium']

    t_stat, p_value = ttest_ind(total_premium_a, total_premium_b)

    print("T-test p-value for profit margin differences between groups:", p_value)
    if p_value < 0.05:
        print("Reject the null hypothesis: Significant profit margin differences exist between groups.")
    else:
        print("Fail to reject the null hypothesis: No significant profit margin differences between groups.")
    
    return p_value

def analyze_and_report(p_values):
    """Analyze and report the findings from the tests."""
    # Summary of findings
    findings = {
        "Risk differences across provinces": p_values[0],
        "Profit margin differences between groups": p_values[1],
    }

    for hypothesis, p_value in findings.items():
        if p_value < 0.05:
            print(f"{hypothesis}: Reject null hypothesis.")
        else:
            print(f"{hypothesis}: Fail to reject null hypothesis.")
