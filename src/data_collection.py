import pandas as pd
import os


def collect_data():

    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

    output_path = "data/raw/titanic.csv"

    os.makedirs("data/raw", exist_ok=True)

    df = pd.read_csv(url)

    df.to_csv(output_path, index=False)

    print("Data collected successfully")
    print("Shape:", df.shape)

    return df


if __name__ == "__main__":
    collect_data()
