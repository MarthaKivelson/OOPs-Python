class chatbook:
    def __init__(self):
        self.id = 123
        self.pwd = 0000
        self.loggedin = False
        self.menu()

    def menu(self):
        user_ip = input("""
            Welcome to chatbook
            Press 1 to signup
            Press 2 to login
            Press 3 to Write a post
            Press 4 to msg a friend
            Press any other key to exit
            """)
        if user_ip == str("1"):
            self.signup()
        elif user_ip == str("2"):
            self.login()
        elif user_ip == str("3"):
            self.post()
        elif user_ip == str("4"):
            self.msg()
        else:
            exit()
        
    
    def  signup(self):
        self.id = input("Enter user user id:\n")
        self.pwd = input("Enter your password\n")
        print("Your profile has been successfully created")
        self.menu() 

    def login(self):
        login_id = input("Enter user user id:\n")
        login_pwd = input("Enter your password\n")
        if login_id == self.id and login_pwd == self.pwd:
            print("Successfully logged in")
            self.loggedin = True
        else:
            print("Invalid credintials")
        self.menu()

    def post(self):
        if self.loggedin == False:
            print("Please login")
        else:
            post = input("Whats on your mind: ")
            print(post + "\n Posted successfully")
        self.menu()

    def msg(self):
        if self.loggedin == False:
            print("Please login")
        else:
            user = input("Whom do you want to send the messgage\n")
            ip_msg = input("Whats on your mind: ")
            print(ip_msg + "\n Message successfully sent to " + user)
        self.menu()
     

user0 = chatbook()