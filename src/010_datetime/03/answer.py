from pandas.core.algorithms import diff
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd


def main():
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

    # チェックイン日時を生成する
    reserve_tb['checkin_datetime'] = pd.to_datetime(reserve_tb['checkin_date'] + reserve_tb['checkin_time'], format='%Y-%m-%d%H:%M:%S')

    # 予約日時を日時型に変換する
    reserve_tb['reserve_datetime'] = pd.to_datetime(reserve_tb['reserve_datetime'])

    # 年単位で差分計算
    diff_year = reserve_tb['reserve_datetime'].dt.year - reserve_tb['checkin_datetime'].dt.year
    print('年差分')
    print(diff_year)

    # 月単位で差分計算
    diff_month = (reserve_tb['reserve_datetime'].dt.year * 12 + reserve_tb['reserve_datetime'].dt.month) \
        - (reserve_tb['checkin_datetime'].dt.year * 12 + reserve_tb['checkin_datetime'].dt.month)
    print('月差分')
    print(diff_month)

    # 日単位で差分計算
    diff_day = (reserve_tb['reserve_datetime'] - reserve_tb['checkin_datetime']).astype('timedelta64[D]')
    print(diff_day)

    # 時単位で差分計算
    diff_hour = (reserve_tb['reserve_datetime'] - reserve_tb['checkin_datetime']).astype('timedelta64[h]')
    print(diff_hour)

    # 分単位で差分計算
    diff_minute = (reserve_tb['reserve_datetime'] - reserve_tb['checkin_datetime']).astype('timedelta64[m]')
    print(diff_minute)

    # 秒単位で差分計算
    diff_second = (reserve_tb['reserve_datetime'] - reserve_tb['checkin_datetime']).astype('timedelta64[s]')
    print(diff_second)

if __name__ == '__main__':
    main()