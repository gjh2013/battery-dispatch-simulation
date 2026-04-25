from battery_dispatch.models import MarketPrice
from battery_dispatch.strategy import GreedyBatteryStrategy


def test_strategy_charges_on_low_price():
    strat = GreedyBatteryStrategy()
    low = MarketPrice(timestamp=None, price=4, period=1)
    op = strat.decide_battery_action([low])

    assert op.operation == "CHARGE"

def test_strategy_charges_on_high_price():
    strat = GreedyBatteryStrategy()
    high = MarketPrice(timestamp=None, price=1000, period=1)
    op = strat.decide_battery_action([high])

    assert op.operation == "DISCHARGE"

def test_strategy_holds_on_medium_price():
    strat = GreedyBatteryStrategy()
    mid = MarketPrice(timestamp=None, price=60, period=1)
    op = strat.decide_battery_action([mid])

    assert op.operation == "HOLD"
