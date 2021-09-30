from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
import datetime


def main():
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    print(reserve_tb)
    reserve_tb['reserve_datetime']  = pd.to_datetime(reserve_tb['reserve_datetime'])
    # 1日追加
    reserve_tb['datetime_add_day'] = reserve_tb['reserve_datetime'] + datetime.timedelta(days=1)
    
    # 1時間追加
    reserve_tb['datetime_add_hour'] = reserve_tb['reserve_datetime'] + datetime.timedelta(hours=1)

    # 1分間追加
    reserve_tb['datetime_add_minute'] = reserve_tb['reserve_datetime'] + datetime.timedelta(minutes=1)

    # 1秒間追加
    reserve_tb['datetime_add_second'] = reserve_tb['reserve_datetime'] + datetime.timedelta(seconds=1)

    # 予約日に1日追加
    # 日付のみ抽出
    reserve_tb['reserve_date'] = reserve_tb['reserve_datetime'].dt.date
    reserve_tb['date_add_day'] = reserve_tb['reserve_date'] + datetime.timedelta(days=1)

    print(reserve_tb[['reserve_datetime', 'datetime_add_day', 'datetime_add_hour', 'datetime_add_hour',
    'datetime_add_minute', 'datetime_add_second', 'reserve_date', 'date_add_day']])


if __name__ == '__main__':
    main()