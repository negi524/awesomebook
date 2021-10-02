from pandas._libs.tslibs.timestamps import Timestamp
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd


def main():
    """最頻値の算出
    予約テーブルの予約金額を1000単位にカテゴリ化して最頻値を算出
    """
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    price_mode = reserve_tb['total_price'].round(-3).mode()
    print(price_mode)


if __name__ == '__main__':
    main()
