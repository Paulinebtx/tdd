def leapYear(i): 
    if((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):   
        return(i," is a leap year")
    else: 
        return(i," is not a leap year")
        