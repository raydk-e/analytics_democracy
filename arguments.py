def justprint(variable, *args, **kwargs):
    print("This is printing variable first time --", variable)
    print("second time --" , variable)
    for i in args:
        print(i)
    print('-'*50)
    for k in kwargs:
        print(k, ":", kwargs[k])

justprint('Santhia',"You stayed in santhia for 19 years", 
          "You completed your studies from there", 
          school = "Nilakanthapur", 
          ground = "Huripada", 
          temple = "shiv mandir")
