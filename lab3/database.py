import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, exc,and_,or_
from sqlalchemy.orm import sessionmaker
from models import Post, User, Comment, parent_comments, subscription

class DB:

    def __init__(self):
        self.s = None

    def open(self):
        try:
            DATABASE_URI = 'postgres+psycopg2://postgres:16072002p@localhost:5432/lab1'
            engine = create_engine(DATABASE_URI)
            Session = sessionmaker(bind=engine)
            self.s = Session()
            print("Connect")
        except (Exception, exc.SQLAlchemyError) as error:
            print("Can`t connect to data base", error)

    def close(self):
        self.s.close()

    def find_post(self, name):
        try:
            posts=self.s.query(Post).filter_by(name=name).all()
            print(posts)
            if posts:
                return posts
            else:
                return "Can`t find posts by name"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_post():", error)

    def find_post_by_id(self, id):
        try:
            post=self.s.query(Post).get(id)
            self.s.commit()
            if post:
                return post
            else:
                return "Can`t find posts by id"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_post_by_id():", error)

    def find_user_posts(self, id_user):
        try:
            posts = self.s.query(Post).filter_by(id_user=id_user).all()
            self.s.commit()
            if posts:
                return posts
            else:
                return "Can`t find user`s post"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_user_post():", error)

    def find_user_comments(self, id_user):
        try:
            comments = self.s.query(Comment).filter_by(id_user=id_user).all()
            self.s.commit()
            if comments:
                return comments
            else:
                return "Can`t find user`s comments"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_user_comments():", error)

    def find_comment(self, id_comment):
        try:
            comment = self.s.query(Comment).get(id_comment)
            self.s.commit()
            if comment:
                return comment
            else:
                return "Can`t find comment by id"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_comment():", error)

    def find_user(self, name):
        try:
            users = self.s.query(User).filter_by(name=name).all()
            self.s.commit()
            if users:
                return users
            else:
                return "Can`t find user by name"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_user():", error)

    def find_user_by_id(self, id):
        try:
            user = self.s.query(User).get(id)
            self.s.commit()
            if user:
                return user
            else:
                return "Can`t find user by id"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_user_by_id():", error)


    def find_subscribers(self, id_user):
        try:
            subscribers=self.s.query(User).join(subscription, subscription.c.id_subscriber==User.id).filter_by(id_user=id_user).all()
            self.s.commit()
            if subscribers:
                return subscribers
            else:
                return "Can`t find subscribers by id_user"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_subscriber():", error)


    def find_subscribes(self, id_user):
        try:
            subscribes = self.s.query(User).join(subscription, subscription.c.id_user == User.id).filter_by(id_subscriber=id_user).all()
            self.s.commit()
            if subscribes:
                return subscribes
            else:
                return "Can`t find subscribes by id_user"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_subscriber():", error)

    def find_post_comments(self, id_post):
        try:
            comments = self.s.query(Comment).filter_by(id_post=id_post).all()
            self.s.commit()
            if comments:
                return comments
            else:
                return "Can`t find post`s comments"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_post_comments():", error)

    def find_all_posts(self):
        try:
            posts = self.s.query(Post).all()
            self.s.commit()
            if posts:
                return posts
            else:
                return "Can`t find posts"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_all_posts():", error)

    def find_all_users(self):
        try:
            users = self.s.query(User).all()
            self.s.commit()
            if users:
                return users
            else:
                return "Can`t find users"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_all_users():", error)

    def find_all_comments(self):
        try:
            comments = self.s.query(Comment).all()
            self.s.commit()
            if comments:
                return comments
            else:
                return "Can`t find comments"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_all_comments():", error)

    def add_comment(self, id_post2, id_user2, text2, id_parent_comment=0):
        try:
            comment=Comment(
            text = text2,
            rating=0,
            id_user = id_user2,
            id_post = id_post2
            )
            self.s.add(comment)
            self.s.commit()
            last_id = comment.id
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in add_comment() first step:", error)
        if id_parent_comment != 0:
            try:
                p_comments=self.s.query(parent_comments).filter_by(id_child=id_parent_comment).first()
                self.s.commit()
                if p_comments:
                    return "Add is successful, but can`t add parent_comment"
            except (Exception, exc.SQLAlchemyError) as error:
                self.s.rollback()
                print("Error in add_comment() second step:", error)
            try:
                p_com=parent_comments.insert().values(id_parent=id_parent_comment,id_child=last_id)
                self.s.execute(p_com)
                self.s.commit()
            except (Exception, exc.SQLAlchemyError) as error:
                self.s.rollback()
                print("Error in add_comment() third step:", error)
        else:
            return "Add is successful"

    def add_user(self, login, password, name, status=None, admin=None):
        try:
            user=User(
            login=login,
            password = password,
            name = name,
            status = status,
            admin = admin
            )
            self.s.add(user)
            self.s.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in add_user():", error)
        return "Add is successful"

    def add_post(self, name, text, id_user, theme):
        try:
            post=Post(
            name=name,
            theme = theme,
            text = text,
            rating = 0,
            id_user = id_user
            )
            self.s.add(post)
            self.s.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in add_post():", error)
        return "Add is successful"

    def subscribe(self, id_user, id_subscriber):
        try:
            subs = self.s.query(parent_comments).filter_by(id_user=id_user).filter_by(id_subscriber=id_subscriber).first()
            self.s.commit()
            if subs:
                return "Can`t subscribe"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in subscribe() first step:", error)
        try:
            sub = subscription.insert().values(id_user=id_user, id_subscriber=id_subscriber)
            self.s.execute(sub)
            self.s.commit()
        except (Exception, psycopg2.Error) as error:
            self.s.rollback()
            print("Error in subscribe() second step:", error)
        return "Add is successful"

    def update_user(self, id, login, password, name, status, admin):
        try:
            u=self.s.query(User).filter_by(id=id).update({User.name:name,User.login:login,User.password:password,User.status:status,User.admin:admin})
            self.s.commit()
            if u:
                return "Update user is successful"
            else:
                return "Can`t update user"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in update_user():", error)
        return "Update is successful"

    def update_comment(self, id, text, rating):
        try:
            c = self.s.query(Comment).filter_by(id=id).update(
                {Comment.text:text,Comment.rating:rating})
            self.s.commit()
            if c:
                return "Update comment is successful"
            else:
                return "Can`t update comment"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in update_comment():", error)

    def update_post(self, id, name, text, theme, rating):
        try:
            p = self.s.query(Post).filter_by(id=id).update(
                {Post.text: text, Post.rating: rating,Post.name:name,Post.theme:theme})
            self.s.commit()
            if p:
                return "Update post is successful"
            else:
                return "Can`t update post"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in update_post():", error)

    def remove_comment(self, id):
        try:
            comment=self.find_comment(id)
            if type(comment) is not Comment:
                return "Can`t find id"
            c=self.s.delete(comment)
            self.s.commit()
            return "Delete is successful"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in remove_comment() second step:", error)

    def remove_post(self, id):
        try:
            post=self.find_post_by_id(id)
            if type(post) is not Post:
                return "Can`t find id"
            c = self.s.delete(post)
            self.s.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in remove_post():", error)
        return "Delete is successful"

    def remove_user(self, id):
        try:
            user=self.find_user_by_id(id)
            if type(user) is not User:
                return "Can`t find id"
            c = self.s.delete(user)
            self.s.commit()
            return "Delete is correct"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in remove_user() third step:", error)

    def remove_subscriber(self, id_user, id_subscriber):
        try:
            c=subscription.delete().where(subscription.c.id_user==id_user).where(subscription.c.id_subscriber==id_subscriber)
            self.s.execute(c)
            self.s.commit()
            return "Delete is correct"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in remove_subscriber():", error)

    def find_user_theme_and_rating_more(self, theme, rating, name):
        users=0
        try:
            users=self.s.execute(
                f"select * from users where id=(select id_user from posts where theme='{theme}' and rating>'{rating}') and name LIKE '%{name}%';")
            self.s.commit()
            if not users:
                return "Can`t find"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_user_theme_and_rating_more():", error)
        return users

    def find_admin_count_comment_name(self, admin, count, name):
        posts=0
        try:
            if admin:
                posts=self.s.execute(
                    f"select * from posts natural join(select id_post as id from comments natural join (select id as id_post from posts natural join(select id as id_user from users where admin IS NOT NULL)t1)t2 group by id_post having count(id)>'{count}')t3  WHERE name LIKE '%{name}%'")
                self.s.commit()
            else:
                posts=self.s.execute(
                    f"select * from posts natural join(select id_post as id from comments natural join (select id as id_post from posts natural join(select id as id_user from users where admin IS NULL)t1)t2 group by id_post having count(id)>'{count}')t3  WHERE name LIKE '%{name}%'")
                self.s.commit()
            if not posts:
                return "Can`t find"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_admin_count_comment_name():", error)
        return posts

    def find_post_count_sub_com_rat_theme(self, sub, rating, theme):
        posts=0
        try:
            posts=self.s.execute(
                f"select * from posts natural join (select distinct id_post as id from comments natural join (select id_user from subscription group by id_user having count(id_subscriber)>'{sub}')t1 where rating >'{rating}')t2 where theme like '%{theme}%'")
            self.s.commit()
            if not posts:
                return "Can`t find"
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_post_count_sub_com_rat_theme():", error)
        return posts

    def generate_comments(self, number):
        try:
            self.s.execute(
                f"Insert into comments (text,rating,id_post,id_user) SELECT  rnd.text,rnd.rating, rnd.id_post,rnd.id_user FROM (SELECT md5(random()::text)as text,trunc(random()*(2001)-1000)::integer as rating,posts.id as id_post,users.id as id_user FROM   generate_series(1, 1000),users,posts ORDER BY random() limit '{number}') as rnd")
            self.connect.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in generate_comments():", error)
            return "Generated"

    def generate_users(self, number):
        try:
            self.s.execute(
                f"Insert into users (login,password,name,status,admin) SELECT  rnd.login,rnd.password,rnd.name,rnd.status,rnd.admin FROM (SELECT md5(random()::text) ||'@gmail.com' as login, md5(random()::text) as password, (array['Nastya','Polina','Oleksandr','Anna','Dmytriy','Nazar','Varvara'])[trunc(random()*7)+1] as name,(array[NULL, md5(random()::text)])[trunc(random()*2)+1] as status,(array[NULL, md5(random()::text)])[trunc(random()*2)+1] as admin FROM   generate_series(1, '{number}') g)  as rnd")
            self.s.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in generate_users():", error)
        return "Generated"

    def generate_subscription(self, number):
        try:
            self.s.execute(
                f"INSERT INTO subscription(id_user,id_subscriber)SELECT  rnd.id_user,rnd.id_subscriber FROM (select users.id as id_subscriber,u.id as id_user FROM   users, users as u) as rnd left join subscription on (rnd.id_user=subscription.id_user and rnd.id_subscriber=subscription.id_subscriber) where rnd.id_user!= rnd.id_subscriber  and subscription.id is NULL ORDER BY random() LIMIT {number}")
            self.s.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in generate_subscription():", error)
        return "Generated"

    def generate_parent_comments(self, number):
        try:
            self.s.execute(
                f"insert into parent_comments (id_parent,id_child) SELECT distinct on (rnd.id_child) rnd.id_parent, rnd.id_child FROM (select comments.id as id_parent,c.id as id_child FROM   comments, comments as c where c.id_post=comments.id_post and EXISTS(select * from parent_comments p where comments.id=p.id_child)=False and EXISTS(select * from parent_comments p where c.id=p.id_parent or c.id=p.id_child)=False) as rnd left join parent_comments on (rnd.id_parent=parent_comments.id_parent and rnd.id_child=parent_comments.id_child) where rnd.id_parent!= rnd.id_child  and parent_comments.id is NULL ORDER BY random() limit {number}")
            self.s.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in generate_parent_comments():", error)
        return "Generated"

    def generate_posts(self, number):
        try:
            self.s.execute(
                f"Insert into posts (name,theme,text,rating,id_user) SELECT  rnd.name,rnd.theme,rnd.text,rnd.rating,id_user FROM (SELECT md5(random()::text) as text, md5(random()::text) as theme, md5(random()::text)as name,trunc(random()*2001-1000) as rating, users.id as id_user FROM   users, generate_series(1, 1000) g)  as rnd ORDER BY random() limit {number}")
            self.s.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in generate_posts():", error)
        return "Generated"