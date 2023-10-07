from nsepy import get_history
from datetime import date
import config

class NiftyOptionsData:
    def __init__(self):
        pass
    
    def get_option_data(self, option_type, expiry_date, strike_price, start_date, end_date, ):
        nifty_opt = get_history(symbol=config.NIFTY_SYMBOL,
                                start=start_date, end=end_date,
                                index=True,
                                option_type=config.CALL_OPTION,
                                strike_price=strike_price,
                                expiry_date=expiry_date)
        return nifty_opt