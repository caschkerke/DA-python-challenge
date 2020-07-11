import pandas as pd
import os


file=r"\PyBank\Resources\budget_data.csv"
txt_output=r"\PyBank\Results.txt"
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

difference = round(accounting['Monthly Difference'].mean(),2) 

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
results_df.to_csv(os.getcwd()+txt_output, sep=',', index=False)