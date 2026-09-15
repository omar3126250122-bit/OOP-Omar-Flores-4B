import re

class User:
    def __init__(self,nombre,correo,telefono,password):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.__password = password

    def Login(self):
        print(f"Sesion iniciada correctamente con el usuario {self.nombre}")

    def create_post(self,post):
        self.post = post
        print(f"El usuario: {post.user} posteo {post.descripcion}\nDATOS:\nFecha: {post.fecha}")

    def comentar(self,post):
        print(f"Comentario publicado correctamente\nDATOS:\nUSER:{post.user}\nDESCRIPCION:{post.descripcion}\nDATE:{post.date}")

    def GetPassword(self):
        return self.__password

    def SetPassword(self,password):
        exp1 = r'^[A-za-z0-9]{4,100}' 
        if re.match(exp1,password):
            self.__password = password

class Post:
    def __init__(self,user,fecha,descripcion):
        self.user = user
        self.fecha = fecha
        self.descripcion = descripcion

class Comments:
    def __init__(self,user,descripcion,date):
        self.user = user
        self.descripcion = descripcion
        self.date = date

    def comentar(self):
        print(f"Comentario publicado correctamente\nDATOS:\nUSER:{self.user}\nDESCRIPCION:{self.descripcion}\nDATE:{self.date}")

class Message:
    def __init__(self,userE,userR,mensaje,date):
        self.userE = userE
        self.userR = userR
        self.mensaje = mensaje
        self.date = date
    def dm(self):
        print(f"Mensaje enviado correctamente\nDATOS:\nUSER QUE ENVIA:{self.userE}\nUSER QUE RECIBE:{self.userR}\nTEXTO:{self.mensaje}\nDATE:{self.date}")

user1 = User("Omar","ac@gmail.com","6181234512","1234e")
user2 = User("Jaime","jaiem123@utd.edu.mx","1234567890","jaiemutd")
post1 = Post(user1.nombre,"12/09/2026","Post numero 1")
comment1= Comments(user2.nombre,"Me gusta la pagina","14/09/2026")
msj = Message(user1.nombre,user2.nombre,"Hola como estas","14/09/2026")

msj.dm()
user1.create_post(post1)
user2.comentar(comment1)