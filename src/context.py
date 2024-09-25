import os

from api import do_request
from docx_reader import docx_strategy
from jpeg_raw_reader import jpeg_raw_strategy


class Context:
    def __init__(self, file_path :str, ai :bool, key:str = None, strategy = None, description:str=None):
        self.file_path = file_path
        self.strategy = strategy
        self.key = key
        self.ai = ai
        self.description = description
    
    def eval (self):
        if self.strategy:
            strat_ret = self.strategy(self.file_path, self.description)
            
            if self.ai:
                response = do_request(self.key, strat_ret)
                return response
            else:
                if strat_ret:
                    return strat_ret
                else:
                    print("an error occurred wasn't able to create filename")
                    return os.path.basename(self.file_path)
        else:
            print(f"no strategy for file {self.file_path}")
            return os.path.basename(self.file_path)


def eval_strategy(file_path:str):
    _, extension = os.path.splitext(file_path)
    if extension == ".docx":
        return (True, docx_strategy)
    if extension in ['.jpg', '.jpeg','.cr2', '.nef', '.arw', '.dng']:
        return (False, jpeg_raw_strategy)
    return (False, None)