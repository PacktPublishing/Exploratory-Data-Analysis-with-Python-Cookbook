import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import HTML
from itertools import combinations, product

def dataframe_side_by_side(*dataframes):
    html = '<div style="display:flex">'
    for dataframe in dataframes:
        html += '<div style="margin-right: 2em">'
        html += dataframe.to_html()
        html += '</div>'
    html += '</div>'
    display(HTML(html))
    
def summary_stats_analyzer(data):
    df1 = data.describe(include='object')
    df2 = data.describe()
    return dataframe_side_by_side(df1,df2)
    

def univariate_analyzer (data,subset):
    categorical_cols = data.select_dtypes(include = 'object').columns
    discrete_cols = [col for col in data.select_dtypes(include = 'number') if data[col].nunique() < 15]
    numerical_cols = [col for col in data.select_dtypes(include = 'number').columns if col not in discrete_cols]
    all_cols = data.columns
    
    plots = []
    if subset == 'cat':
        print("categorical variables: ", categorical_cols)
        for i in categorical_cols:
            plt.figure()
            chart = sns.countplot(data = data, x= data[i])
            plots.append(chart)
    elif subset == 'num':
        print("Numerical variables: ", numerical_cols)
        for i in numerical_cols:
            plt.figure()
            chart = sns.histplot(data = data, x= data[i])
            plots.append(chart)
    elif subset == 'discrete':
        print("Discrete variables: ", discrete_cols)
        for i in discrete_cols:         
            plt.figure()
            chart = sns.countplot(data = data, x= data[i])
            plots.append(chart)
    else:
        for i in all_cols:
            if i in categorical_cols:
                plt.figure()
                chart = sns.countplot(data = data, x= data[i])
                plots.append(chart)
            elif i in numerical_cols:
                plt.figure()
                chart = sns.histplot(data = data, x= data[i])
                plots.append(chart)
            elif i in discrete_cols:
                plt.figure()
                chart = sns.countplot(data = data, x= data[i])
                plots.append(chart)
            else:
                pass
            
    for plot in plots:
        print(plot)





def bivariate_analyzer (data):
    categorical_cols_ = data.select_dtypes(include = 'object').columns
    discrete_cols_ = [col for col in data.select_dtypes(include = 'number') if data[col].nunique() < 15]
    numerical_cols_ = [col for col in data.select_dtypes(include = 'number').columns if col not in discrete_cols_]
    
    num_num = [t for t in combinations(numerical_cols_, 2)]   
    cat_cat = [t for t in combinations(categorical_cols_, 2)]
    num_cat = [(i,j) for i in numerical_cols_ for j in categorical_cols_ ]  
    dis_num = [(i,j) for i in discrete_cols_ for j in numerical_cols_ if i != j] 
    dis_cat = [(i,j) for i in discrete_cols_ for j in categorical_cols_ if i != j] 
    
    
    plots = []
    for i in num_num:
        plt.figure()
        chart = sns.scatterplot(data = data, x= data[i[0]], y= data[i[1]])
        plots.append(chart)
    for i in num_cat:
        plt.figure()
        chart = sns.boxplot(data = data, x= data[i[1]], y= data[i[0]] )
        plots.append(chart)
    for i in dis_num:
        plt.figure()
        chart = sns.boxplot(data = data, x= data[i[0]], y= data[i[1]] )
        plots.append(chart)
    for i in cat_cat:
        plt.figure()
        cross = pd.crosstab(index= data[i[0]], columns= data[i[1]])
        chart = cross.plot(kind="bar", stacked=True,rot=0)
        plots.append(chart)
    for i in dis_cat:
        plt.figure()
        cross = pd.crosstab(index= data[i[1]], columns= data[i[0]])
        chart = cross.plot(kind="bar", stacked=True,rot=0)
        plots.append(chart)
    else:
         pass
            
    for plot in plots:
        print(plot)