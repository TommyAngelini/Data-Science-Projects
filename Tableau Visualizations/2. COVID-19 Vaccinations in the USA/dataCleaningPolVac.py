# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:20:36 2021

@author: tomas
"""
import pandas as pd
import numpy as np
import seaborn as sns 

electionDF = pd.read_csv('./Data/countyElectionReturns.csv')
covidDF = pd.read_csv('./Data/dailyCovidVaccinations.csv')
covidDF = covidDF.drop('Code',axis=1)
covidDF = covidDF[covidDF['Entity'] != 'United States']
covidDF = covidDF[covidDF['daily_vaccinations'] < 0]

covidDF.to_csv('./dailyCovid.csv')

electionDF
covidDF

# need to clean up election dataset to summarize by state 
electionDF = electionDF[electionDF['year'] == 2020]
electionDF = electionDF[['state', 'state_po', 'party', 'candidatevotes', 'totalvotes']]

# group by state, party 
elecGrouped = electionDF.groupby(['state', 'party']).sum().reset_index()

covidDF = covidDF[['Entity', 'Day', 'daily_vaccinations']]
covidDF

# group by state
covidGrouped = covidDF.groupby(['Entity']).sum().reset_index()

statePop = pd.read_csv('./Data/statePopulations.csv')
statePop

elecGrouped
covidGrouped

# give percentage votes and percentage of pop vaccinations
elecGrouped['percentageTotal'] = elecGrouped['candidatevotes'] / elecGrouped['totalvotes']
elecGrouped

covidCleaned = pd.merge(covidGrouped, statePop, left_on='Entity', right_on='State')
covidCleaned = covidCleaned[['State', 'daily_vaccinations', 'Pop']]
covidCleaned['percentage'] = covidCleaned['daily_vaccinations']/ covidCleaned['Pop']
covidCleaned = covidCleaned.rename(columns={'daily_vaccinations': 'total_vaccinations'})

elecGrouped.to_csv('./Data/electionsDataCleaned.csv')
covidCleaned.to_csv('./Data/vaxDataCleaned.csv')

