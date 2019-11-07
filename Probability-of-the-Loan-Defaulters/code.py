# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
path
df = pd.read_csv(path)
p_a  = ((df['fico']>700).sum())/(len(df))
print(p_a)
p_b = ((df['purpose'] == 'debt_consolidation').sum())/(len(df))
print(p_b)
df1 = df['purpose'] == 'debt_consolidation'
#print(df)
p_a_b = (p_a * p_b)
print(p_a_b)
result = (p_a*p_b) == (p_a)
print(result)



# code ends here


# --------------
# code starts here
#prob_lp = ((df['paid.back.loan']== 'Yes').sum())/(len(df['paid.back.loan']))
#print(prob_lp)
#prob_cs = ((df['credit.policy'] == 'Yes').sum())/(len(df['credit.policy']))
#print(prob_cs)
#new_df = ((df['paid.back.loan'] == 'Yes').sum())#/(len(df))
#print(new_df)
#prob_pd_cs = prob_cs/new_df
#print(prob_pd_cs)
#bayes = ((prob_pd_cs) * (prob_lp))/(prob_cs)
#print(bayes)
pb = len(df['paid.back.loan'])
print(pb)
y = len(df[df['paid.back.loan'] == 'Yes'])
print(y)
prob_lp = y/pb
print(prob_lp)
cp = len(df['credit.policy'])
print(cp)
cy = len(df[df['credit.policy'] == 'Yes'])
print(cy)
prob_cs = cy/cp
print(prob_cs)
new_df = pd.DataFrame(df[df['paid.back.loan'] == 'Yes'])
print(new_df)
prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0] / new_df.shape[0]
print(prob_pd_cs)
bayes  = (prob_pd_cs * prob_lp)/prob_cs
print(bayes)





# code ends here


# --------------
# code starts here
#df.plot.bar(rot = 0)
#df.plot.bar(y='purpose', rot=0)
#plt.bar(df['purpose'],)
#plt.show()
df1 = df[df['paid.back.loan'] == 'No']
print(df1)
plt.bar(df['purpose'],'df1')
# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
print(inst_median)
inst_mean = df['installment'].mean()
print(inst_mean)
plt.hist(df['installment'])
plt.hist(df['log.annual.inc'])




# code ends here


