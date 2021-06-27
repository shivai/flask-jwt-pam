# flask-jwt-pam

When it comes to using JWT without hardcoding the credential or storing it in a database, pam commences. Yes, we can use OS users and let the rest to the OS!

How to test:

```
$ python main.py

```

Then send a curl request like this:

```
curl -X POST http://127.0.0.1:5000/auth -H "Content-Type: application/json" -d '{"username": "MY_USERNAME", "password":"MY_PASSWORD"}'

```
The output would be like this:

```
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjQ4MTI4MTAsImlhdCI6MTYyNDgxMjUxMCwibmJmIjoxNjI0ODEyNTEwLCJpZGVudGl0eSI6IjNlMGZiNWMzLTA0ZjEtNGJjNi1iMzNlLTYyMzI1NGM3MDIxNSJ9.j6qczVTbVz3dQAjDd9g0iNSLeFvxS1GXSD97tg20h60"
}

```

Now you can access to the protected endpoint:

```
curl -X GET http://127.0.0.1:5000/protected -H "Content-Type: application/json" -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjQ4MTI4MTAsImlhdCI6MTYyNDgxMjUxMCwibmJmIjoxNjI0ODEyNTEwLCJpZGVudGl0eSI6IjNlMGZiNWMzLTA0ZjEtNGJjNi1iMzNlLTYyMzI1NGM3MDIxNSJ9.j6qczVTbVz3dQAjDd9g0iNSLeFvxS1GXSD97tg20h60"

```
