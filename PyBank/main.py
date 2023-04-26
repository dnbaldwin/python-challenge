import os
import csv
from pathlib import Path

# Get path and resolve data file location

# base_path = Path(__file__).parent
base_path = Path(__file__)

input_path = (base_path / "../Resources/budget_data.csv").resolve()
output_path = (base_path / "../Analysis/analysis.txt").resolve()

# open the data table

""" with open(file_path, 'r') as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines)) """

# Set variables

datasetLength = 0
netTotal = 0
changeProfitLoss = 0
avgChangeProfitLoss = 0
maxProfitValue = 0
maxLossValue = 0

currentMonth = ""
currentValue = 0
profits = []
losses = []

# open resource file

with open(input_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # print the header and exclude it from analysis

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        datasetLength += 1

        currentMonth = row[0]
        currentValue = float(row[1])

        netTotal = netTotal + currentValue

        # check if current value is a profit

        if currentValue > 0:
            currentProfitValue = currentValue
            profits.append(currentValue)

            # if its a profit, add it to a list of profits for later and check if
            # its a max. if it is record it and the month it occurred

            if currentProfitValue > maxProfitValue:
                maxProfitValue = currentProfitValue
                maxProfitMonth = currentMonth

        # check if current value is a loss

        if currentValue < 0:
            currentLossValue = currentValue
            # losses.append([currentMonth, currentValue])
            losses.append(currentValue)

        # note that a maximum loss is actually a numerical minimum

            if currentLossValue < maxLossValue:
                maxLossValue = currentLossValue
                maxLossMonth = currentMonth

    # format results

    netTotal = "${:,.0f}".format(netTotal)
    maxProfitValue = "${:,.0f}".format(maxProfitValue)
    maxLossValue = "${:,.0f}".format(maxLossValue)

    # print output data to screen

    print("length of dataset: ", datasetLength)
    print("netTotal: ", netTotal)
    print("maxProfitValue: ", maxProfitValue, "   Month: ", maxProfitMonth)
    print("maxLossValue: ", maxLossValue, "   Month: ", maxLossMonth)
    print("max profit val: ", max(profits))
    print("max loss val: ", min(losses))

    # Calculate averages

    avgLoss = sum(losses) / len(losses)
    avgProfit = sum(profits) / len(profits)
    avgChange = avgProfit - avgLoss

    # format averages

    avgLoss = "${:,.0f}".format(avgLoss)
    avgProfit = "${:,.0f}".format(avgProfit)
    avgChange = "${:,.0f}".format(avgChange)
    print("avgLoss: ", avgLoss)
    print("avgProfit: ", avgProfit)
    print("avgChange: ", avgChange)

# Write data to file

with open(output_path, 'w') as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("---------------------------\n")
    outfile.write("")
    outfile.write("\n")
    outfile.write(f"Total Months:  {datasetLength}\n")
    outfile.write("\n")
    outfile.write(f"Total:  {netTotal}\n")
    outfile.write("\n")
    outfile.write(f"Average Change:  {avgChange}\n")
    outfile.write("\n")
    outfile.write(f"Greatest Increase in Profits:  {maxProfitValue}\n")
    outfile.write("\n")
    outfile.write(f"Greatest Decrease in Profits:  {maxLossValue}\n")
    outfile.write("\n")
