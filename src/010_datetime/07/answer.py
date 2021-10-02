from pandas._libs.tslibs.timestamps import Timestamp
from preprocess.load_data.data_loader import load_holiday_mst, load_hotel_reserve
import pandas as pd


def main():
    """checkin_dateに対して、休日、休前日フラグを付与
    """
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    holiday_mst = load_holiday_mst()
    print(holiday_mst)
    reserve_tb_with_holiday = pd.merge(reserve_tb, holiday_mst, left_on='checkin_date', right_on='target_day')
    print(reserve_tb_with_holiday)


if __name__ == '__main__':
    main()