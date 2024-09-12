# frankfurter - Unofficial Lightweight Wrapper for the frankfurter API


[![Downloads](https://static.pepy.tech/badge/frankfurter)](https://pepy.tech/project/frankfurter)
[![PyPI](https://badge.fury.io/py/frankfurter.svg)](https://pypi.org/project/frankfurter/)


The Frankfurter API tracks foreign exchange references rates published by the [European Central Bank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html). The data refreshes around 16:00 CET every working day.


# Installation 

You can directly download it from pip using the command 

```
pip install frankfurter
```

# Usage

First, you need to make a object of the ```FrankfurterEngine``` class. It takes an argument called ```quiet_mode``` which decides whether to print the logging information. 

```
from frankfurter import FrankfurterEngine

engine = FrankfurterEngine(quiet_mode=False)
```

## Get List of Supported Currencies

To fetch the list of supported currencies:

```
currencies = engine.fetch_currencies()
print(currencies)
```

## Fetch Latest Forex Data

To fetch the latest forex data for a base currency and an optional target currency:

```
latest_data = engine.fetch_latest_data(base="USD", to="EUR")
print(latest_data)
```

## Fetch Historical Data for a Specific Date

To fetch forex data for a specific date:

```
historical_data = engine.fetch_data_for_date(date="2022-01-01", base="USD", to="EUR")
print(historical_data)
```

## Fetch Time Series Data

To fetch forex data over a date range:

```
time_series_data = engine.fetch_time_series_data(
    base="USD", to="EUR", start_date="2022-01-01", end_date="2022-12-31"
)
print(time_series_data)
```

# API Documentation

API Documentation
For more information on the API itself, visit the [official documentation](https://www.frankfurter.app/docs/).


