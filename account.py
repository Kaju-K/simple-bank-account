class Account():

    __existing_accounts = []

    def __init__(self):
        self.__number = self.account_number()
        self.__owner = self.asking_name()
        self.__amount = 0.00
        self.__limit = 1000.00
        print("Welcome {}! Your account number is {} and you currently have ${} on your bank account.".format(self.__owner, self.__number, self.__amount))

    def account_number(self):
        while True:
            account_number = 0

            while account_number == 0:
                account_number_str = input("Choose an account number: ")
                try:
                    account_number = int(account_number_str)
                except:
                    print("The account number should be a number")
                else:
                    if (account_number < 100) or (account_number > 9999):
                        print("The account number should be between 100 and 9999")
                        account_number = 0

            if account_number in self.__existing_accounts:
                print("This account number already exists")
            else:
                self.__existing_accounts.append(account_number)
                return account_number

    def asking_name(self):
        first_name = ""

        while not(first_name):
            first_name = input("What's your first name: ").strip().capitalize()
            if not(self.valid_name(first_name)):
                print("Only letters are allowed in the name, please type again.")
                first_name = ""

        last_name = ""

        while not(last_name):
            last_name = input("What's your last name: ").strip().capitalize()
            if not(self.valid_name(last_name)):
                print("Only letters are allowed in the name, please type again.")
                last_name = ""
        return first_name + " " + last_name
    
    def valid_name(self, name):
        invalid_characters = set("0123456789!@#$%¨&*()-=+_'\"\\|,.;<>£¢¬}{[]:")
        if invalid_characters.intersection(set(name)) != set():
            return False
        return True

    def balance(self):
        print("You have {} on your account".format(self.__amount))

    def deposit(self, value):
        self.__amount += value

    def withdraw(self, value):
        test = self.__amount - value
        if test >= 0:
            self.__amount = test
        else:
            print("You don't have enough money on your account to withdraw this amount")
            print("Your current balance is {}".format(self.__amount))

    def transfer(self, another_account):
        value = 0
        while value == 0:
            value_str = input("How much money would you like to transfer?\n")
            try:
                value = int(value_str)
            except:
                print("You have to put a number")
            else:
                if self.__amount - value >= 0:
                    another_account.deposit(value)
                self.withdraw(value)

    @property
    def amount(self):
        return self.__amount

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value

    @staticmethod
    def bank_code():
        return "001"