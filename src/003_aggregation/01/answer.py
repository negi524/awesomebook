from pandas._libs.tslibs.timestamps import Timestamp
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd


def main():
    """ホテルごとに予約件数と予約したことのある顧客数を出す
    """
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    print(reserve_tb)

    # agg関数を使ってまとめて集約処理を適用する
    temp = reserve_tb.groupby('hotel_id').agg({'reserve_id': 'count', 'customer_id': 'nunique'})
    temp.reset_index(inplace=True)
    temp.columns = ['hotel_id', 'rsv_count', 'customer_count']
    print(temp)


if __name__ == '__main__':
    main()