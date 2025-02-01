#################
# INP
#################

class inp:
    def Type(self):
        if self.type == "int" or self.type == int:
            return "int"
        elif self.type == "float" or self.type == float:
            return "float"
        elif self.type == "bool" or self.type == bool:
            return "bool"
        elif self.type == "list" or self.type == list:
            return "list"
        elif self.type == "dict" or self.type == dict:
            return "dict"
        elif self.type == "tuple" or self.type == tuple:
            return "tuple"
        else: return "str"

    def Generate(self):
        return input(f'{self.text} (Type: {self.Type()}){self.end}')

    def __init__(self, text, type: str = "", end: str =": "):
        self.text = text
        self.type = type
        self.end = end
        self.value = self.Generate()
    
    def __str__(self):
        return str(self.value)
    
    def __int__(self):
        return int(self.value)
    
    def __float__(self):
        return float(self.value)
    
    def __bool__(self):
        return bool(self.value)
    
    def __list__(self):
        return list(self.value)
    
    def __dict__(self):
        return dict(self.value)
    
    def __tuple__(self):
        return tuple(self.value)

i = inp("Enter a num", int, ":\n")
print(f"input: {i}")

# inp("asd" <- required) = input("asd")
# inp("asd", int) or inp("asd", "int") -> int(input("asd"))
# inp("asd", str, "\n") -> input("asd" + "\n")

#################
# LISTS
#################

class listPlus:
    def __init__(self): pass
    
    def removeDuplicated(self, l: list, case: str =""):
        self.value = list(dict.fromkeys(l).keys())
        if case == "l" or "low" or "lower":
            for i in range(0, len(self.value)):
                if str(type(self.value[i])) == "<class 'str'>":
                    self.value[i] = self.value[i].lower()
                else: pass
        return self.value
    
    def __list__(self):
        if self.value:
            return list(self.value)
        else:
            return "Not defined"

print(listPlus().removeDuplicated(["a", "a", "a", "b"]))