import psycopg2


class DB:

    def __init__(self):
        self.connect =None
        self.cursor=None

    def open(self):
        try:
            self.connect =psycopg2.connect(user="postgres", password="16072002p", host="localhost", port="5432", database="lab1")
            self.cursor =self.connect.cursor()
            print("Connect")
        except (Exception,psycopg2.Error) as error:
            print("Can`t connect to data base",error)

    def close(self):
        if self.connect:
            self.cursor.close()
            self.connect.close()

    def find_post(self,name):
        try:
            self.cursor.execute(f"Select * from posts where name='{name}';")
            self.connect.commit()
            posts=self.cursor.fetchall()
            if posts:
                return posts
            else:
                return "Can`t find posts by name"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_post():", error)

    def find_post_by_id(self, id):
        try:
            self.cursor.execute(f"Select * from posts where id= {id};")
            self.connect.commit()
            posts=self.cursor.fetchall()
            if posts:
                return posts
            else:
                return "Can`t find posts by id"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_post_by_id():", error)

    def find_user_posts(self,id_user):
        try:
            self.cursor.execute(f"Select * from posts where id_user= {id_user};")
            self.connect.commit()
            posts=self.cursor.fetchall()
            if posts:
                return posts
            else:
                return "Can`t find user`s post"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_user_post():", error)

    def find_user_comments(self,id_user):
        try:
            self.cursor.execute(f"Select * from comments where id_user= {id_user};")
            self.connect.commit()
            comments=self.cursor.fetchall()
            if comments:
                return comments
            else:
                return "Can`t find user`s comments"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_user_comments():", error)

    def find_comment(self,id_comment):
        try:
            self.cursor.execute(f"Select * from comments where id= {id_comment};")
            self.connect.commit()
            comments=self.cursor.fetchall()
            if comments:
                return comments
            else:
                return "Can`t find comment by id"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_comment():", error)

    def find_user(self,name):
        try:
            self.cursor.execute(f"Select * from users where name= '{name}';")
            self.connect.commit()
            users=self.cursor.fetchall()
            if users:
                return users
            else:
                return "Can`t find user by name"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_user():", error)

    def find_user_by_id(self,id):
        try:
            self.cursor.execute(f"Select * from users where id= {id};")
            self.connect.commit()
            users=self.cursor.fetchall()
            if users:
                return users
            else:
                return "Can`t find user by id"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_user_by_id():", error)

    def find_subscribers(self,id_user):
        try:
            self.cursor.execute(f"select * from users,subscription where users.id=subscription.id_subscriber and subscription.id_user={id_user};")
            self.connect.commit()
            subscribers=self.cursor.fetchall()
            if subscribers:
                return subscribers
            else:
                return "Can`t find subscribers by id_user"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_subscriber():", error)

    def find_subscribes(self,id_user):
        try:
            self.cursor.execute(f"select * from users,subscription where users.id=subscription.id_user and subscription.id_subscriber={id_user};")
            self.connect.commit()
            subscribes=self.cursor.fetchall()
            if subscribes:
                return subscribes
            else:
                return "Can`t find subscribes by id_user"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_subscriber():", error)

    def find_post_comments(self,id_post):
        try:
            self.cursor.execute(f"select * from comments where id_post={id_post};")
            self.connect.commit()
            comments=self.cursor.fetchall()
            if comments:
                return comments
            else:
                return "Can`t find post`s comments"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_post_comments():", error)

    def find_all_posts(self):
        try:
            self.cursor.execute(f"select * from posts;")
            self.connect.commit()
            posts=self.cursor.fetchall()
            if posts:
                return posts
            else:
                return "Can`t find posts"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_all_posts():", error)

    def find_all_users(self):
        try:
            self.cursor.execute(f"select * from users;")
            self.connect.commit()
            users=self.cursor.fetchall()
            if users:
                return users
            else:
                return "Can`t find users"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_all_users():", error)

    def find_all_comments(self):
        try:
            self.cursor.execute(f"select * from comments;")
            self.connect.commit()
            comments=self.cursor.fetchall()
            if comments:
                return comments
            else:
                return "Can`t find comments"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_all_comments():", error)

    def add_comment(self,id_post,id_user,text,id_parent_comment=0):
        try:
            self.cursor.execute(f"insert into comments (id_post,id_user,text,rating) VAlUES({id_post},{id_user},'{text}',0) RETURNING id;")
            self.connect.commit()
            last_id = self.cursor.fetchone()[0]
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in add_comment() first step:", error)
        if id_parent_comment!=0:
            try:
                self.cursor.execute(f"Select * from parent_comments where id_child={id_parent_comment} ")
                self.connect.commit()
                if self.cursor.fetchall():
                    return "Add is successful, but can`t add parent_comment"
            except (Exception, psycopg2.Error) as error:
                self.connect.rollback()
                print("Error in add_comment() second step:", error)
            try:
                self.cursor.execute(f"insert into parent_comments (id_parent,id_child) VAlUES({id_parent_comment},{last_id}) ;")
                self.connect.commit()
            except (Exception, psycopg2.Error) as error:
                self.connect.rollback()
                print("Error in add_comment() third step:", error)
        else:
            return "Add is successful"

    def add_user(self,login,password,name,status='NULL',admin='NULL'):
        try:
            self.cursor.execute(f"insert into users (login,password,name,admin,status) VAlUES('{login}','{password}','{name}',{admin},'{status}') ;")
            self.connect.commit()
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in add_user():", error)
        return "Add is successful"

    def add_post(self,name,text,id_user,theme):
        try:
            self.cursor.execute(f"insert into posts (name,text,id_user,rating,theme) VAlUES('{name}','{text}','{id_user}',0,'{theme}') ;")
            self.connect.commit()
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in add_post():", error)
        return "Add is successful"

    def subscribe(self,id_user,id_subscriber):
        try:
            self.cursor.execute(f"select * from subscription where id_user={id_user} and id_subscriber={id_subscriber};")
            self.connect.commit()
            if self.cursor.fetchall():
                return "Can`t subscribe"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in subscribe() first step:", error)
        try:
            self.cursor.execute(f"insert into subscription (id_user,id_subscriber) VAlUES('{id_user}',{id_subscriber}) ;")
            self.connect.commit()
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in subscribe() second step:", error)
        return"Add is successful"

    def update_user(self, id, login, password, name, status, admin):
        try:
            self.cursor.execute(f"update users set login='{login}',password='{password}',name='{name}',admin='{admin}',status='{status}' where id={id} ;")
            self.connect.commit()
            if self.cursor.rowcount:
                return "Update user is successful"
            else:
                return "Can`t update user"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in update_user():", error)
        return "Update is successful"

    def update_comment(self, id, text, rating):
        try:
            self.cursor.execute(f"update comments set text='{text}',rating='{rating}' where id={id} ;")
            self.connect.commit()
            if self.cursor.rowcount:
                return "Update comment is successful"
            else:
                return "Can`t update comment"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in update_comment():", error)

    def update_post(self, id, name, text, theme, rating):
        try:
            self.cursor.execute(f"update posts set name='{name}',text='{text}',rating='{rating},theme='{theme}' where id='{id}';")
            self.connect.commit()
            if self.cursor.rowcount:
                return "Update post is successful"
            else:
                return "Can`t update post"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in update_post():", error)

    def remove_comment(self,id):
        try:
            self.cursor.execute(f"delete from parent_comments where id_parent='{id}' or id_child='{id}'")
            self.connect.commit()
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in remove_comment() first step:", error)
        try:
            self.cursor.execute(f"delete from comments where id='{id}'")
            self.connect.commit()
            if self.cursor.rowcount:
                return "Delete is successful"
            else:
                return "Can`t delete"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in remove_comment() second step:", error)

    def remove_post(self,id):
        comments=0
        try:
            self.cursor.execute(f"select id from comments where id_post='{id}'")
            self.connect.commit()
            comments = self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in subscribe() second step:", error)
        if comments:
            for row in comments:
                self.remove_comment(row[0])
        try:
            self.cursor.execute(f"delete from posts where id='{id}'")
            self.connect.commit()
            if not self.cursor.rowcount:
                return "Can`t delete post"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in subscribe() second step:", error)
        return "Delete is successful"

    def remove_user(self,id):
        try:
            self.cursor.execute(f"select id from posts where id_user='{id}'")
            self.connect.commit()
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in remove_user() first step:", error)
        posts = self.cursor.fetchall()
        if posts:
            for row in posts:
                self.remove_post(row[0])
        try:
            self.cursor.execute(f"select id from comments where id_user='{id}'")
            self.connect.commit()
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in remove_user() second step:", error)
        comments = self.cursor.fetchall()
        if comments:
            for row in comments:
             self.remove_comment(row[0])
        try:
            self.cursor.execute(f"delete from users where id='{id}'")
            self.connect.commit()
            if self.cursor.rowcount:
                return "Delete is correct"
            else:
                return "Can`t delete"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in remove_user() third step:", error)

    def remove_subscriber(self,id_user,id_subscriber):
        try:
            self.cursor.execute(f"delete from subscription where id_user='{id_user}' and id_subscriber='{id_subscriber}'")
            self.connect.commit()
            if self.cursor.fetchall():
                return "Delete is correct"
            else:
                return "Can`t delete"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in remove_subscriber():", error)

    def find_user_theme_and_rating_more(self,theme,rating,name):
        try:
            self.cursor.execute(f"select * from users where id=(select id_user from posts where theme='{theme}' and rating>'{rating}') and name LIKE '%{name}%';")
            self.connect.commit()
            users=self.cursor.fetchall()
            if not users:
                return"Can`t find"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_user_theme_and_rating_more():", error)
        return users

    def find_admin_count_comment_name(self,admin,count,name):
        try:
            if admin:
                self.cursor.execute(f"select * from posts natural join(select id_post as id from comments natural join (select id as id_post from posts natural join(select id as id_user from users where admin IS NOT NULL)t1)t2 group by id_post having count(id)>'{count}')t3  WHERE name LIKE '%{name}%'")
                self.connect.commit()
                posts = self.cursor.fetchall()
            else:
                self.cursor.execute(f"select * from posts natural join(select id_post as id from comments natural join (select id as id_post from posts natural join(select id as id_user from users where admin IS NULL)t1)t2 group by id_post having count(id)>'{count}')t3  WHERE name LIKE '%{name}%'")
                self.connect.commit()
                posts = self.cursor.fetchall()
            if not posts:
                return "Can`t find"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_admin_count_comment_name():", error)
        return posts
    
    def find_post_count_sub_com_rat_theme(self,sub,rating,theme):
        try:
            self.cursor.execute(f"select * from posts natural join (select distinct id_post as id from comments natural join (select id_user from subscription group by id_user having count(id_subscriber)>'{sub}')t1 where rating >'{rating}')t2 where theme like '%{theme}%'")
            self.connect.commit()
            posts = self.cursor.fetchall()
            if not posts:
                return "Can`t find"
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in find_post_count_sub_com_rat_theme():", error)
        return posts

    def generate_comments(self,number):
        try:
            self.cursor.execute(f"Insert into comments (text,rating,id_post,id_user) SELECT  rnd.text,rnd.rating, rnd.id_post,rnd.id_user FROM (SELECT md5(random()::text)as text,trunc(random()*(2001)-1000)::integer as rating,posts.id as id_post,users.id as id_user FROM   generate_series(1, 1000),users,posts ORDER BY random() limit '{number}') as rnd")
            self.connect.commit()
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in generate_comments():", error)
            return"Generated"

    def generate_users(self, number):
        try:
            self.cursor.execute(f"Insert into users (login,password,name,status,admin) SELECT  rnd.login,rnd.password,rnd.name,rnd.status,rnd.admin FROM (SELECT md5(random()::text) ||'@gmail.com' as login, md5(random()::text) as password, (array['Nastya','Polina','Oleksandr','Anna','Dmytriy','Nazar','Varvara'])[trunc(random()*7)+1] as name,(array[NULL, md5(random()::text)])[trunc(random()*2)+1] as status,(array[NULL, md5(random()::text)])[trunc(random()*2)+1] as admin FROM   generate_series(1, '{number}') g)  as rnd")
            self.connect.commit()
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in generate_users():", error)
        return "Generated"


    def generate_subscription(self,number):
        try:
            self.cursor.execute(f"INSERT INTO subscription(id_user,id_subscriber)SELECT  rnd.id_user,rnd.id_subscriber FROM (select users.id as id_subscriber,u.id as id_user FROM   users, users as u) as rnd left join subscription on (rnd.id_user=subscription.id_user and rnd.id_subscriber=subscription.id_subscriber) where rnd.id_user!= rnd.id_subscriber  and subscription.id is NULL ORDER BY random() LIMIT {number}")
            self.connect.commit()
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in generate_subscription():", error)
        return "Generated"

    def generate_parent_comments(self,number):
        try:
            self.cursor.execute(f"insert into parent_comments (id_parent,id_child) SELECT distinct on (rnd.id_child) rnd.id_parent, rnd.id_child FROM (select comments.id as id_parent,c.id as id_child FROM   comments, comments as c where c.id_post=comments.id_post and EXISTS(select * from parent_comments p where comments.id=p.id_child)=False and EXISTS(select * from parent_comments p where c.id=p.id_parent or c.id=p.id_child)=False) as rnd left join parent_comments on (rnd.id_parent=parent_comments.id_parent and rnd.id_child=parent_comments.id_child) where rnd.id_parent!= rnd.id_child  and parent_comments.id is NULL ORDER BY random() limit {number}")
            self.connect.commit()
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in generate_parent_comments():", error)
        return "Generated"

    def generate_posts(self,number):
        try:
            self.cursor.execute(f"Insert into posts (name,theme,text,rating,id_user) SELECT  rnd.name,rnd.theme,rnd.text,rnd.rating,id_user FROM (SELECT md5(random()::text) as text, md5(random()::text) as theme, md5(random()::text)as name,trunc(random()*2001-1000) as rating, users.id as id_user FROM   users, generate_series(1, 1000) g)  as rnd ORDER BY random() limit {number}")
            self.connect.commit()
        except (Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("Error in generate_posts():", error)
        return "Generated"