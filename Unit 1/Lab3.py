class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def introduce(self):
        print(f"Hi, my name is {self.name}")

class Post:
    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author

    def show_post(self):
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Author: {self.author}")

user1 = User("Carlos","carlos@email.com")

post1 = Post(
    "My first post",
    "I am learning Python!",
    user1
)


print(post1.author.name)