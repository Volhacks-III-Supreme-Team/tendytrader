from .get_finance import get_stock_data
import datetime

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2016, 1, 1)
data = get_stock_data("GOOGL", start, end, 1)
