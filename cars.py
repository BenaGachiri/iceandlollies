# cars ={"model":"ford",
#        "year":1990,
#        "colour":"red",
#        "counrty":"zambia",

# }
# print(cars["year"])
# print(cars["counrty"])

# person={
#         "name":"sam",
#         "age":4,
#         "pets":["dog","cats"]

# }
# person["pets"][0]
# print(person["pets"][0])


# person={
#         "name":"sam",
#         "age":4,
#       ?0

profile={}
profile["username"] ="user123"
profile["age"]=20
#profile["email"]="user123@gmail.com"}

profile={}
def login():
    #ask for username
    #ask for password
    #store in a dictionary
    

    username=input("Enter username:")
    email=input("Enter email:")
    password=input("Enter password:") 


    profile["username"]=username
    profile["email"]=email
    profile["password"]=password
login()

def get_profile():
    print(profile)
    get_profile()  

def change_username():
        new_username=input(" enter new_username")
        profile["username"]=new_username
login()
get_profile()
    