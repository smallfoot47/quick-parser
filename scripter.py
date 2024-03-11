import re

class Scripter:
    def __init__(self, scriptFile:str) -> None:
        self.__parse(scriptFile)
    
    def __parse(self, scriptFile) -> None:
        with open(scriptFile) as script:
            snip = script.readline()

            if len(snip) > 0:

                if snip[0] == '~':
                    
                    # pre-proc
                    pass
                elif snip[0] == '-':
                    # pre-sub
                    pass
                elif snip[0] == '+':
                    # post-sub
                    pass
                elif snip[0] == '*':
                    # post-proc
                    pass
            