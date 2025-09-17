import csv
import numpy as np

# extract the "close" column as a numpy array
closes = []
#extract the date value #extract dates column
dates = []
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
print("1s month:" ,monthly_chunks[0])
print("2nd month:" ,monthly_chunks[1])

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


#4️⃣ Price Differences
#- daily changes
daily_change = np.diff(closes_arr)
print("day change:",daily_change)
print(len(daily_change))

# biggest increase & decrease
biggest_increase = np.max(daily_change)
print("biggest_increase change:",biggest_increase)

#biggest_decrease
biggest_decrease =np.min(daily_change)
print("biggest_decrease change:",biggest_decrease)

# Which day had the largest increase?
#largest_increase_date = dates_arr[np.where(day_change == biggest_increase)]
largest_increase_date = dates_arr[np.argmax(daily_change) + 1]
print("The largest increase date:",largest_increase_date)

#largest_decrease_date
largest_decrease_date = dates_arr[np.argmin(daily_change) + 1]
print("The largest decrease date:",largest_decrease_date)

#5️⃣ Simple Trend Visualization
#- simple text-based chart
# for price in closes_arr:
#     print(f"{price:6.2f} | " + "*" * int(price/2))

# - Modify the visualization to highlight days above the average price.
# for price in closes_arr:
#     maker_v = "[^,^]" if price > close_mean else "[>,<]"
#     print(f"{price:6.2f} | " + maker_v * (int(price) // 10))

# - Try plotting the last 30 days instead.
last_30days = closes_arr[-30:]
avg_30 = last_30days.mean()

print(f"30-day average: {avg_30:.2f}")

for price in last_30days:
    marker = "$" if price > avg_30 else "."
    print(f"{price:6.2f} | " + marker * (int(price)//10))
