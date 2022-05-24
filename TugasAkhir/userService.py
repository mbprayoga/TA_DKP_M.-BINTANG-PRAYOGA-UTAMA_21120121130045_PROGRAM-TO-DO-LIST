class userService:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.data = {
            "bintang@gmail.com" : {
            "email" : "bintang@gmail.com",
            "password" : "12345",
            "role" : "user"
            }
        }


    def checkCredentials(self):
        for value in self.data:
            if value == self.email:
                get_data_user = self.data[value]
                if self.password == get_data_user['password']:
                    return get_data_user
                else:
                    return False
         
                
    def login(self):
        get_data = self.checkCredentials()
        if get_data:
            return True
        else:
            return False