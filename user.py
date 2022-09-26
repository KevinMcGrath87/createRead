from mysqlconnection import connectToMySQL 


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users_schema.users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return(users)
    @classmethod
    def insertion(cls,fname, lname, email):
        query = 'INSERT into users_schema.users (first_name,last_name,email, created_at, update_at) VALUES(%(firstname)s,%(lastname)s,%(email)s,now(),now());'
        data = {'firstname' : fname, 'lastname':lname, 'email':email}
        connectToMySQL('users_schema').query_db(query, data)
