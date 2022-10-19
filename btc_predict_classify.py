import csv
import time
import calendar

# Class Investment:
# Instance variables
#	start date
#	end date
#	data
#Functions
#	highest_price(data, start_date, end_date) -> float
#	lowest_price(data, start_date, end_date) -> float
#	max_volume(data, start_date, end_date) -> float
#	best_avg_price(data, start_date, end_date) -> float
#	moving_average(data, start_date, end_date) -> float
class Investment:

    def __init__(self, data, start_date, end_date):
        self.data = data
        self.start_date = start_date
        self.end_date = end_date

        self.start_date_timestamp = calendar.timegm(time.strptime(self.start_date, "%d/%m/%Y"))
        self.end_date_timestamp = calendar.timegm(time.strptime(self.end_date, "%d/%m/%Y"))

    def highest_price(self,data=None, start_date=None, end_date=None):
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        start_date_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        end_date_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))

        current_highest = 0.0
        for row in data:
            if int(row['time']) >= start_date_timestamp and int(row['time']) <= end_date_timestamp:
                if float(row['high']) > current_highest:
                    current_highest = float(row['high'])
        return current_highest

    # lowest_price(data, start_date, end_date) -> float
    # data: the data from a csv file
    # start_date: string in "dd/mm/yyyy" format
    # start_date: string in "dd/mm/yyyy" format
    def lowest_price(self,data=None, start_date=None, end_date=None):
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        start_date_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        end_date_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))

        current_lowest = float("inf")
        for row in data:
            if int(row['time']) >= start_date_timestamp and int(row['time']) <= end_date_timestamp:
                if float(row['low']) < current_lowest:
                    current_lowest = float(row['low'])
        return current_lowest

    # max_volume(data, start_date, end_date) -> float
    # data: the data from a csv file
    # start_date: string in "dd/mm/yyyy" format
    # start_date: string in "dd/mm/yyyy" format
    def max_volume(self,data=None, start_date=None, end_date=None):
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        start_date_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        end_date_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))

        current_max = 0.0
        for row in data:
            if int(row['time']) >= start_date_timestamp and int(row['time']) <= end_date_timestamp:
                if float(row['volumefrom']) > current_max:
                    current_max = float(row['volumefrom'])
        return current_max

    # avg_price(row) -> float
    # row: an item from the data from the csv file
    def avg_price(self,row):
        return float(row['volumeto']) / float(row['volumefrom'])

    # best_avg_price(data, start_date, end_date) -> float
    # data: the data from a csv file
    # start_date: string in "dd/mm/yyyy" format
    # start_date: string in "dd/mm/yyyy" format
    def best_avg_price(self,data=None, start_date=None, end_date=None):
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        start_date_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        end_date_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))

        current_best_avg = 0.0
        for row in data:
            if int(row['time']) >= start_date_timestamp and int(row['time']) <= end_date_timestamp:
                avg_price = avg_value(row)
                if avg_price > current_best_avg:
                    current_best_avg = avg_price
        return round(current_best_avg,2)

    # moving_average(data, start_date, end_date) -> float
    # data: the data from a csv file
    # start_date: string in "dd/mm/yyyy" format
    # start_date: string in "dd/mm/yyyy" format
    def moving_average(self,data=None, start_date=None, end_date=None):
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        start_date_timestamp = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        end_date_timestamp = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))

        avg_values = []
        for row in data:
            if int(row['time']) >= start_date_timestamp and int(row['time']) <= end_date_timestamp:
                avg_values.append(avg_value(row))
        return round(mean(avg_values),2)

# mean(data) -> list
# data: list of lists of numerical values
def mean(data):
    return [sum([row[i] for row in data])/len(data) for i in range(len(data[0]))]

# gradient(data) -> float
# data: list of pairs (lists) of numerical values
def gradient(data):
    mean_vector = mean(data)
    x_mean, y_mean = mean_vector[0],mean_vector[1]
    change_in_y = sum([(int(row[0]) - x_mean) * (row[1] - y_mean) for row in data])
    change_in_x = sum([(int(row[0]) - x_mean)**2 for row in data])
    return change_in_y / change_in_x

# predict_linear_regression(data) -> float
# data: list of pairs (lists) of numerical values
# x_value: new instance of independent variable to predict dependent variable from
def predict_linear_regression(data, x_value):
    m = gradient(data)
    mean_vector = mean(data)
    x_mean, y_mean = mean_vector[0],mean_vector[1]
    y_intercept = y_mean - m*x_mean
    return m*x_value + y_intercept

# predict_next_average(investment) -> float
# investment: Investment type
def	predict_next_average(investment):

    #determine the indices for the slice of the data to be used for the moving average value,
    #as determined by start and end date arguments
    for i in range(len(investment.data)):
        if int(investment.data[i]['time']) >= investment.start_date_timestamp:
            start_index = i
            break
    end_index = -1
    for i in range(start_index,len(investment.data)):
        if int(investment.data[i]['time']) > investment.end_date_timestamp:
            end_index = i
            break
    data_slice = investment.data[start_index:end_index]

    data = [(int(row['time']), investment.avg_price(row)) for row in data_slice]

    return predict_linear_regression(data, data[-1][0]+86400)

# classify_trend(investment) -> str
# investment: Investment type
def classify_trend(investment):
    for i in range(len(investment.data)):
        if int(investment.data[i]['time']) >= investment.start_date_timestamp:
            start_index = i
            break
    end_index = -1
    for i in range(start_index,len(investment.data)):
        if int(investment.data[i]['time']) > investment.end_date_timestamp:
            end_index = i
            break
    data_slice = data[start_index:end_index]

    high_values = [(int(row['time']), float(row['high'])) for row in data_slice]
    low_values = [(int(row['time']), float(row['low'])) for row in data_slice]

    if gradient(high_values) > 0:
        return "increasing" if gradient(low_values) > 0 else "volatile"
    elif gradient(low_values) < 0 and gradient(low_values) < 0:
        return "decreasing"
    return "other"

# Example
if __name__ == "__main__":
    # Start the program
    data = []
    with open("cryptocompare_btc.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
    f.close()

    i1 = Investment(data,'04/05/2015','27/05/2015')
    i2 = Investment(data,'01/02/2016','28/02/2016')
    i3 = Investment(data,'08/12/2016','11/12/2016')
    print(predict_next_average(i1))
    print(classify_trend(i1))
    print(predict_next_average(i2))
    print(classify_trend(i2))
    print(predict_next_average(i3))
    print(classify_trend(i3))
