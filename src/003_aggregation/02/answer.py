from pandas._libs.tslibs.timestamps import Timestamp
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd


def main():
    """ホテルごとの宿泊人数別の合計予約金額
    """
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

    result = reserve_tb.groupby(['hotel_id', 'people_num'])['total_price']  \
        .sum().reset_index()
    result.rename(columns={'total_price': 'price_num'}, inplace=True)
    print(result)


if __name__ == '__main__':
    main()