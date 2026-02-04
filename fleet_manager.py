
names=["Kirk","Spock","Scotty","Mccoy","Sulu"]
roles=["Officer","Officer","Engineer","Medical Officer","Helmsman"]
divs=["Command","Command","Engine","Medical","Operations"]
races=["Human","Vulcan","Human","Human","Human"]

def init_database():
    for i in range(len(names)):
        print("\n", names[i]+"-"+roles[i]+"-"+divs[i]+"-"+races[i])

def display_menu():
    user=input("User?:").upper
    print("\n","WELCOME"+ user )

def add_member():
    print("hey")


def remove_member():
    print("hello")





def main():
    init_database()
    display_menu()



main()