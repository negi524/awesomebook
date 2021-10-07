from pandas._config.config import reset_option
from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from preprocess.load_data.data_loader import load_production

def main():
    """交差検証
    製造レコードのデータを用いて、予測モデル構築のためのデータ分割を行う
    データの20%をホールドアウト検証ようのテストデータとして確保
    残りのデータで交差数4の交差検証を行う
    """
    production_tb = load_production()
    production_tb.info()
    train_data, test_data, train_target, test_target = \
        train_test_split(production_tb.drop('fault_flg', axis=1), production_tb['fault_flg'], test_size=0.2)
    train_data.info()
    test_data.info()
    print(train_target.shape)
    print(test_target.shape)


if __name__ == '__main__':
    main()
