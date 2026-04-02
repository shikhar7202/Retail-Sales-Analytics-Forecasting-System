import pandas as pd

def create_features():
    df = pd.read_csv("data/cleaned_sales.csv")

    df['order_date'] = pd.to_datetime(df['order_date'])

    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month
    df['day'] = df['order_date'].dt.day
    df['weekday'] = df['order_date'].dt.weekday

    df.to_csv("data/cleaned_sales.csv", index=False)
    print("Features added.")

if __name__ == "__main__":
    create_features()
