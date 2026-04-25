from battery_dispatch.market_data import MarketPrice
from battery_dispatch.models import StrategyOperation


class GreedyBatteryStrategy:
    """ Simple strategy that buys when the price is below the buy price and sells when above the sell price"""
    def __init__(self):
        # Buy below this price
        self._buy_price = 55

        # Sell above this price
        self._sell_price = 65

    def decide_battery_action(self, market_price_data: list[MarketPrice]) -> StrategyOperation:
        """ Return CHARGE, DISCHARGE or HOLD based on min/max prices. """
        valid_market_data = [p for p in market_price_data if p is not None and p.price is not None]

        if len(valid_market_data) == 0:
            return  StrategyOperation("HOLD", None)

        max_market_price = max(valid_market_data, key=lambda p: p.price)
        min_market_price = min(valid_market_data, key=lambda p: p.price)

        if min_market_price.price < self._buy_price:
            return StrategyOperation("CHARGE", min_market_price)
        elif max_market_price.price > self._sell_price:
            return StrategyOperation("DISCHARGE", max_market_price)
        else:
            return StrategyOperation("HOLD", None)
