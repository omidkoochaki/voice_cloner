
# Voice Cloner API

This is just a very simple API which provides Registration and Login functionalities.

For Authentication, we used django rest framework TokenAuthentication.


## API Reference

### Accounts App
#### Register User
```http
  POST /accounts/register/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. |
| `password` | `string` | **Required**. |
| `email` | `string` |  |
| `first_name` | `string` |  |
| `last_name` | `string` |  |


#### Login User
```http
  GET /accounts/login/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. |
| `password` | `string` | **Required**. |


## Run Project

To start the project run:

```bash
  make build
  make start
```
take a look at Makefile for more options.
