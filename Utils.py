import pandas as pd
from config import print_config
from datetime import datetime


class CommonUtils:
    
    @staticmethod
    def getFile(file=None, filepath:str =None):
        if file is not None:
            if isinstance(file, str):
                try:
                    #Todo : check for a trailing slash
                    fileObject = open(filepath+file, "a+")
                    return  fileObject
                except Exception as e:
                    return None
            elif isinstance(file, object):
                return file

    @staticmethod
    def getDataFramefromFile(file=None, filepath:str =None) -> pd.DataFrame:
        if file is not None:
            if isinstance(file, str):
                try:
                    #Todo: based on file extension dynamically map the pandas opening function
                    #Todo : check for a trailing slash
                    fileObject = pd.read_csv(filepath+"/"+file)
                    return  fileObject
                except Exception as e:
                    return None
            elif isinstance(file, object):
                #Todo: Change the file object to dataframe
                return file

    @staticmethod
    def Dataframe_CSV(data=None, file=None, filepath: str = None) -> pd.DataFrame:
        if file is not None:
            if isinstance(file, str):
                try:
                    # Todo: based on file extension dynamically map the pandas opening function
                    # Todo : check for a trailing slash
                    fileObject = data.to_csv(filepath + "/" + file, index=None)
                    return fileObject
                except Exception as e:
                    return None
            elif isinstance(file, object):
                # Todo: Change the file object to dataframe
                return file

    @staticmethod
    def convert_to_datetime(data_frame=None, columns=None):
        
        for col in columns:
            data_frame[col] = pd.to_datetime(data_frame[col])
        return data_frame




    def console(*values, print_value=print_config, sep: str = ..., end: str = ...):
        #Todo: change the file path and name from inline to config
        if print_value in ["file", 2, "F", "File"]:
            file = open(file_path, "a+")
            print(*values, file=file)
        elif print_value in ["text", 1, "inline", "console", "terminal"]:
            print(*values)




