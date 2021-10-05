from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

def main():
    """過去n件の合計値
    予約テーブルの全ての行に、自身の行から2件前までの3回の合計予約金額の情報を付与
    過去の予約が3回未満の場合は値なし
    """
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

    # customer_idごとにグループ化
    result = reserve_tb.groupby('customer_id')   \
        .apply(lambda x: x.sort_values(by='reserve_datetime', ascending=True))  \
            .reset_index(drop=True)
    
    # 新たな列としてprice_avgを追加
    # customer_idごとにtotal_priceのwindow3件にまとめ、その平均値を計算する
    # min_period=1を設定し、1件以上あった場合には計算するように設定
    result['price_avg'] = pd.Series(
        result.groupby('customer_id')['total_price']
        .rolling(center=False, window=3, min_periods=1).mean()
        .reset_index(drop=True)
    )
    # customer_idごとにprice_avgを1行下にずらす
    result['price_avg'] = result.groupby('customer_id')['price_avg'].shift(periods=1)
    print(result)

if __name__ == '__main__':
    main()
