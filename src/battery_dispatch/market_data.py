import pandas as pd

from battery_dispatch.models import MarketPrice


class MarketData:
    """Stream market rows from an Excel sheet, optionally skipping rows for a market with a timespan of 2 periods."""
    def __init__(self, path: str, sheet_index: int, period: int):
        self._period = period
        self._skip = False
        df = pd.read_excel(path, sheet_name=sheet_index)
        df.columns = [c.strip() for c in df.columns]
        df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0])

        self._df = df
        self._iter = df.iterrows()

    def get_next_row(self) -> MarketPrice:
        """
        Return the next MarketPrice, or None when the data ends or when this
        market uses a double period and the current step is the skipped one.
        """

        if self._period > 1 and self._skip:
            self._skip = False
            return None

        self._skip = self._period > 1

        try:
            _, row = next(self._iter)
        except StopIteration:
            return None

        return MarketPrice(
            timestamp=row.iloc[0],
            price=row.iloc[1],
            period=self._period
        )
