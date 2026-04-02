import pandas as pd
from prophet import Prophet

def forecast_sales():
    df = pd.read_csv("data/cleaned_sales.csv")

    df = df.groupby('order_date')['sales'].sum().reset_index()
    df.columns = ['ds', 'y']

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    forecast[['ds', 'yhat']].to_csv("outputs/forecast.csv", index=False)
    print("Forecast generated.")

if __name__ == "__main__":
    forecast_sales()
