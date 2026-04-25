from battery_dispatch.battery import Battery, BatteryConfig
from battery_dispatch.market_data import MarketData
from battery_dispatch.strategy import GreedyBatteryStrategy


def simulate() -> Battery:
    """Run a simple greedy battery simulation over two markets."""
    stratagy = GreedyBatteryStrategy()

    battery_config = BatteryConfig(4, 2, 2, 2)
    battery = Battery(battery_config)

    market1 = MarketData("data/market_data.xlsx", 0, 1)
    market2 = MarketData("data/market_data.xlsx", 1, 2)

    market1_data = market1.get_next_row()
    market2_data = market2.get_next_row()

    while market1_data is not None or market2_data is not None:
        operation = stratagy.decide_battery_action([market1_data, market2_data])
        battery.update_battery(operation)

        if (operation.operation != "HOLD" and operation.market_price is not None and operation.market_price.period > 1):
            # selected market requires a double time period at minimum, so skip the next period
            market1_data = market1.get_next_row()
            market2_data = market2.get_next_row()

        # get the next row
        market1_data = market1.get_next_row()
        market2_data = market2.get_next_row()

    return battery
