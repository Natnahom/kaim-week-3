import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score, precision_score, recall_score

def prepare_data(df):
    """Prepare data for modeling by handling missing values and splitting the dataset."""
    # Example: Fill missing values or drop them
    df.fillna(df.mean(), inplace=True)  # Filling numeric columns with mean
    
    # Convert categorical variables to dummy variables
    df = pd.get_dummies(df, drop_first=True)

    # Define features and target variable
    X = df.drop(columns=['TotalClaims'])  # Features
    y = df['TotalClaims']  # Target variable

    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_models(X_train, y_train):
    """Train multiple models and return the trained models."""
    models = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier()
    }

    trained_models = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model
        print(f"{name} trained.")

    return trained_models

def evaluate_models(trained_models, X_test, y_test):
    """Evaluate models using accuracy for classification and MAE/RMSE for regression."""
    for name, model in trained_models.items():
        if isinstance(model, LinearRegression):
            # Predictions for regression model
            y_pred = model.predict(X_test)
            mae = mean_absolute_error(y_test, y_pred)
            rmse = mean_squared_error(y_test, y_pred, squared=False)
            print(f"{name} - MAE: {mae}, RMSE: {rmse}")
        else:
            # Predictions for classification models
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
            recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
            print(f"{name} - Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}")

# if __name__ == "__main__":
#     # Load dataset
#     df = pd.read_csv('data/insurance_data.csv')

#     # Prepare data
#     X_train, X_test, y_train, y_test = prepare_data(df)

#     # Train models
#     trained_models = train_models(X_train, y_train)

#     # Evaluate models
#     evaluate_models(trained_models, X_test, y_test)