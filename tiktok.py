from TikTokApi import TikTokApi as tiktok
import json
from helpers import process_results
import pandas as pd
import sys


def get_data(hashtag):
    verifyFp = "verify_kx4xyzny_6QK0j7ib_WKcB_4loU_8wtO_n4H5Y3WreHDk"
    api = tiktok.get_instance(
        custom_verifyFp=verifyFp, use_test_endpoints=True)
    trending = api.by_hashtag(hashtag)
    flattened_data = process_results(trending)
    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('tiktokdata.csv', index=False)


if __name__ == '__main__':
    get_data(sys.argv[1])
