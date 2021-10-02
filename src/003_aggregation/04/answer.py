from pandas._libs.tslibs.timestamps import Timestamp
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
import numpy as np


def main():
    """各ホテルの予約金額の分散値と標準偏差を算出
    ただし、予約が1件しかない場合は、分散値と標準偏差値を0とする
    """
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    print(reserve_tb)

    # agg関数を利用して分散と標準偏差を算出
    result = reserve_tb.groupby('hotel_id') \
        .agg({'total_price': ['var', 'std']}).reset_index()
    result.columns = ['hotel_id', 'price_var', 'price_std']

    # 計算できないものはnaとなってしまっているので0で埋める
    result.fillna(value={'price_var': 0, 'price_std': 0}, inplace=True)
    print(result)


if __name__ == '__main__':
    main()
