# %%
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import random as rd 
import itertools as it 
import sympy as smp
plt.style.use('ggplot')



# %% CREATE SAMPLE BASE SET OF CARD NO'S WITH ONLY 10 DIGITS -> CAUSE FIRST 6 ALL THE SAME
def compute_reciprocals(values):
    output_array = np.empty(values,dtype=int)
    for i in range(values):
        output_array[i] = int(round(rd.random()*10000000000,0))
    return output_array

raw_card_no_set = compute_reciprocals(100000) #compute dataset creation with N rows

# define filtering of card no's != to 10 digits  
lolist = []
for i in range(len(raw_card_no_set)):
    if len(str(raw_card_no_set[i])) != 10:
        lolist.append(i)
# Delete from rawset all card np's != 10 digits 
base_card_set = np.delete(raw_card_no_set, lolist)



# %% Define the combination (altering of permuation where order does matter) to order does not matter combination
# order does matter = [1,2,3] [3,2,1] [2,1,3] etc -> in our case the numbers just represent which index we will hide
    # so they all refer to the same in our case 

# combination = list(it.combinations([0,1,2,3,4,5,6,7,8,9],7))
# combination = list(it.combinations([0,1,2,3],2))
# comb_set = combination[3]
# print(comb_set, 'type:', type(comb_set))

# for index in comb_set:
#     print(index)




# %% RUNNING THE CARD NO'S CREATION WITH ARRAY OUTPUT OF NEW NO'S
valueDrawn_comb = list(it.combinations([0,1,2,3,4,5,6,7,8,9],1))
indiv_combSet = valueDrawn_comb[1]
print(indiv_combSet)

def perf_id_creation(value):
    new_id = []
    for index in indiv_combSet:
        new_id.append(str(value)[index])
    end_value = ''.join(new_id)
    return int(end_value)
np_vectorize_object = np.vectorize(perf_id_creation)
result_id_and_combination = np_vectorize_object(base_card_set)


# print(comb_set)
print(base_card_set)
print('Set: ',len(result_id_and_combination))
print('unique: ',len(np.unique(result_id_and_combination)))
print(result_id_and_combination)

# %% FINAL VERSION WITH OUTPUT IN DICTS 
def perf_id_creationX(value):
    new_id = []
    for index in indiv_combSet:
        new_id.append(str(value)[index])
    end_value = ''.join(new_id)
    return int(end_value)


L_N_valueToDraw = [9,8,7,6,5]
# L_N_valueToDraw = [1,2]
D_valueDrawnOptions ={}
for val_drawn in L_N_valueToDraw: # each drawing combination
    valueDrawn_comb = list(it.combinations([0,1,2,3,4,5,6,7,8,9],val_drawn))
    # valueDrawn_comb = list(it.combinations([0,1,2,3],val_drawn))
    hidden_str = 10-val_drawn
    # D_valueDrawn[f'{val_drawn}Val-{hidden_str}Hid({len(valueDrawn_comb)})']
    print(f'{val_drawn}Val-{hidden_str}Hid({len(valueDrawn_comb)})')
    D_withinDrawncombos ={}
    for comb in range(len(valueDrawn_comb)): # each possibility within drawing 
        indiv_combSet = valueDrawn_comb[comb]
        np_vectorize_object = np.vectorize(perf_id_creationX)
        out_newCrdNos = np_vectorize_object(base_card_set)
        print(indiv_combSet,' old:',len(out_newCrdNos) ,'new:',len(np.unique(out_newCrdNos)))
        D_withinDrawncombos[indiv_combSet] = (len(out_newCrdNos)-len(np.unique(out_newCrdNos)))
    D_valueDrawnOptions[f'{val_drawn}Val-{hidden_str}Hid({len(valueDrawn_comb)})'] = D_withinDrawncombos



# combination = list(it.combinations([0,1,2,3,4,5,6,7,8,9],7))

# %%
# ['9Val-1Hid(10)', '8Val-2Hid(45)', '7Val-3Hid(120)', '6Val-4Hid(210)', '5Val-5Hid(252)']
# D_valueDrawnOptions.keys()
# pd.DataFrame.from_dict(D_valueDrawnOptions['5Val-5Hid(252)'], orient='tight')
test_drawSet = D_valueDrawnOptions['7Val-3Hid(120)']

# %%
for keyX, valueX in D_valueDrawnOptions.items():
    test_drawSet = D_valueDrawnOptions[keyX]
    index_comb = []
    duplicate_values = []

    
    for key, value in test_drawSet.items():
        index_comb.append(key)
        duplicate_values.append(value)

    df_set = pd.DataFrame(list(zip(index_comb, duplicate_values)),columns =['index_combinations', 'n_duplicates'])
    df_set = df_set.sort_values(by=['n_duplicates'])
    # df_set.to_excel(f"{keyX} output.xlsx")  
    plt.gcf().set_size_inches(15,38, forward=True)
    plt.barh(df_set['index_combinations'].astype(str),df_set['n_duplicates'])
    plt.title(keyX)
    plt.tight_layout
    plt.show()
