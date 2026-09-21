def preprocess_data(df):

    df = df.copy()

    print("Starting preprocessing...")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    df["Embarked"] = df["Embarked"].fillna(
        df["Embarked"].mode()[0]
    )

    # Fill missing cabin
    df["Cabin"] = df["Cabin"].fillna("Unknown")

    # Convert gender into numbers
    df["Sex"] = df["Sex"].map({
        "male": 0,
        "female": 1
    })

    print("Preprocessing completed")

    return df
