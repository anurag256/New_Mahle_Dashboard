import pandas as pd


def dataBetweenDates(df: pd.DataFrame, endDate: str, startDate: str) -> pd.DataFrame:
    df['DATE'] = pd.to_datetime(df['DATE'], format="%d-%m-%Y", dayfirst=True)
    # Filter data between starting_date and end_date
    filtered_data = df[(df['DATE'] >= startDate) & (df['DATE'] <= endDate)]
    return filtered_data


def monthlyData(df: pd.DataFrame):
    df['DATE'] = pd.to_datetime(df['Date'], format="%d-%m-%Y", dayfirst=True)
    current_month = pd.Timestamp('now').to_period('M')
    monthly_data = df[((df['Date'].dt.to_period('M')) == current_month)]
    return monthly_data
