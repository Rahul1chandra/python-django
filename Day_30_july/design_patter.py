####   we have follow some set of standard for developing any application 
####   for better readiablity and maintaince 


# Desgin Patter :
"""
       1)  Creantional Pattern
                Sigleton                **
                Prototype
                Factories               **
                    Abstract Factories
                    Factories Method
       2) Structural Pattern
                Adapater Pattern        **
                Bridge Pattern
                Componsite(has -a relationship)
                Decorator
                flyweight
                proxy
        3) Behavioral Patter
                Chain of reposiblity
                visitor patter
                state
                interator patter
                ........................




"""

# Sigleton pattern
# we have to create one and only object

def singleton(class_):
    instance = {}
    
    def get_instance(*arg, **kwargs):
        if class_ not in instance:
            # import ipdb; ipdb.set_trace()
            instance[class_] = class_
        return instance[class_]
    return get_instance



@singleton
class Singletoncls:
    def __init__(self):
        print ("loading database")


d1_obj =  Singletoncls()
d2_obj = Singletoncls()
d3_obj = Singletoncls()


print (id(d1_obj))
print (id(d2_obj))

print (d1_obj ==  d2_obj)







class Singletonclass:
    instance = {}
    def __init__(self):
        if not instance:
            instance[self] = self
        return instance[self]

        






