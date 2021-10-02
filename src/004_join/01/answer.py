from pandas._libs.tslibs.timestamps import Timestamp
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd


def main():
    """マスタテーブルの結合
    予約テーブルとホテルテーブルを結合して、宿泊人数が一人のビジネスホテルの予約レコードのみを抽出
    """
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    print(hotel_tb)
    print(reserve_tb)

    # 宿泊人数が一人の予約レコードを抽出
    reserve_tb_of_one_people = reserve_tb.query('people_num == 1')

    # ビジネスホテルのレコードを抽出
    business_hotel = hotel_tb.query('is_business')

    # ２つのテーブルをマージ
    print(pd.merge(reserve_tb_of_one_people, business_hotel, on='hotel_id', how='inner'))


if __name__ == '__main__':
    main()

