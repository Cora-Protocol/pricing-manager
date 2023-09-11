from pycoingecko import CoinGeckoAPI
from datetime import datetime, timezone
import pandas as pd
import os


class HistoricDownloader:
    def __init__(self):
        self.api_base_url = "https://api.coingecko.com/api/v3/"
        self.session = CoinGeckoAPI(api_base_url=self.api_base_url)

    def get_token_ids(self):
        token_ids = []
        token_id_list_dicts = self.session.get_coins_list()
        for token_id_dict in token_id_list_dicts:
            token_ids.append(token_id_dict['id'])
        return token_ids

    def download_history_file(self, path, coin_id, number_of_days):
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
            print(path, "folder does not exist, created.")

        history = self.session.get_coin_market_chart_by_id(
            id=coin_id, vs_currency='usd', days=number_of_days)

        history_dates, history_prices = list(map(list,
                                                 zip(*[[datetime.fromtimestamp(
                                                     float(entry[0] / 1000.0),
                                                     tz=timezone.utc), entry[1]]
                                                     for entry in history['prices']])))

        df = pd.DataFrame(
            data={'Master calendar': history_dates, coin_id: history_prices})
        df['Master calendar'] = df['Master calendar'].apply(
            lambda a: pd.to_datetime(a).date().strftime('%d/%m/%Y'))
        df[['Master calendar', coin_id]].to_csv(
            f"{path}/{coin_id}.csv", sep=',', index=False)
