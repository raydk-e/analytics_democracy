class ReverseString:
    def __init__(self,string_input):
        self.string_input = string_input

    def reverse_String(self):
        # self.string_input = input("Enter the string: ")
        last_element = self.string_input[-1::-1]
        return last_element
    
rs = ReverseString("ABCDEF")

print(rs.reverse_String())  





    
    
        