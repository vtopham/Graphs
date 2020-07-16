import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for x in range(num_users):
            self.users[x] = set()
            self.friendships[x] = set()
        # Create friendships
        poss_friendships = []
        for x in self.users:
            for y in range(x + 1, len(self.users)):
                poss_friendships.append((x, y))

        random.shuffle(poss_friendships)
        total_friendships = num_users * avg_friendships

        gathered_friendships = poss_friendships[:total_friendships]

        for x in gathered_friendships:
            print(x)
            friend_1 = x[0]
            friend_2 = x[1]
            
            self.friendships[friend_1].add(friend_2)
            self.friendships[friend_2].add(friend_1)

        return self.friendships
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        def find_path(path, target):
            node = path[-1]
            if node == target:
                return path
            else:
                for x in self.friendships[node]:
                    if x not in path:
                        new_path = list(path)
                        new_path.append(x)
                        poss = find_path(new_path, target)
                        if poss == None:
                            return None
                        else:
                            return poss
                    return None
        
        for x in self.users:
            result = find_path([user_id], x)
            if result != None:
                visited[x] = result

        print(visited)




        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
