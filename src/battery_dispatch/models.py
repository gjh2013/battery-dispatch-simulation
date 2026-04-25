import datetime
from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class BatteryConfig:
    capacity: float
    max_charge_rate: float
    max_discharge_rate: float
    initial_charge: float


@dataclass(frozen=True)
class MarketPrice:
    timestamp: datetime
    price: float
    period: int


@dataclass(frozen=True)
class StrategyOperation:
    operation: Literal["CHARGE", "DISCHARGE", "HOLD"]
    market_price: MarketPrice | None
