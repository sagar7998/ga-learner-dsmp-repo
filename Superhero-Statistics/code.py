# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data = pd.read_csv(path)

data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot.bar(rot=0)
print(gender_count)
#print(data)


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
print(alignment)
alignment.plot.pie()
plt.title("Character Alignment")


# --------------
#Code starts here
import numpy as np
sc_df = data[['Strength','Combat']]
sc_covariance = sc_df.Strength.cov(sc_df.Combat)
#sc_covariance = np.cov(sc_df['Strength'],sc_df['Combat'])
print(sc_covariance)
sc_strength = sc_df.Strength.std(axis=0, skipna=True)
sc_combat = sc_df.Combat.std(axis=0, skipna=True)
#print(sc_combat)
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print(sc_pearson.round(2))
ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.Intelligence.cov(ic_df.Combat)
#ic_covariance = np.cov(ic_df['Intelligence'],ic_df['Combat'])
ic_intelligence = ic_df.Intelligence.std(axis=0,skipna=True)
ic_combat = ic_df.Combat.std(axis=0, skipna=True)
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)



# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)
#print(total_high)
super_best = data[data['Total'] > total_high]
print(super_best)
super_best_names = super_best['Name'].values.tolist()
print(super_best_names)


# --------------
#Code starts here
ax_1 = data['Intelligence']
ax_2 = data['Speed']
ax_3 = data['Power']
data.boxplot(column = ['Intelligence','Speed','Power'])
plt.show()


