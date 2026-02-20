# lst= [1,2,3,4,5]
# my_str = "quick brown fox jumps over the lazy dog"
# my_int = 42

# print(type(my_str)) 
# print(type(lst))
# print(type(my_int))

# lst.append(6)

# # lst class ke aander bahut saare methods hote hain, jise hum use kar sakte hain. For example, 
# # lst.append(6) will add the number 6 to the end of the list. Similarly, we can use other methods like lst.pop(), lst.sort(), etc


from py_proj import chatbot
user= chatbot()  # creating an instance of the chatbot class, which will call the __init__ method of the chatbot class and execute the code inside it. The __init__ method is a special method in Python classes that is called when an instance of the class is created. It is used to initialize the attributes of the class and perform
# print(user._chatbot__name) # accessing the private attribute __name of the chatbot 
#                        #class using name mangling. In Python, when we define a private attribute using double underscores, it is name-mangled to prevent direct access from outside the class. To access the private attribute, we need to use the syntax _ClassName__AttributeName, which in this case is _chatbot__name

# print(user.get_name()) # accessing the private attribute __name of the chatbot class using the get_name method, which is a public method that can be accessed from outside the class. The get_name method returns the value of the private attribute __name, which is "default_name" in this case.
# set_name = user.set_name("new_name") # setting the value of the private attribute __name of the chatbot class using the set_name method, which is a public method that can be accessed from outside the class. The set_name method takes a value as an argument and sets the value of the private attribute __name to that value. In this case, we are setting the value of __name to "new_name". After setting the new name, we can access it using the get_name method to verify that it has been updated correctly.
# print(user.get_name()) # accessing the private attribute __name of the chatbot class using the get_name method, which is a public method that can be accessed from outside the class. The get_name method returns the value of the private attribute __name, which is "new_name" in this case.

print(user.id)
user1 = chatbot() 
print(user1.id)

chatbot.reset_userid(10) # resetting the value of the private class variable __userid to 10 using the reset_userid static method, which is a public method that can be accessed from outside the class. The reset_userid method takes a value as an argument and sets the value of the private class variable __userid to that value. In this case, we are resetting the value of __userid to 10. After resetting the userid, we can create a new instance of the chatbot class and check its id to verify that it has been updated correctly.

user2 = chatbot()
print(user2.id)

user3 = chatbot()
print(user3.id)




















