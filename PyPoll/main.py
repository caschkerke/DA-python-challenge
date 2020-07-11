import pandas as pd
import os

def results():

    file=r"\PyPoll\Resources\election_data.csv"
    txt_output=r"\PyPoll\Results.txt"
    csv_path = os.getcwd()+file
    votes = pd.read_csv(csv_path)

    votes['Vote Count'] = ""
    temp_df = pd.DataFrame(columns=['Election Results'])
 
    cand_count = votes.groupby('Candidate')['Vote Count'].count()
    cand_df = pd.DataFrame(cand_count)

    total_votes = cand_df['Vote Count'].sum()
    cand_df['Vote Pct'] = (cand_df['Vote Count'] / total_votes *100).map('{:,.2f}%'.format)
    cand_df = cand_df.sort_values(by=['Vote Count'], ascending=False)
    cand_df = cand_df.reset_index()

    winner = cand_df['Candidate'].iloc[0]

    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {total_votes}')
    print('--------------------------------')
    for i, j in cand_df.iterrows():

        candidate = cand_df['Candidate'].values[i]
        votes_f = cand_df['Vote Count'].values[i]
        votes_pct = cand_df['Vote Pct'].values[i]

        print(f'{candidate}: {votes_pct} ({votes_f})')
        new_row = {'Election Results': (f'{candidate}: {votes_pct} ({votes_f})')}
        temp_df = temp_df.append(new_row, ignore_index=True)
    print('--------------------------------')
    print(f'Winner: {winner}')
    new_row2 = {'Election Results': (f'Winner: {winner}')}
    temp_df = temp_df.append(new_row2, ignore_index=True)
    print('--------------------------------')

    results_df = temp_df
    results_df.to_csv(os.getcwd()+txt_output, index=False)

    return

results()