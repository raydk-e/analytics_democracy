def lengthyString(*args):
    final_string = ''
    for i in args:
        final_string = final_string+ " "+ i
    return final_string

print(lengthyString('i', 'am', 'confused', 'how', 'to', 'work', 'in', 'our' , 'house'))
