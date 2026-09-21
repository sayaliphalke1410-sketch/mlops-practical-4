def validate_data(df):

    print("Starting data validation...")

    assert not df.empty, "Dataset is empty"

    assert df.duplicated().sum() == 0, \
        "Duplicate data found"

    assert df.isnull().sum().sum() == 0, \
        "Missing values found"

    required_columns = [
        "PassengerId",
        "Survived",
        "Pclass",
        "Age",
        "Fare"
    ]

    for column in required_columns:
        assert column in df.columns, \
            f"Missing column: {column}"

    assert (df["Age"] >= 0).all(), \
        "Invalid Age"

    assert (df["Fare"] >= 0).all(), \
        "Invalid Fare"

    print("Data validation passed")

    return True
