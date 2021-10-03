from pandas._libs.tslibs.timestamps import Timestamp
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd


def main():
    """n件前のデータ取得
    予約テーブルの全ての行に、同じ顧客の2回前の予約金額の情報を付与する
    2回前の予約がない場合は値なしとする
    """
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    print(reserve_tb)

    # customerごとにreserve_datetimeで並び替え
    # groupbyで集約したものに対して、apply関数を使ってソートする
    result = reserve_tb.groupby('customer_id')   \
        .apply(lambda group: group.sort_values(by='reserve_datetime', axis=0, inplace=False))

    # customerごとに2件前のtotal_priceを保存
    result['before_price'] = \
        pd.Series(result['total_price'].groupby('customer_id').shift(periods=2))
    print(result)


if __name__ == '__main__':
    main()