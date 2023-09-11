class Config:
    def __init__(self,
                 asset,
                 number_of_days_for_training_curve,
                 strike_percentage,
                 expiration,
                 training_label):
        self.asset = asset
        self.number_of_days_for_training_curve = number_of_days_for_training_curve
        self.training_label = training_label
        self.strike_percentage = strike_percentage
        self.expiration = expiration
