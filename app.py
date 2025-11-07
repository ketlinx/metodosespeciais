class Livro:
    def __init__(self,titulo,autor,ano):
       self.titulo = titulo
       self.autor = autor
       self.ano = ano
    def __eq__(self, value):
        return self.titulo == value.titulo and self.autor == value.autor and self.ano==value.ano
livro1 = Livro("Python para Todos", "John Doe", 2024)
livro2 = Livro("Python para Todos", "John Doe", 2024)
livro3 = Livro("aprendendo python", "John Doe", 2021)
livro4 = Livro("java essencial", "maria silva", 2019)

print(livro1 == livro2)  
print(livro2 == livro3)  
print(livro1 == livro1)  
print(id(livro1))
print(id(livro2))
print(id(livro3))
print(livro1 is livro1)