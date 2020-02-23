import pandas as pd
import os

file=r"\python-challenge\PyBank\Resources\budget_data.csv" #couldn't get relative paths to run appropriately in shell terminal (probably an issue with my virtual environment setup) so I had to use an absolute file path. sorry! :(
csv_path = os.getcwd()+file
accounting = pd.read_csv(csv_path)

accounting.head()
accounting.columns

monthcount = accounting['Date'].count()
returnstatementmonths = "There are {} total months in this dataset.".format(monthcount)

netpl = accounting['Profit/Losses'].sum()
returnstatementnetpl = "The total amount of Profit/Losses over the entire period is: ${}".format(netpl)

accounting['Shifted Profit/Losses'] = accounting['Profit/Losses'].shift(1)
accounting['Monthly Difference'] = accounting['Profit/Losses'] - accounting['Shifted Profit/Losses']

difference = round(accounting['Monthly Difference'].mean(),2) #didn't set the difference to an absolute value in order to accurately
                                                     #represent a negative or positive change from previous months.
returnstatementdiff = 'The average change in Profit/Losses over the entire period is: ${}'.format(difference)

max = round(accounting['Monthly Difference'].max(), 2)
returnstatementmax = 'The Greatest Increase in Profits was: (${})'.format(max)

min = round(accounting['Monthly Difference'].min(),2)
returnstatementmin = 'The Greatest Decrease in Profits was: (${})'.format(min)

print('Financial Analysis')
print('-----------------------------------------')
print(returnstatementmonths)
print(returnstatementnetpl)
print(returnstatementdiff)
print(returnstatementmax)
print(returnstatementmin)

results = {
    'Financial Analysis': [returnstatementmonths, 
                            returnstatementnetpl, 
                            returnstatementdiff, 
                            returnstatementmax, 
                            returnstatementmin]
}


results_df = pd.DataFrame(data=results)
results_df.to_csv(r'python-challenge/PyBank/Results.txt', sep=',', index=False)