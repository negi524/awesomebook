from pandas._libs.tslibs.timestamps import Timestamp
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd


def main():
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    reserve_tb['reserve_datetime'] = pd.to_datetime(reserve_tb['reserve_datetime'])

    # reserve_datetimeを季節分割する
    reserve_tb['reserve_season'] = reserve_tb['reserve_datetime'].dt.month.apply(to_season)
    print(reserve_tb[['reserve_datetime', 'reserve_season']])


def to_season(target: int) -> str:
    """日時型を季節の文字列に変換する
    """
    if (3 <= target <= 5):
        return 'spring'
    elif (6 <= target <= 8):
        return 'summer'
    elif (9 <= target <= 11):
        return 'autumn'
    else:
        return 'winter'


if __name__ == '__main__':
    main()
