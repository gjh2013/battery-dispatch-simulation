# Battery Dispatch Simulation

This project implements a simple battery‑dispatch simulation using two market price data
sets. It uses a greedy buy/sell strategy that charges, discharges or holds when the price
is below, above or between two hard‑coded thresholds. The battery model enforces capacity
and charge/discharge limits, and market data is read row‑by‑row from Excel. At each step
the strategy selects CHARGE, DISCHARGE or HOLD, and the battery updates its state and
financial balance accordingly. The demo runs the simulation once using the provided data
and prints the final charge level and balance.

## To run the demo simulation, use the following command:

The market data excel sheet is expected to be in the path `data/market_data.xlsx` relative
to the project directory.
```
uv sync
uv run python -m battery_dispatch
```

### Example output
```
Final Battery Charge: 0.00 MW, Final Balance: £61900.34
```

## To run the unit tests use the following command:
```
uv run pytest -v      
```

## To run the linting checks use the following command:
```
 uv run ruff check
```
