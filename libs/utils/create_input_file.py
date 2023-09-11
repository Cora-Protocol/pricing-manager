import pandas as pd


def create_input_file(price_history_file, path, config):
    df = pd.read_csv(price_history_file)
    asset = df.columns[1]

    # 9\. Select a user custom training label to uniquely identify this Potion from others with the same
    # Asset, Strike, and Expiration but a different training data window. Examples include: 'Full',
    # 'Bull', 'Bear', 'PastYear', etc.
    training_label = config.training_label
    training_start = df.loc[0, 'Master calendar']
    training_end = df.loc[len(df) - 1, 'Master calendar']
    # StrikePercent : float
    # The strike price of the Put option as a multiple of the at-the-money (ATM) price. e.g. 1.0
    # is ATM, 0.9 is 10% out-of-the-money (OTM), and 1.1 is 10% in-the-money (ITM), etc.
    strike_percentage = config.strike_percentage
    expiration = config.expiration

    current_price = df.loc[len(df) - 1, df.columns[1]]

    df_new = pd.DataFrame(data={'Asset': [asset],
                                'TrainingLabel': [training_label],
                                'TrainingStart': [training_start],
                                'TrainingEnd': [training_end],
                                'StrikePct': [strike_percentage],
                                'Expiration': [expiration],
                                'CurrentPrice': [current_price]
                                })
    df_new.to_csv('{}/CurveConfigFor{}.csv'.format(path, config.asset.title()),
                  sep=',', index=False)
