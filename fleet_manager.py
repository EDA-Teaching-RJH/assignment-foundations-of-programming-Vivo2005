
names=["Kirk","Spock","Scotty","Mccoy","Sulu"]
rank=["Captain","First Officer","Engineer","Medical Officer","Helmsman"]
divs=["Command","Command","Operations","Operations","Operations"]
id=["H1","V1","H2","H3","H4"]
Recognised_Ranks = ["Captain","First Officer","Engineer","Medical Officer","Helmsman","Officer","Ensign","Lieutenant","Lt. Commander","Commander"]

user = input (" User name :").lower().title()

active = True

#done
def init_database():
    for i in range(len(names)):
        print( names[i]+"-"+rank[i]+"-"+divs[i]+"-"+id[i],)
#done
def display_menu():
    
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
    
  
#done
def add_member():
    new_name = input ("crew name:").lower().title()
    new_rank = input ("crew rank:").lower().title()
    new_div = input ("crew division:").lower().title()
    new_id = input ("crew id:").upper()
    if new_rank not in Recognised_Ranks:
        print("Rank not recognised, try again...")
        
    elif new_id in id :
        print ("ID already in use, try again...") 
    
    else:
        names.append(new_name)
        rank.append(new_rank)
        divs.append(new_div)
        id.append(new_id)

        print("Crew member added...")
    
#done
def remove_member():
    rem_id = input("Input crew member ID:").upper()
    if rem_id not in id :
        print ("ID not recognised, try again...")
        
    else:
        I= id.index(rem_id)
        names.pop(I)
        rank.pop(I)
        id.pop(I)
        divs.pop(I)

#done
def update_rank():
    rank_id = input ("Input crew member ID:").upper()
    if rank_id not in id:
        print ("ID not recognised, try again...")
        
    else:
        I= id.index(rank_id)
        n_rank= input ( "what is " + names[I] + "'s new rank :").strip().lower().title()
        rank [I] = n_rank
        print ("Rank updated ...")


# look at how to use a dictionary to create table
def display_roster():
    print ("---Current crew roster:---")
    print ("Names  -  Rank  -  Division  -  ID")
    for i in range(len(names)):
        print (names[i]+" - "+rank[i]+" - "+divs[i]+" - "+id[i])


#done
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
        

# done but fails when a new crew member is added
def filter_by_division():
    d = input ("Science , Operations or Command :").strip().lower().title()
    if d == "Science" :
        print ("No crew on-board ...")

    elif d == "Operations":
        print ("Scotty , Mccoy and Sulu")

    elif d == "Command":
        print ("Kirk and Spock")

    else:
        print ("Division not recognised")
        

#done with dictionary
def calculate_payroll():
    pay = {
        "Captain": 100000,
        "First Officer": 75000,
        "Engineer": 50000,
        "Medical Officer": 50000,
        "Helmsman": 40000
    }
    p=0
    for r in rank:
        if r in pay:
            p=p+pay[r]

    print("Total payroll: $",p)

#done
def count_officers():
      
    count = 0
    for r in rank:
         if r== "Captain" or r == "First Officer": 
            count = count + 1
    print("High ranking officers: ", count)

    
    
    

def main():
    
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

    elif opt =="6":
        filter_by_division()
        
    elif opt == "7":
        calculate_payroll()

    elif opt == "8":
        count_officers()

    elif opt =="9":
        print ("Shutting down...")
        print ("Goodbye", user)
        exit()
    

    else :
        print ("Input not recognised ...")
        


 



init_database()
while True:
   main()
 