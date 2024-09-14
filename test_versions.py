from frankfurter import FrankfurterEngine

def test_get_currencies():
    engine = FrankfurterEngine()
    engine.fetch_currencies()


def test_get_latest_data():
    engine = FrankfurterEngine()
    engine.fetch_latest_data(base="USD",to="INR")
