from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd


def main():
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    reserve_tb.info()
    print(reserve_tb)

    # reserve_datetimeを日時型に変換する
    reserve_tb['reserve_datetime'] = pd.to_datetime(reserve_tb['reserve_datetime'])

    # checkin_dateとcheckin_timeを合わせて日時型に変換し、checkin_dateを日付型に変換
    reserve_tb['checkin_datetime']  = pd.to_datetime(reserve_tb['checkin_date'] + reserve_tb['checkin_time'], format='%Y-%m-%d%H:%M:%S')

    # checkin_dateを日付型に変換
    reserve_tb['checkin_date'] = pd.to_datetime(reserve_tb['checkin_date'], format='%Y-%m-%d')

    reserve_tb.info()
    print(reserve_tb)


if __name__ == '__main__':
    main()