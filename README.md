# btc_predict_classify
Contains two methods, one for predicting the average price of an asset (eg. Bitcoin) on a given day, and one for classifying the trend of a price (increasing or decreasing)

# Class Investment
This class is the data type used for performing analysis and requires three arguments:
  - data: list of dictionaries. Each dictionary contains the fields shown in the file cryptocompare_btc.csv and corresponds to one day of trading.
  - start_date: the start date of the slice of the data where the analysis should be applied, in the form "DD/MM/YYYY"
  - end_date: the end date of the slice, in the same format
  
# Example loaded from cryptocompare_btc.csv:
with open("cryptocompare_btc.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
    f.close()

inv = Investment(data,'04/05/2015','27/05/2015')

# predict_next_average(investment) -> float
This method provides a prediction for the price of the asset on the next day after the end of the time slice in an Investment object, by fitting a linear regression model on its data
# Example:
print(predict_next_average(inv))

# classify_trend(investment) -> str
This method classifies whether the price of an asset is increasing or decreasing. The logic is as follows: if the gradient of the high values for the time period is strictly positive, then the trend is "positive" if the gradient of the low values is also strictly positive, otherwise it is "volatile". If the gradient of the high and low values are both strictly negative, the trend is "decreasing". If none of these cases apply, the trend is "other".
# Example:
print(classify_trend(i1))
