from database import DB
from View import View
import time
database = DB()
database.open()

view = View()
choice=0
while choice!='33':
    choice=view.print_menu()
    if choice=='1':
        name = view.get_name()
        posts = database.find_post(name)
        if type(posts) is str:
            view.print_correct(posts)
        else:
            view.print_posts(posts)
            view.print_correct("Find is successful")
    if choice=='2':
        id = view.get_id()
        posts = database.find_post_by_id(id)
        if type(posts) is str:
            view.print_correct(posts)
        else:
            view.print_posts(posts)
            view.print_correct("Find is successful")
    if choice=='3':
        user_id = view.get_id()
        posts = database.find_user_posts(user_id)
        if type(posts) is str:
            view.print_correct(posts)
        else:
            view.print_posts(posts)
            view.print_correct("Find is successful")
    if choice=='4':
        user_id = view.get_id()
        comments = database.find_user_comments(user_id)
        if type(comments) is str:
            view.print_correct(comments)
        else:
            view.print_comments(comments)
            view.print_correct("Find is successful")
    if choice=='5':
        id = view.get_id()
        comments = database.find_comment(id)
        if type(comments) is str:
            view.print_correct(comments)
        else:
            view.print_comments(comments)
            view.print_correct("Find is successful")
    if choice=='6':
        id = view.get_id()
        users = database.find_user_by_id(id)
        if type(users) is str:
            view.print_correct(users)
        else:
            view.print_users(users)
            view.print_correct("Find is successful")
    if choice=='7':
        name = view.get_name()
        users = database.find_user(name)
        if type(users) is str:
            view.print_correct(users)
        else:
            view.print_users(users)
            view.print_correct("Find is successful")
    if choice=='8':
        user_id = view.get_id()
        users = database.find_subscribers(user_id)
        if type(users) is str:
            view.print_correct(users)
        else:
            view.print_users(users)
            view.print_correct("Find is successful")
    if choice =='9':
        user_id = view.get_id()
        users = database.find_subscribes(user_id)
        if type(users) is str:
            view.print_correct(users)
        else:
            view.print_users(users)
            view.print_correct("Find is successful")
    if choice =='10':
        id = view.get_id()
        comments = database.find_post_comments(user_id)
        if type(comments) is str:
            view.print_correct(comments)
        else:
            view.print_comments(comments)
            view.print_correct("Find is successful")
    if choice == '11':
        posts = database.find_all_posts()
        if type(posts) is str:
            view.print_correct(posts)
        else:
            view.print_posts(posts)
            view.print_correct("Find is successful")
    if choice == '12':
        users = database.find_all_users()
        if type(users) is str:
            view.print_correct(users)
        else:
            view.print_users(users)
            view.print_correct("Find is successful")
    if choice == '13':
        comments = database.find_all_comments()
        if type(comments) is str:
            view.print_correct(comments)
        else:
            view.print_comments(comments)
            view.print_correct("Find is successful")
    if choice == '14':
        post=view.add_post()
        mes=database.add_post(post["theme"],post["name"],post["text"],post["id_user"],post["theme"])
        view.print_correct(mes)
    if choice == '15':
        user = view.add_user()
        mes = database.add_user(user["login"], user["password"], user["name"], user["status"], user["admin"])
        view.print_correct(mes)
    if choice == '16':
        comment = view.add_comment()
        mes = database.add_comment(user["id_post"], user["id_user"], user["text"],  user["id_parent_comment"])
        view.print_correct(mes)
    if choice == '17':
        id=view.get_subscribe()
        mes = database.subscribe(id["user"],id["subscriber"])
        view.print_correct(mes)
    if choice == '18':
        id=view.get_id()
        user=view.update_user()
        user_old = database.find_user_by_id(id)
        if not user["name"]:
            user["name"]=user_old[0][3]
        if not user["login"]:
            user["login"]=user_old[0][1]
        if not user["password"]:
            user["password"]=user_old[0][2]
        if not user["status"]:
            user["status"]=user_old[0][4]
        if not user["admin"]:
            user["admin"]=user_old[0][5]
        mes=database.update_user(id,user["login"],user["password"],user["name"],user["status"],user["admin"])
        view.print_correct(mes)

    if choice == '19':
        id = view.get_id()
        comment = view.update_comment()
        com_old = database.find_comment(id)
        if not comment["text"]:
            comment["text"] = com_old[0][1]
        if comment["rating"]=="":
            comment["rating"] = com_old[0][2]
        mes=database.update_comment(id,comment["text"],comment["rating"])
        view.print_correct(mes)

    if choice == '20':
        id = view.get_id()
        post = view.update_post()
        post_old = database.find_post_by_id(id)
        if not post["name"]:
            post["name"] = post_old[0][1]
        if not post["theme"]:
            post["theme"] = post_old[0][2]
        if not post["text"]:
            post["text"] = post_old[0][3]
        if post["rating"] == "":
            post["rating"] = post_old[0][4]
        mes = database.update_post(id, post["name"],post["text"],post["theme"],post["rating"])
        view.print_correct(mes)
    if choice == '21':
        id=view.get_id()
        mes=database.remove_user(id)
        view.print_correct(mes)
    if choice == '22':
        id = view.get_id()
        mes = database.remove_comment(id)
        view.print_correct(mes)
    if choice == '23':
        id = view.get_id()
        mes = database.remove_post(id)
        view.print_correct(mes)
    if choice == '24':
        id = view.get_subscribe()
        mes = database.remove_subscriber(id["user"],id["subscriber"])
        view.print_correct(mes)
    if choice == '25':
        users=view.get_user_theme_and_rating_more()
        u=database.find_user_theme_and_rating_more(users["theme"],users["rating"],users["name"])
        if type(u) is str:
            view.print_correct(u)
        else:
            view.print_users(u)
            view.print_correct("Find is successful")
    if choice == '26':
        posts=view.get_post_admin_count_comment_name()
        p=database.find_admin_count_comment_name(posts["admin"],posts["count"],posts["name"])
        if type(p) is str:
            view.print_correct(p)
        else:
            view.print_posts(p)
            view.print_correct("Find is successful")
    if choice == '27':
        posts=view.get_post_count_sub_com_rat_theme()
        p=database.find_post_count_sub_com_rat_theme(posts["count"],posts["rating"],posts["theme"])
        if type(p) is str:
            view.print_correct(p)
        else:
            view.print_posts(p)
            view.print_correct("Find is successful")
    if choice == '28':
        number=view.get_number_generate()
        start = time.time()
        mes=database.generate_comments(number)
        finish=time.time()
        dif2 = str(finish - start)
        print(type(dif2))
        dif = mes + "   time:" + dif2
        view.print_correct(dif)

    if choice == '29':
        number = view.get_number_generate()
        start = time.time()
        mes = database.generate_users(number)
        finish = time.time()
        dif2 = str(finish - start)
        print(type(dif2))
        dif = mes + "   time:" + dif2
        view.print_correct(dif)
    if choice == '30':
        number = view.get_number_generate()
        start = time.time()
        mes = database.generate_subscription(number)
        finish = time.time()
        dif2 = str(finish - start)
        print(type(dif2))
        dif = mes + "   time:" + dif2
        view.print_correct(dif)
    if choice == '31':
        number = view.get_number_generate()
        start = time.time()
        mes = database.generate_parent_comments(number)
        finish = time.time()
        dif2 = str(finish - start)
        print(type(dif2))
        dif = mes + "   time:" + dif2
        view.print_correct(dif)
    if choice == '32':
        number = view.get_number_generate()
        start = time.time()
        mes = database.generate_posts(number)
        view.print_correct(mes)
        finish = time.time()
        dif2 = str(finish - start)
        print(type(dif2))
        dif = mes+ "   time:" + dif2
        view.print_correct(dif)


database.close()
