from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd


def main():
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    reserve_datetime = pd.to_datetime(reserve_tb['reserve_datetime'])
    reserve_tb['month'] = reserve_datetime.dt.month
    reserve_tb['day_in_month'] = reserve_datetime.dt.day
    reserve_tb['wday'] = reserve_datetime.dt.dayofweek
    reserve_tb['weekdays'] = reserve_datetime.dt.day
    reserve_tb['hour'] = reserve_datetime.dt.hour
    reserve_tb['minute'] = reserve_datetime.dt.minute
    reserve_tb['second'] = reserve_datetime.dt.second
    reserve_tb['format_str'] = reserve_datetime.dt.strftime('%Y-%m-%d %H:%M:%S')
    print(reserve_tb)


if __name__ == '__main__':
    main()