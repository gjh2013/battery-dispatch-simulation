
from battery_dispatch.models import BatteryConfig, StrategyOperation


class Battery:
    """Battery with charge state and financial balance."""
    UNIT_TIME = 0.5  # 30‑minute periods

    def __init__(self, config: BatteryConfig):
        self.cfg = config
        self.charge = config.initial_charge
        self.balance = 0.0

    def _charge_amount(self, hours: float) -> float:
        """Charge the battery for a given number of hours, limited by the maximum capacity"""
        allowed = min(
            self.cfg.max_charge_rate * hours,
            self.cfg.capacity - self.charge
        )
        self.charge += allowed
        return allowed

    def _discharge_amount(self, hours: float) -> float:
        """ Discharge the battery for a given number of hours """
        allowed = min(
            self.cfg.max_discharge_rate * hours,
            self.charge
        )
        self.charge -= allowed
        return allowed

    def update_battery(self, op: StrategyOperation):
        """ Update the battery state doe the given operation: HOLD, CHARGE, DISCHAGE """
        if not op or not op.market_price or op.operation == "HOLD":
            return

        mp = op.market_price
        hours = mp.period * self.UNIT_TIME

        if op.operation == "CHARGE":
            actual = self._charge_amount(hours)
            self.balance -= actual * mp.price
        else:
            actual = self._discharge_amount(hours)
            self.balance += actual * mp.price
