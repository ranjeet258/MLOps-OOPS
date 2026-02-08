class chatbot:
    def __init__(self):
        self.username = ""
        self.password = ""
        print("Chatbot created")
        self.manu()

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


        
    
