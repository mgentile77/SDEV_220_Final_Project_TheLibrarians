from typing import OrderedDict
import pandas as pd
from openpyxl import load_workbook
import os
from collections import OrderedDict, defaultdict 
pd.set_option('display.float_format', '{:.2f}'.format)

cwd = os.path.abspath(os.path.join(os.getcwd()))
excel_file = os.path.join(cwd, "Library.xlsx")
bfile = pd.read_excel(excel_file, header=0, index_col='Book_ID', sheet_name="Books", dtype={'ISBN':str})       
mfile = pd.read_excel(excel_file, index_col='Member_ID',sheet_name="Members")
borfile = pd.read_excel(excel_file, header=0, index_col=[0,1], sheet_name="Books_Out",
                                     parse_dates = ['Date_Borrowed', 'Date_Due'])
finefile = pd.read_excel(excel_file, header=0, sheet_name="Fines", index_col=[0])





def bks_late():    
    with pd.option_context('display.max_rows', None, 'display.max_colwidth', 50, 'display.width', 100):
        __late_merge = borfile.merge(mfile[['Fname', 'Lname', 'Phone', 'Email']], right_index=True, 
                                            left_on='Member_ID'
                                            ).merge(bfile[['Title', 'Author']], right_index=True, 
                                                    left_on= 'Book_ID'
                                                    ).merge(finefile[['Balance']], left_on='Member_ID', right_index = True)
        __late_merge[['Days_Late']] = pd.Timestamp.today().floor('D') - __late_merge[['Date_Due']]
        __late_merge['Title'] = __late_merge['Title'].str.wrap(45)
        __late_merge['Name']= (__late_merge['Fname']+" "+__late_merge['Lname'])
        __late_merge['Author']= __late_merge['Author'].str.split().str[-1]
        __late_merge = __late_merge[['Name', 'Phone', 'Email', 'Title', 'Author','Days_Late','Late','Balance']]
        __late_merge= __late_merge.set_index(['Name', 'Phone', 'Email','Balance', 'Title']
                                                ).groupby(['Days_Late']).filter(lambda x: (x['Late'] == 'Late').any())
        __late_merge=__late_merge.drop(columns='Late')
        __late_merge= __late_merge.dropna(axis=0, how='any')
        # __late_merge = df.style.applymap_index(lambda v: "font-weight: bold;", axis="columns")
        __late_merge = __late_merge.to_string(index=True, max_colwidth=45, show_dimensions=True,
                                              justify='center', index_names=True ).replace('\n2', '\n'+'_'*500+'\n2')
    return __late_merge

print (bks_late())
# df = bks_late()
# s = {level: df.xs(level).to_dict('index') for level in df.index.levels[0]}


# print (s)
