class User:
    def __init__(self, first_name, last_name):
        print("Создан")
        self.name = first_name
        self.second_name = last_name

    def sayName(self):
        print("Мое имя", self.name)

    def saySecondname(self):
        print("Моя фамилия", self.second_name)

    def sayNameandSecondname(self):
        print("Меня зовут", self.name, self.second_name)


konstantin = User("Konstantin", "Belyakov")

konstantin.sayName()
konstantin.saySecondname()
konstantin.sayNameandSecondname()
