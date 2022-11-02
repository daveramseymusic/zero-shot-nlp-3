# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_zero_shot_linkedin_test.ipynb.

# %% auto 0
__all__ = ['analyze_one']

# %% ../nbs/01_zero_shot_linkedin_test.ipynb 18
def analyze_one(df:pd.DataFrame, # dataframe with df.input
                candidate_labels, index ):
    i=index
    sequence = df.input[i]
    answer = classifier(sequence, candidate_labels)
    dfo = pd.DataFrame(answer)
    dfo.sort_values('scores',inplace=True)
    fig = px.bar(dfo, x="scores", y="labels", orientation='h')
    print(dfo.sequence[0])
    
    print('Actual Category: '+str(df.category[i]))
    fig.show()
