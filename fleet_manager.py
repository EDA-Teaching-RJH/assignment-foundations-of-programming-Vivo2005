
names=["Kirk","Spock","Scotty","Mccoy","Sulu"]
roles=["Officer","Officer","Engineer","Medical Officer","Helmsman"]
divs=["Command","Command","Engine","Medical","Operations"]
races=["Human","Vulcan","Human","Human","Human"]

def init_database():
    for i in range(len(names)):
        print("\n", names[i]+"-"+roles[i]+"-"+divs[i]+"-"+races[i])



def main():
    init_database()





main()