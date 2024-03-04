'''
String Implementation.
'''


class String:
    
    
    def __init__(self, size: int):
        self.elements = [None] * (size + 1)

    
    def __repr__(self):
        return 'Elements in string: ' + str(self.elements)


    def insert(self, char: str, index: int) -> bool:
        self.elements[index] = char
        return True
    

    def delete(self, index: int) -> bool:
        self.elements[index] = None
        return True
    

    def show(self) -> None:
        for element in self.elements:
            if element != '/':
                print(element, end='')
            else:
                print('')
                return None


    def length(self) -> int:
        len = 0
        for element in self.elements:
            if element != '/':
                len += 1
            else:
                return len
    

    def upper(self) -> None:
        for element in self.elements:
            if element != '/':
                if ord(element) > 96 and ord(element) < 123:
                    upper_char = chr(ord(element) - 32)
                    print(upper_char, end='')
                else:
                    print(element, end='')
            else:
                print('')
                return None  
    

    def lower(self) -> None:
        for element in self.elements:
            if element != '/':
                if ord(element) > 64 and ord(element) < 91:
                    lower_char = chr(ord(element) + 32)
                    print(lower_char, end='')
                else:
                    print(element, end='')
            else:
                print('')
                return None  









