import csv
import pandas as pd
import numpy as np
import requests
import json
import sys
import re

def readReviwerscsv(CSVFile):
	df=pd.read_csv(CSVFile)
	return df

def readAuthorscsv(CSVFile):
	df=pd.read_csv(CSVFile)
	return df

def filterCitations(df):
	df=df.drop(df[(df.citedby <100) | (df.citedby>1000) ].index)
	#df=df.ix[(df['citedby'] >= 100) & (df['citedby']<=1000)]
	return df

def excludeCOIs(Revdf,Authdf):
	# get rid of COIs (Reviewer : not one of authors, no co-work or afilliations, not in a same country)
	Revdf=Revdf[~Revdf.Affiliation.isin(Authdf.affiliation.values)]
	Revdf=Revdf[~Revdf.Name.isin(Authdf.Name.values)]
	return Revdf

def main():
    Reviewersdf= readReviwerscsv(sys.argv[1])
    print(len(Reviewersdf.index))
    Authorsdf= readReviwerscsv(sys.argv[2])
    print(len(Authorsdf.index))
    df=filterCitations(Reviewersdf)
    print(len(df.index))
    exdf=excludeCOIs(df,Authorsdf)
    print(len(exdf.index))
    print(exdf.Name)

if __name__ == '__main__':
    main()