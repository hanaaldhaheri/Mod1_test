# try:
#     print("Hana"+12)
# except:
#     print("Error")

def accept_string(text=None):
    try:
        if  text is None:
            raise Exception
        return text
    except:
        print("Null")
    
    
print(accept_string("mouse"))


        
