import pandas as pd

def clean_data():
    df = pd.read_csv("data/raw_sales.csv")

    # Convert date
    df['order_date'] = pd.to_datetime(df['order_date'])

    # Handle missing values
    df = df.dropna()

    # Remove duplicates
    df = df.drop_duplicates()

    df.to_csv("data/cleaned_sales.csv", index=False)
    print("Data cleaned and saved.")

if __name__ == "__main__":
    clean_data()
