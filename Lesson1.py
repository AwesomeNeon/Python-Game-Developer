countryDb = {}
while True:
    print("1.Insert")
    print("1.Display all countries")
    print("3. Display all capitals")
    print("Get capital")
    print("Delete")
    
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
       country = input("Enter country :").upper()
       capital = input("Enter capital :").upper()
       countryDb[country] = capital
       
    elif choice == 2:
        print(list(countryDb.keys()))
        
    elif choice == 3:
        print(list(countryDb.values()))
    elif choice == 4:
      country = input("Enter country :").upper()
      print(countryDb.get(country))
            
    elif choice == 5:
        country = input("Enter country : ").upper()
        del countryDb[country]
    else:
        break