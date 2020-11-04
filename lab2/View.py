class View:

    def print_menu(self):
         choice = 0
         while not (choice in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33']):
             print("Select an option")
             print("1. Find a post by name")
             print("2. Find a post by id")
             print("3. Find user`s posts")
             print("4. Find user`s comments")
             print("5. Find a comment by id")
             print("6. Find user by id")
             print("7. Find user by name")
             print("8. Find user`s subscribers")
             print("9. Find user`s subscribes")
             print("10. Find post`s comments")
             print("11. Find all posts")
             print("12. Find all  users")
             print("13. Find all comments")
             print("14. Add post")
             print("15. Add user")
             print("16. Add comment")
             print("17. Subscribe")
             print("18. Update user")
             print("19. Update comment")
             print("20. Update post")
             print("21. Delete user")
             print("22. Delete comment")
             print("23. Delete post")
             print("24. Delete subscriber ")
             print("25. Find users who wrote post on theme with rating more than and name like")
             print("26. Find posts which admin(or not) wrote with number of comments and name of post like")
             print("27. Find posts  on theme like under which user`s with number of subscribers more than wrote comment with rating more than")
             print("28. Generate comments")
             print("39. Generate users")
             print("30. Generate subscriptions")
             print("31. Generate parent comments")
             print("32. Generate posts")
             print("33. Exit ")
             choice = input ("Enter your choice:")
         return choice

    def get_id(self):
        id=0
        while True:
            try:
                id=int(input("Enter id:"))
                if id<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return id
    def get_subscribe(self):
        id = {}
        while True:
            try:
                id["user"]= int(input("Enter user_id:"))
                if id["user"] < 1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                id["subscriber"] = int(input("Enter id_subscriber:"))
                if id["subscriber"] < 1:
                    print("You must enter positive integer. Try again")
                    continue
                if id["subscriber"]==id["user"]:
                    print("You should enter different subscriber, not like user. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return id

    def get_name(self):
        return input("Enter name:")

    def add_post(self):
        post={}
        post["name"]=input("Enter name:")
        post["theme"]=input("Enter theme:")
        post["text"]=input("Enter text:")
        while True:
            try:
                post["id_user"]=int(input("Enter id_user:"))
                if post["id_user"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return post

    def add_user(self):
        user={}
        user["name"] = input("Enter name:")
        user["login"] = input("Enter login:")
        user["password"] = input("Enter password:")
        user["status"] = input("Enter status or 'NULL':")
        user["admin"] = input("Enter admin or 'NULL':")
        return user

    def add_comment(self):
        comment = {}
        comment["text"] = input("Enter text:")
        while True:
            try:
                comment["id_post"]=int(input("Enter id_post:"))
                if comment["id_post"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                comment["id_user"]=int(input("Enter id_user:"))
                if comment["id_user"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                comment["id_parent_comment"]=int(input("Enter id_parent_comment or '0':"))
                if comment["id_parent_comment"]<0:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return comment

    def update_post(self):
        post = {}
        post["name"] = input("Enter name or nothing:")
        post["theme"] = input("Enter theme or nothing :")
        post["text"] = input("Enter text or nothing:")
        while True:
            try:
                post["rating"] = input("Enter rating or nothing:")
                if post["rating"]!="":
                    post["rating"]=int(post["rating"])
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return post

    def update_user(self):
        user = {}
        user["name"] = input("Enter name or nothing:")
        user["login"] = input("Enter login or nothing:")
        user["password"] = input("Enter password or nothing:")
        user["status"] = input("Enter status or 'NULL' or nothing:")
        user["admin"] = input("Enter admin or 'NULL' or nothing:")
        return user

    def update_comment(self):
        comment = {}
        comment["text"] = input("Enter text or nothing:")
        while True:
            try:
                comment["rating"] = input("Enter rating or nothing:")
                if  comment["rating"] != "":
                    comment["rating"] = int(comment["rating"])
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return comment

    def get_user_theme_and_rating_more(self):
        user={}
        user["name"] = input("Enter name:")
        user["theme"] = input("Enter theme:")
        while True:
            try:
                user["rating"]=int(input("Enter rating:"))
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return user


    def get_post_admin_count_comment_name(self):
        post={}
        post["name"]=input("Enter name: ")
        while True:
            post["admin"]=input("Enter admin True or False:")
            if(post["admin"]!="True" and post["admin"]!="False"):
                print("You should enter boolean. Try again")
                continue
            break
        if(post["admin"]=="True"):
            post["admin"]=True
        else:
            post["admin"]=False
        while True:
            try:
                post["count"]=int(input("Enter count of comments:"))
                if post["count"]<0:
                    print("You should enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return post

    def get_post_count_sub_com_rat_theme(self):
        post={}
        post["theme"]=input("Enter theme: ")
        while True:
            try:
                post["count"]=int(input("Enter count of subscribers:"))
                if post["count"]<0:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                post["rating"]=int(input("Enter rating:"))
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return post

    def get_number_generate(self):
        number=0
        while True:
            try:
                number=int(input("Enter number for generate:"))
                if number<0:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return number

    def print_posts(self,posts):
        for post in posts:
            print("id:", post[0])
            print("name:", post[1])
            print("theme:", post[2])
            print("text:", post[3])
            print("rating:", post[4])
            print("id_user:", post[5])
            print("")

    def print_comments(self, comments):
        for comment in comments:
            print("id:", comment[0])
            print("text:", comment[1])
            print("rating:", comment[2])
            print("id_user:", comment[4])
            print("id_post",comment[3])
            print("")

    def print_users(self,users):
        for user in users:
            print("id:", user[0])
            print("login:", user[1])
            print("password:", user[2])
            print("name:", user[3])
            if user[4]:
                print("status:", user[4])
            if user[5]:
                print("admin:", user[5])
            print("")

    def print_correct(self,mes):
        print(mes)