# working with CSS

#reading
import csv
rows = []

with open('employees.csv',"r",newline='') as csvfile:
    csvreader =csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)


print(header)
print(rows)

#writing
header =["Name","age"]
data = [["Ales", 25],["Brad", 45],["Cam", 55], ["Kaki",92]]

with open('student_info.csv',"w",newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(data)

# csv.DictReader()

with open('employees.csv',"r",newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["Name"], row["Email"])
    print(rows)

#csv. DictWriter
    header = ["Name","Age"]
    data = [["Ales", 25],["Brad", 45], ["Joey", 18]]

    with open('student_info.csv',"w",newline='') as csvfile:
        writer =csv.DictWriter(csvfile,fieldnames=header)

        writer.writeheader()
        for student in data:
            writer.writerow({"Name": student[0], "Age": student[1]})

#Read the following CSV about Australia states and territories
# Add a new header "Capital" and add the capital city for each state/territory
# Write to the same CSV file
# Extra fun: calculate the total population of Australia

header = ["Capital", "Population"]
data = [["VIC",6649159], ["NSW",8189266],["SA",1773243], ["WA",2681633],["Tasmania",541479], ["Queensland",5221170], ["ACT",432266], ["NT",246338]]
#csv.writer()
# with open('australia_stateInfo.csv',"w",newline='') as csvfile:
#     csvwriter =csv.writer(csvfile)
#     csvwriter.writerow(header)
#     csvwriter.writerows(data)
#Dict read
with open("australia_stateInfo.csv","r",newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["Capital"], row["Population"])

#csv. DictWriter

with open('australia_stateInfo.csv',"w",newline='') as csvfile:
    writer =csv.DictReader(csvfile, fieldnames=header)

    with open("australia_stateInfo.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()  # column names

        for state in data:
            writer.writerow({
                "Capital": state[0],
                "Population": state[1]
            })

#calculate the total population in Australia

def total_population(data):
    total= 0
    for row in data:
        total += row[1]
    return total

print(f"the total population in Australia {total_population(data)}")