from battery_dispatch.battery import Battery
from battery_dispatch.models import BatteryConfig, MarketPrice, StrategyOperation


def test_charge_respects_capacity():
    cfg = BatteryConfig(capacity=4, max_charge_rate=2, max_discharge_rate=2, initial_charge=3)
    battery = Battery(cfg)

    op = StrategyOperation("CHARGE", MarketPrice(timestamp=None, price=50, period=1))
    battery.update_battery(op)

    # Cannot exceed capacity 4
    assert battery.charge == 4
    # Balance should decrease
    assert battery.balance < 0


def test_discharge_respects_minimum_zero():
    cfg = BatteryConfig(capacity=4, max_charge_rate=2, max_discharge_rate=2, initial_charge=1)
    battery = Battery(cfg)

    op = StrategyOperation("DISCHARGE", MarketPrice(timestamp=None, price=70, period=1))
    battery.update_battery(op)

    # Cannot go below zero
    assert battery.charge == 0
    # Balance should increase
    assert battery.balance > 0


def test_hold_operation_does_nothing():
    cfg = BatteryConfig(4, 2, 2, 2)
    battery = Battery(cfg)

    op = StrategyOperation("HOLD", None)
    battery.update_battery(op)

    assert battery.charge == 2
    assert battery.balance == 0
