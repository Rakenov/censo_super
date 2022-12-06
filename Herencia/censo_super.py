class Human:

    def __init__(self,first_name,last_name,date_of_birth,gender,adress):
        self.first_name= first_name
        self.last_name= last_name
        self.date_of_birth= date_of_birth
        self.gender= gender
        self._adress= adress

    def data(self):
        self.first_name= input("Ingrese su nombre:")
        self.last_name= input("Ingrese su apellido:")
        self.date_of_birth= input("ingrese su fecha de naciemiento:")
        self.gender= input("Ingrese su genero:")
        self._adress= input("Ingrese su dirección:")

    def print(self):
        print("Nombre:",self.first_name,self.last_name)
        print("Fecha de nacimiento:",self.date_of_birth)
        print("Genero:",self.gender)
        print("Dirección:",self._adress)
    




