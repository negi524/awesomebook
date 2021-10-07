from pandas._config.config import reset_option
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

def main():
    """全結合処理
    顧客ごとに2017年1月〜2017年3月の月間合計利用金額を計算
    利用がない日は0とする
    日付はチェックイン日付を利用する
    """
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    print(reserve_tb)
    print(customer_tb)

    # 日付マスタを生成
    month_mst = pd.DataFrame({'year_month': [(date(2017, 1, 1) + relativedelta(months=x)).strftime("%Y%m") for x in range(0, 3)]})
    # month_mst['year_month'] = pd.to_datetime(month_mst['year_month'])

    # cross_joinのためにすべて同じ値の結合キーを準備
    customer_tb['join_key'] = 0
    month_mst['join_key'] = 0

    # 顧客テーブルと月テーブルを全結合する
    customer_mst = pd.merge(customer_tb[['customer_id', 'join_key']], month_mst, on='join_key')
    customer_mst.info()

    # 年月の結合キーを予約テーブルで準備
    reserve_tb['year_month'] = reserve_tb['checkin_date']   \
        .apply(lambda x: pd.to_datetime(x).strftime("%Y%m"))
    reserve_tb.info()

    # 予約レコードと結合し、合計予約金額を計算
    # TODO: yearで結合できていない(月単位で結合されてしまっている)
    summary_result = pd.merge(
        customer_mst,
        reserve_tb[['customer_id', 'year_month', 'total_price']],
        on=['customer_id', 'year_month'],
        how='left'
    ).groupby(['customer_id', 'year_month'])['total_price'].sum().reset_index()

    # 予約レコードがなかった場合の合計金額を値なしから0に変換
    summary_result.fillna(0, inplace=True)
    print(summary_result.query('customer_id == "c_1"'))
    print(reserve_tb.query('customer_id == "c_1"'))


if __name__ == '__main__':
    main()
