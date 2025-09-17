import csv
import numpy as np

# extract the "close" column as a numpy array
closes = [] #store in the list
dates = [] #store the date value
with open('gold_price_data.csv',"r", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            closes.append(float(row["close"]))
            dates.append(row["date"])
print(closes)

closes_arr = np.array(closes)
print(closes_arr)

#2️⃣Basic Statistics

#mean closing price
close_mean = np.mean(closes_arr)
print("close price mean:",close_mean)

#median closing price
close_median =np.median(closes_arr)
print("close price median:",close_median)

#standard deviation
close_std = np.std(closes_arr)
print("close price std:",close_std)

#maximum closing price
close_max = np.max(closes_arr)
print("close price max:",close_max)

#minimum closing price
close_min = np.min(closes_arr)
print("close price min:",close_min)

#Calculate the range of gold closing prices  (max – min).
close_price_range = close_max - close_min
print("close price range:",close_price_range)

# Find the day(s) where the closing price equalled the maximum.
dates_arr = np.array(dates) #np the dates column data

#np.where to find the match condition
max_close_price_date = dates_arr[np.where(closes_arr == close_max)]

print("Max close price date:",max_close_price_date)


#3️⃣Slicing & Reshaping

#get the first 30 days
first_30days = dates_arr[:30] #[start:end]
print("first 30days:",first_30days)
print("",np.size(first_30days))

#get the last 30 days
last_30days = dates_arr[-30:]
print("last 30days:",last_30days)

#reshape into chunks of 30 (approx months)

#finding the sizes of the data, how many days stored in the csv file
# print("number of dates stored: ",np.size(dates_arr))
print("length of months:", len(dates_arr))

usable_length =((len(dates_arr)//30)*30)

monthly_chunks =  closes_arr[:usable_length].reshape(-1,30)
print("Shape:", monthly_chunks.shape)
# print("1s month:" ,monthly_chunks[0])
# print("2nd month:" ,monthly_chunks[1])

#Find the average price per month using np.mean(reshaped, axis=1).

monthly_mean = np.mean(monthly_chunks,axis=1)
print("1st month mean:",monthly_mean[0])
print("last month mean:",monthly_mean[-1])

#Compare the first month’s average to the last month’s.
diff= monthly_mean[0] - monthly_mean[-1] # find out the difference
#compare
if diff < 0:
    print(f"the mean price rise: {abs(diff):.2f}")
elif diff > 0:
    print(f"the mean price fall: {diff:.2f}")
else:
    print("the mean price didn't change")

