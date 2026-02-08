
names=["Kirk","Spock","Scotty","Mccoy","Sulu"]
rank=["Officer","Officer","Engineer","Medical Officer","Helmsman"]
divs=["Command","Command","Engine","Medical","Operations"]
id=["H1","V1","H2","H3","H4"]

def init_database():
    for i in range(len(names)):
        print( names[i]+"-"+rank[i]+"-"+divs[i]+"-"+id[i],)

def display_menu():
    user=input("User?:")
    print("\n--- WELCOME",user.upper(),"---")
    print("1. Add Crew To Roster")
    print("2. Remove crew from roster")
    print("3. Update rank")
    print("4. display roster")
    print("5. search crew")
    print("6. search division")
    print("7. calculate pay role")
    print("8. count officers")
    print("9. exit")
    
  

def add_member():
    new_name = input ("crew name:").lower().title()
    new_rank = input ("crew rank:").lower().title()
    new_div = input ("crew division:").lower().title()
    new_id = input ("crew id:").upper()
    if new_rank not in rank :
        print("Rank not recognised, try again...")
        add_member()
    elif new_id in id :
        print ("ID already in use, try again...") 
        add_member()
    else:
        names.append(new_name)
        rank.append(new_rank)
        divs.append(new_div)
        id.append(new_id)

        print("Crew member added...")
    

def remove_member():
    rem_id = input("Input crew member ID:").upper()
    if rem_id not in id :
        print ("ID not recognised, try again...")
        remove_member()
    else:
        I= id.index(rem_id)
        names.pop(I)
        rank.pop(I)
        id.pop(I)
        divs.pop(I)


def main():
    init_database()
    display_menu()

    opt= input("select function:")

    if opt == "1":
        add_member()
    
    elif opt == "2":
        remove_member()

 





main()