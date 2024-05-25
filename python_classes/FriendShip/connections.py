import read_data


class SocialNetwork:
    def __init__(self):
        self.network = read_data.format_data()
    
    def friends_list(self):
        for key, values in self.network.items():
            values_list = list(values)
            if len(values) >= 3:
                initial_friends = ', '.join(map(str, values_list[:-1]))
                last_friend = str(values_list[-1])
                print(f'{key} is friends with {initial_friends} and {last_friend}')
            
            elif len(values) == 2:
                friends = ' and '.join(map(str, values_list))
                print(f'{key} is friends with {friends}.')
                
            elif len(values) < 1:
                print(f'{key} doesnt have any friends.')

            else:
                print(f'{key} is friends with {values_list[0]}')
    
    def highest_name_len(self):
        highest_len = 0
        for users in self.network:
            if len(users) > highest_len:
                highest_len = len(users)

        return highest_len

    def get_unqiue_users(self):
        
        count_users = 0
        for _ in self.network:
            count_users += 1
        print(f'There are {count_users} unique in this social network.')
    
    def checking_solo(self):
        # print(self.network["Ritesh"])
        for keys, values in self.network.items():
            print(self.network[keys])

sn = SocialNetwork()
sn.checking_solo()

