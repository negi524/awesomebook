from pandas._libs.tslibs.timestamps import Timestamp
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
import numpy as np


def main():
    """ホテルごとの予約金額の最大値、平均値、中央値、20パーセンタイル値を算出
    """
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    print(reserve_tb)
    result = reserve_tb.groupby('hotel_id') \
        .agg({'total_price': ['max', 'min', 'mean', 'median', lambda x: np.percentile(x, q=20)]}) \
            .reset_index()
    result.columns = ['hotel_id', 'price_max', 'price_min', 'price_mean', 'price_median', 'price_20_percentile']
    print(result)


if __name__ == '__main__':
    main()