
names=["Kirk","Spock","Scotty","Mccoy","Sulu"]
rank=["Officer","Officer","Engineer","Medical Officer","Helmsman"]
divs=["Command","Command","Engine","Medical","Operations"]
id=["H1","V1","H2","H3","H4"]

def init_database():
    for i in range(len(names)):
        print( names[i]+"-"+roles[i]+"-"+divs[i]+"-"+races[i],"\n")

def display_menu():
    user=input("User?:")
    print("--- WELCOME",user.upper(),"---")
    print("1. Add Crew To Roster")
    print("2. Remove crew from roster")
    print("3. Update role")
    print("4.")
    print("5.")
    print("6.")
    print("7.")
    print("8.")


def add_member():
    print("hey")


def remove_member():
    print("hello")





def main():
    init_database()
    display_menu()



main()