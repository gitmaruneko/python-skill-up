import csv
import statistics

# Calculate statistics such as mean, median, mode on this data

with open("tips.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    data = [float(row["total_bill"]) for row in reader]

results = {
    "mean": statistics.mean(data),
    "median": statistics.median(data),
    "mode": statistics.mode(data),
}

with open("statistics.csv", "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["metric", "value"])
    writer.writerows(results.items())

for metric, value in results.items():
    print(f"{metric.title()}: {value}")
