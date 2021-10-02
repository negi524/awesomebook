from pandas._libs.tslibs.timestamps import Timestamp
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd


def main():
    """順位の算出
    顧客ごとに予約日時の順位を古い順につける
    同じ予約日時の場合はデータ行の読み込み順に小さな順位をつける
    """
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

    # 予約日時のデータ型をDateTime型に変換する
    reserve_tb['reserve_datetime'] = pd.to_datetime(reserve_tb['reserve_datetime'])

    reserve_tb['log_no'] = reserve_tb.groupby('customer_id')['reserve_datetime'] \
        .rank(ascending=True, method='first')   # 昇順、重複値は登録順

    print(reserve_tb.head(20))


if __name__ == '__main__':
    main()
