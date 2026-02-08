
names=["Kirk","Spock","Scotty","Mccoy","Sulu"]
rank=["First Officer","Officer","Engineer","Medical Officer","Helmsman"]
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

def update_rank():
    rank_id = input ("Input crew member ID:").upper()
    if rank_id not in id:
        print ("ID not recognised, try again...")
        update_rank()
    else:
        I= id.index(rank_id)
        n_rank= input ( "what is " + names[I] + "'s new rank :").strip().lower().title()
        rank [I] = n_rank
        print ("Rank updated ...")

def display_roster():
    print("m")

def search_crew():
    t= input ("Search for ...:").strip().lower().title()
    if t in names:
        n= names.index(t)
        print (names[n]+"-"+rank[n]+"-"+divs[n]+"-"+id[n])
    elif t in rank:
        r = rank.index(t)
        print (names[r]+"-"+rank[r]+"-"+divs[r]+"-"+id[r])
    elif t in divs :
        d= divs.index(t)
        print (names[d]+"-"+rank[d]+"-"+divs[d]+"-"+id[d])
    elif t in id:
        i= id.index(t)
        print (names[i]+"-"+rank[i]+"-"+divs[i]+"-"+id[i])
    else:
        print ("No crew found , try again")
        search_crew()
    
    
       



def main():
    init_database()
    display_menu()

    opt= input("select function:")

    if opt == "1":
        add_member()
    
    elif opt == "2":
        remove_member()

    elif opt == "3":
        update_rank()

    elif opt == "4":
        display_roster()

    elif opt == "5":
        search_crew()

 





main()