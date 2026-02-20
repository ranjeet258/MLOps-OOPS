class chatbot:
    __userid = 0  # private class variable to keep track of user ids
    def __init__(self):
        self.__name= "default_name"  # __name is a private attribute, it can only be accessed within the class, it cannot be accessed from outside the class. It is a convention to use double underscore before the attribute name to indicate that it is a private attribute.
        self.username = ""
        self.id=chatbot.__userid
        chatbot.__userid +=1
        self.userid = 0
        self.userid+=1
        self.password = ""
        # print("Chatbot created")

    @staticmethod   # static method is a method that belongs to the class rather than an instance of the class. It can be called on the class itself, rather than on an instance of the class. Static methods are defined using the @staticmethod decorator and do not take the self parameter as the first argument. They are typically used for utility functions that do not require access to instance-specific data.
    def get_userid():
        return chatbot.__userid
    
    @staticmethod
    def reset_userid(value):
        chatbot.__userid = value
        
    # getter and setter methods for the private attribute __name of the chatbot class
    def get_name(self):  # accessing the private attribute __name of the chatbot class using the get_name method, which is a public method that can be accessed from outside the class. The get_name method returns the value of the private attribute __name, which is "default_name" in this case.
        return self.__name
    
    def set_name(self, value):  # setting the value of the private attribute __name of the chatbot class using the set_name method, which is a public method that can be accessed from outside the class. The set_name method takes a value as an argument and sets the value of the private attribute __name to that value. In this case, we are setting the value of __name to "new_name". After setting the new name, we can access it using the get_name method to verify that it has been updated correctly.
        self.__name= value

    def manu(self):
        user_input= input("""Welcome to the chatbot! Please enter your username and password to continue.
                            \n1. Signup\n2. Login\n3. write a post \n4. msg to friend \n5. Exit\n
                          ->""")
        
        if user_input == "1":
            self.signup()          # calling the signup method , self is used to call the method of the class, it is a reference to the current instance of the class.
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            self.write_post()
        elif user_input == "4":
            self.msg_to_friend()
        elif user_input == "5":
            print("Exiting the chatbot. Goodbye!")
        else:
            print("Invalid input. Please try again.")

    def signup(self):                  # self is used to access the attributes and methods of the class, it is a reference to the current instance of the class. 
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.username = email
        self.password = password
        print(f"Welcome, {self.username}!")
        self.manu()
    
    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if email == self.username and password == self.password:
            print(f"Welcome back, {self.username}!")
            self.login = True
        else:
            print("Invalid email or password. Please try again.")
        self.manu()
        

    def write_post(self):
        if self.login== True:
            post = input("Write your post: ")
            print(f"Your post: {post}")
            self.manu()
        else:
            print("Please login to write a post.")
        self.manu()
    def msg_to_friend(self):
        if self.login== True:
            friend = input("Enter your friend's name: ")
            msg = input("Enter your message: ")
            print(f"Message to {friend}: {msg}")
        else:
            print("Please login to send a message.")
        self.manu()
    
    
my_chatbot = chatbot()


        
    
