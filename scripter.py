import re

class Instruction:
    def __init__(self, preproc=[], presub=[], postsub=[], postproc=[]) -> None:
        self.__cat = {
            '~' : preproc,
            '-' : presub,
            '+' : postsub,
            '*' : postproc
        }
    
    def Get(self, key:str) -> tuple:
        return self.__cat[key]
    
    def Set(self, key:str, value:tuple) -> None:
        self.__cat[key] = value
    

class Scripter:
    def __init__(self, scriptFile:str) -> None:
        self.__parse(scriptFile)
    
    def __parse(self, scriptFile) -> None:
        with open(scriptFile) as script:
            self.__instr = Instruction()

            for snippet in script.readlines():
                instruction = None

                if len(snippet) > 0:
                    if snippet[0] == '~':
                        # pre-proc
                        pass
                    elif snippet[0] == '-':
                        # pre-sub
                        pass
                    elif snippet[0] == '+':
                        # post-sub
                        pass
                    elif snippet[0] == '*':
                        # post-proc
                        pass
                
                    self.__instr[snippet[0]].append(instruction)