from pandas._libs.tslibs.timestamps import Timestamp
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd


def main():
    """ランキング
    ホテルごとの予約数に順位付けを行う
    同じ予約数の場合は同予約数の全ホテルに最小の順位をつける
    """
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

    # ホテルごとの予約数を算出
    rsv_count_by_hotel = reserve_tb.groupby('hotel_id')['reserve_id'].size().reset_index()
    rsv_count_by_hotel.rename(columns={'reserve_id': 'rsv_count'}, inplace=True)

    # 予約数ごとに順位を算出
    rsv_count_by_hotel['rsv_rank'] = rsv_count_by_hotel['rsv_count'].rank(ascending=False, method='min')


    # print(rsv_count_by_hotel.sort_values('rsv_rank'))
    # print(reserve_tb.query('hotel_id == "h_1" or hotel_id == "h_2"'))
    print(rsv_count_by_hotel)

if __name__ == '__main__':
    main()

