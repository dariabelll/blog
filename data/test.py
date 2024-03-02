from requests import get, post, delete

#print(get('http://localhost:8080/api/news').json())
#print(get('http://localhost:8080/api/news/1').json())

#print(get('http://localhost:8080/api/news/999').json())
#print(get('http://localhost:8080/api/news/q').json())


print(delete('http://localhost:8080/api/news/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:8080/api/news/1').json())
