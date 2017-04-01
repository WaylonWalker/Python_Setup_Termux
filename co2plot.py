#' #Testing out pweave on android with Termux

import matplotlib
matplotlib.use('agg')
from tabulate import tabulate
from co2data import df

#' ## raw data
#' *from data.world*
# This example will plot the co2 emissions trend for the top 5 countries in 2011


print(tabulate(df.iloc[0:10, 0:5], headers=df.columns, tablefmt='simple'))

#' ## Transform Data for plotting
#' 
plot_df = (df
    .set_index('CO2 emission total')
    .sort_values('2011', ascending=False)
    .head(5)
    .T
    .dropna(how='all')
    )

print(tabulate(plot_df.iloc[0:10, 0:5], headers=plot_df.columns, tablefmt='simple'))

#' Plot the data
title = 'Top 5 countries CO2 emissions trend\n(based on 2011 emissions data)'
ax = plot_df.plot(title=title)
ax.figure.savefig('tmp.png')


