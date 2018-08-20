 
# Modify this function to return a list of strings as defined above
# You need to put parenthesis () to group the 
def list_benefits():
    return ("More organized code",  
    "More readable code", 
    "Easier code reuse", 
    "Allowing programmers to share and connect code together")

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def myfunc():
    list_of_benefits = list_benefits() 
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

myfunc()


# 
test = ['sam', 'amador', 25]
arr  = [23, 54 ,24]
print(type(test))
print(type(arr))

