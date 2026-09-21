def engineer_features(df):

    df = df.copy()

    print("Starting feature engineering...")

    # Create FamilySize
    df["FamilySize"] = (
        df["SibSp"] +
        df["Parch"] +
        1
    )

    # Create IsAlone
    df["IsAlone"] = (
        df["FamilySize"] == 1
    ).astype(int)

    # Create FarePerPerson
    df["FarePerPerson"] = (
        df["Fare"] / df["FamilySize"]
    )

    # Remove unnecessary columns
    df = df.drop(
        columns=["Name", "Ticket", "Cabin"],
        errors="ignore"
    )

    print("Feature engineering completed")

    return df
