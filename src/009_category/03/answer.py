import pandas as pd
import numpy as np
from preprocess.load_data.data_loader import load_hotel_reserve


def main():
    customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
    print(customer_tb)


if __name__ == '__main__':
    main()