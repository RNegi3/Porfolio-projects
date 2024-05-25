

def format_data():
    #file_name = input("Enter the file name: ")
    new_Dict = {}
    try:
        with open('nw1.txt', 'r') as file:
            for line in file:
                users = line.strip().split()
                if not line:
                    continue
                elif len(users) == 2:
                    first_name, second_name = users
                    if first_name not in new_Dict:
                        new_Dict[first_name] = {second_name}
                    
                    else:
                        new_Dict[first_name].add(second_name)

                    if second_name not in new_Dict:
                        new_Dict[second_name] = {first_name}

                    else:
                        new_Dict[second_name].add(first_name)
                        
                elif len(users) == 1 and users[0] not in new_Dict:
                    first_name = users[0]
                    new_Dict[first_name] = {None}
        return new_Dict
    except FileNotFoundError:
        return []

    



