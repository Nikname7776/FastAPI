##### ♦ FastAPI – создание пользователя с занесением в sqlite, аутентификация пользователя по email + password, методы для работы с блогами аутентифицированных пользователей с занесением в sqlite.

Переход в swagger [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
##### Блок Users ->
* POST:

 {

"name": "Danika",

"email": "strongwomen@mail.com",

"password": "qwerty123"

}

* GET:
Id: ``1``
##### Authorize ->
Username: `` strongwomen@mail.com``
Password: `` qwerty123``

* Authentication:

Username: ``strongwomen@mail.com``

Password: ``qwerty123``

Response

Status 200

{

"access_token": "*****",

"token_type": "bearer"

}

##### Блок Blogs ->

* POST:

*

{

"title": "Harry Potter",

"body": " Harry Potter and the Half-Blood Prince"

}
