class character:
    def __init__(self,firstname,lastname,email,age):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points=0

    def display_info(self):
        print(self.firstname)
        print(self.lastname)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
    
    def enroll(self):
        if self.is_rewards_member==True : 
            print('User already a member')
            return False
        else:
            self.is_rewards_member=True
            self.gold_card_points=200
        
        


    def spend(self,amount):
        if self.gold_card_points > amount:
            self.gold_card_points=self.gold_card_points-amount
        

sadik=character("sadik","zrelli","zadkoa@izad.com",21)
iheb=character("iheb","bs","a@izad.com",28)
# print(sadik.firstname)
sadik.display_info()
#iheb.display_info()

sadik.enroll()
sadik.spend(1000)
sadik.enroll()
sadik.display_info()

print(sadik.is_rewards_member)
print(iheb.is_rewards_member)
