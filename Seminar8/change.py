def change(new_name, old_name):
    persons = file.txt()
    with open("file.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")

    

   
    
   
    
