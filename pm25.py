import pandas as pd


def get_pm25():
    url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=CSV"
    df = pd.read_csv(url).dropna()
    columns = df.columns
    values = df.values.tolist()
    return columns, values


if __name__ == "__main__":  # 要這樣寫以避免外部引用時會呼叫到測試邏輯
    print(get_pm25())
