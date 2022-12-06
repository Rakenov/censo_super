from censo_super import Human

class Superhero(Human):
    
    def __init__(self,first_name,last_name,date_of_birth,gender,adress,hero_name,super_power,weakness):
        super().__init__(first_name,last_name,date_of_birth,gender,adress)
        self.__hero_name= hero_name
        self.__super_power= super_power
        self.__weakness= weakness

    def setHero_name(self):
        self.__hero_name= input("Ingrese su nombre de Super Heroe:")
    
    def setSuper_power(self):
        self.__super_power= input("Ingrese una descripción de su super poder:")
    
    def setWeakness(self):
        self.__weakness= input("Ingrese sus debilidades:")
    
    def getHero_name(self):
        return self.__hero_name
    
    def getSuper_power(self):
        return self.__super_power

    def getWeakness(self):
        return self.__weakness

def main():
    print("\t\t\t Censo Mundial")
    print("Seleccione una opción")
    print("1.-Registrar persona no super")
    print("2.-Registrar SuperHeroé")
    print("3.-Salir")

    option=int(input())

    if option==1:
        human1= Human("first_name","last_name","date_of_birth","gender","adress")
        human1.data()
        human1.print()
    elif option==2:

        super1= Superhero("first_name","last_name","date_of_birth","gender,adress,hero_name,super_power,weakness)
        super1.data()
        super1.setHero_name()
        super1.setSuper_power()
        super1.setWeakness()
        super1.print()
        super1.getHero_name()
        super1.getSuper_power()
        super1.getWeakness()

main()

