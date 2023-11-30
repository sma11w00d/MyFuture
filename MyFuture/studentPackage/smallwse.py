#student.py

#create a class with 6+2, capitalize the first letter
#Write a method in class called addMyFuture, and put it in the my_future_dataframe

import pandas as pd

class Smallwse:
    def addMyFuture(self, my_future_dataframe):
        my_info= {
            'Name':['Sam Smallwood'], 
            'Major':['Information Systems'], 
            'DesiredPosition':['Software Developer']}
        smallwse_df = pd.DataFrame(my_info)
        updated_df = pd.concat ([my_future_dataframe, smallwse_df])
        
        return updated_df 


