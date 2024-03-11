import re

class Wrapper:
    def __init__(self, header:str='', body_fmt:str='', footer:str='', axe:str=' ', glue=',', arg_prep:int=10) -> None:
        self.__h = header
        self.__b = body_fmt
        self.__arg_count(10)
        self.__f = footer
        self.__a = axe
        self.__g = glue
    
    def __arg_count(self, guess:int) -> None:
        if "{" + str(guess) + "}" in self.__b:
            guess += 1
            while "{" + str(guess) + "}" in self.__b: guess += 1
            return guess
        else:
            guess -= 1
            while "{" + str(guess) + "}" not in self.__b: guess -= 1
        
        self.__argc = guess

    def __fix_string(self, ajar:str) -> str:
        apickle = re.sub(r'(?<!\\)\\n', r'\n', ajar)
        return apickle
    
    def __format(self, form, tokens) -> str:
        argc = min(self.__argc, len(tokens))

        for idx, token in enumerate(tokens):
            form = form.replace("{"+ str(idx) + "}", token)
        
        for idx in range(argc, self.__argc):
            form = form.replace("{" + str(idx) + "}", '')
        
        return form
    
    def Set(self, header:str=None, body_fmt:str=None, footer:str=None, axe:str=None, glue:str=None) -> None:
        if header != None:
            self.__h = header
        if body_fmt != None:
            self.__b = body_fmt
        if footer != None:
            self.__f = footer
        if axe != None:
            self.__a = axe
        if glue != None:
            self.__g = glue
    
    def Wrap(self, filepath:str) -> str:
        wrapping = ''
        try:
            with open(filepath) as data_file:
                wrapping += self.__fix_string(self.__h)
        
                body = []
                
                for line in data_file.read().splitlines():
                    tokens = line.split(self.__a)
                    body.append(self.__format(self.__b, tokens))
                
                wrapping += self.__fix_string(self.__g.join(body))
                
                wrapping += self.__fix_string(self.__f)
                
                return wrapping
            
        except Exception as e:
            raise e