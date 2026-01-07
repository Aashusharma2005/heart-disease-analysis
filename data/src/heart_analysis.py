import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

heart_disease = pd.read_csv("../data/heart-disease.csv")

plt.style.use('ggplot')
fig,(ax0,ax1) = plt.subplots(nrows=2,ncols=1,figsize =(10,10),sharex=True)

over_50 = heart_disease[heart_disease['age']>50]

scatter =ax0.scatter(x = over_50['age'],
            y = over_50['chol'],
            c = over_50['target'])

ax0.set(title = 'Heart Disease and cholestrol level',
        ylabel = 'cholestrol level')

ax0.legend(*scatter.legend_elements(),title='target')

ax0.axhline(y = over_50['chol'].mean(),linestyle='--')

scatter = ax1.scatter(x = over_50['age'],
                      y = over_50['thalach'],
                      c = over_50['target'])

ax1.set(title = 'Heart disease and Max heart attack Rate',
        xlabel ='age',
        ylabel='thalach')

ax1.legend(*scatter.legend_elements(),title = 'target')

ax1.axhline(y = over_50['thalach'].mean(),linestyle = '--')

fig.suptitle('Heart Analysis', fontsize = 16, fontweight = 'bold')

plt.show()
