RESTFull API for harddrive failures prediction by S.M.A.R.T data

SwaggerUI http://localhost:8000

Основной вызов:

POST new data:

endpoint - /data/ (http://localhost:8000/data/)

example:


```
{
  "smart_data_list": [
    {
      "track_dev_id": "0",
      "timestamp": "2019-01-01 14:21:07",
      "date": "2019-01-01",
      "model": "XYZ",
      "serial_number": "HD00",
      "failure": 0,
      "capacity_bytes": 10000000000000,
      "smart_1_normalized": 0.4875488281,
      "smart_1_raw": 0.1240234375,
      "smart_3_normalized": 0.1147460938,
      "smart_3_raw": 0,
      "smart_4_normalized": 1,
      "smart_4_raw": 0.0004377365,
      "smart_5_normalized": 0.39453125,
      "smart_5_raw": 0,
      "smart_7_normalized": 0.1557617188,
      "smart_7_raw": 0.0000224113,
      "smart_9_normalized": 0.6870117188,
      "smart_9_raw": 0.3869628906,
      "smart_10_normalized": 0.3586425781,
      "smart_10_raw": 0,
      "smart_12_normalized": 1,
      "smart_12_raw": 0.0097427368,
      "smart_187_normalized": 1,
      "smart_187_raw": 0,
      "smart_188_normalized": 1,
      "smart_188_raw": 0,
      "smart_190_normalized": 0.8569335938,
      "smart_190_raw": 0.1428222656,
      "smart_192_normalized": 0.2622070312,
      "smart_192_raw": 0,
      "smart_193_normalized": 0.412109375,
      "smart_193_raw": 0.0224761963,
      "smart_194_normalized": 0.0333251953,
      "smart_194_raw": 0.1428222656,
      "smart_195_normalized": 0.5385742188,
      "smart_195_raw": 0.4965820312,
      "smart_197_normalized": 0.39453125,
      "smart_197_raw": 0,
      "smart_198_normalized": 0.39453125,
      "smart_198_raw": 0,
      "smart_199_normalized": 1,
      "smart_199_raw": 0,
      "smart_240_normalized": 1,
      "smart_240_raw": 0,
      "smart_241_normalized": 0,
      "smart_241_raw": 0.2244873047,
      "smart_242_normalized": 0,
      "smart_242_raw": 0.0037708282
    },
    {
      "track_dev_id": "1",
      "timestamp": "2019-01-01 14:21:08",
      "date": "2019-01-01",
      "model": "UVT",
      "serial_number": "00DH",
      "failure": 0,
      "capacity_bytes": 10000000000001,
      "smart_1_normalized": 0.2563476562,
      "smart_1_raw": 0.0827026367,
      "smart_3_normalized": 0.1529541016,
      "smart_3_raw": 0,
      "smart_4_normalized": 1,
      "smart_4_raw": 0.0000397563,
      "smart_5_normalized": 0.39453125,
      "smart_5_raw": 0,
      "smart_7_normalized": 0.1708984375,
      "smart_7_raw": 0.0000358224,
      "smart_9_normalized": 0.9497070312,
      "smart_9_raw": 0.0624084473,
      "smart_10_normalized": 0.3586425781,
      "smart_10_raw": 0,
      "smart_12_normalized": 1,
      "smart_12_raw": 0.0016231537,
      "smart_187_normalized": 1,
      "smart_187_raw": 0,
      "smart_188_normalized": 1,
      "smart_188_raw": 0,
      "smart_190_normalized": 0.7143554688,
      "smart_190_raw": 0.2856445312,
      "smart_192_normalized": 0.2622070312,
      "smart_192_raw": 0.0007324219,
      "smart_193_normalized": 0.4924316406,
      "smart_193_raw": 0.0014295578,
      "smart_194_normalized": 0.0666503906,
      "smart_194_raw": 0.2697753906,
      "smart_195_normalized": 0.68359375,
      "smart_195_raw": 0.4990234375,
      "smart_197_normalized": 0.39453125,
      "smart_197_raw": 0,
      "smart_198_normalized": 0.39453125,
      "smart_198_raw": 0,
      "smart_199_normalized": 1,
      "smart_199_raw": 0,
      "smart_240_normalized": 1,
      "smart_240_raw": 0,
      "smart_241_normalized": 0,
      "smart_241_raw": 0.1544189453,
      "smart_242_normalized": 0,
      "smart_242_raw": 0.0013923645
    }
  ]
}
```

curl -X POST "http://localhost:8000/data/" -H  "accept: application/json" -H  "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQ1NzA2ODYsImlhdCI6MTU5NDU3MDM4Niwic3ViIjo2fQ.it4jWsHc9wPqIv9Dx8BCTTxG5VShMgwJB3_UA6q8I6o" -H  "Content-Type: application/json" -d "{  \"smart_data_list\": [    {      \"track_dev_id\": \"0\",      \"timestamp\": \"2019-01-01 14:21:07\",      \"date\": \"2019-01-01\",      \"model\": \"XYZ\",      \"serial_number\": \"HD00\",      \"failure\": 0,      \"capacity_bytes\": 10000000000000,      \"smart_1_normalized\": 0.4875488281,      \"smart_1_raw\": 0.1240234375,      \"smart_3_normalized\": 0.1147460938,      \"smart_3_raw\": 0,      \"smart_4_normalized\": 1,      \"smart_4_raw\": 0.0004377365,      \"smart_5_normalized\": 0.39453125,      \"smart_5_raw\": 0,      \"smart_7_normalized\": 0.1557617188,      \"smart_7_raw\": 0.0000224113,      \"smart_9_normalized\": 0.6870117188,      \"smart_9_raw\": 0.3869628906,      \"smart_10_normalized\": 0.3586425781,      \"smart_10_raw\": 0,      \"smart_12_normalized\": 1,      \"smart_12_raw\": 0.0097427368,      \"smart_187_normalized\": 1,      \"smart_187_raw\": 0,      \"smart_188_normalized\": 1,      \"smart_188_raw\": 0,      \"smart_190_normalized\": 0.8569335938,      \"smart_190_raw\": 0.1428222656,      \"smart_192_normalized\": 0.2622070312,      \"smart_192_raw\": 0,      \"smart_193_normalized\": 0.412109375,      \"smart_193_raw\": 0.0224761963,      \"smart_194_normalized\": 0.0333251953,      \"smart_194_raw\": 0.1428222656,      \"smart_195_normalized\": 0.5385742188,      \"smart_195_raw\": 0.4965820312,      \"smart_197_normalized\": 0.39453125,      \"smart_197_raw\": 0,      \"smart_198_normalized\": 0.39453125,      \"smart_198_raw\": 0,      \"smart_199_normalized\": 1,      \"smart_199_raw\": 0,      \"smart_240_normalized\": 1,      \"smart_240_raw\": 0,      \"smart_241_normalized\": 0,      \"smart_241_raw\": 0.2244873047,      \"smart_242_normalized\": 0,      \"smart_242_raw\": 0.0037708282    },    {      \"track_dev_id\": \"1\",      \"timestamp\": \"2019-01-01 14:21:08\",      \"date\": \"2019-01-01\",      \"model\": \"UVT\",      \"serial_number\": \"00DH\",      \"failure\": 0,      \"capacity_bytes\": 10000000000001,      \"smart_1_normalized\": 0.2563476562,      \"smart_1_raw\": 0.0827026367,      \"smart_3_normalized\": 0.1529541016,      \"smart_3_raw\": 0,      \"smart_4_normalized\": 1,      \"smart_4_raw\": 0.0000397563,      \"smart_5_normalized\": 0.39453125,      \"smart_5_raw\": 0,      \"smart_7_normalized\": 0.1708984375,      \"smart_7_raw\": 0.0000358224,      \"smart_9_normalized\": 0.9497070312,      \"smart_9_raw\": 0.0624084473,      \"smart_10_normalized\": 0.3586425781,      \"smart_10_raw\": 0,      \"smart_12_normalized\": 1,      \"smart_12_raw\": 0.0016231537,      \"smart_187_normalized\": 1,      \"smart_187_raw\": 0,      \"smart_188_normalized\": 1,      \"smart_188_raw\": 0,      \"smart_190_normalized\": 0.7143554688,      \"smart_190_raw\": 0.2856445312,      \"smart_192_normalized\": 0.2622070312,      \"smart_192_raw\": 0.0007324219,      \"smart_193_normalized\": 0.4924316406,      \"smart_193_raw\": 0.0014295578,      \"smart_194_normalized\": 0.0666503906,      \"smart_194_raw\": 0.2697753906,      \"smart_195_normalized\": 0.68359375,      \"smart_195_raw\": 0.4990234375,      \"smart_197_normalized\": 0.39453125,      \"smart_197_raw\": 0,      \"smart_198_normalized\": 0.39453125,      \"smart_198_raw\": 0,      \"smart_199_normalized\": 1,      \"smart_199_raw\": 0,      \"smart_240_normalized\": 1,      \"smart_240_raw\": 0,      \"smart_241_normalized\": 0,      \"smart_241_raw\": 0.1544189453,      \"smart_242_normalized\": 0,      \"smart_242_raw\": 0.0013923645    }  ]}"

```
response: True (or False)
```




Перед основным вызовом надо также авторизоваться, если же не создан user то так же его создать.

Создание пользователя:

POST create user:

endpoint - /user/ (http://localhost:8000/user/)

```
example:
{
  "email": "mail01@gmail.com",
  "username": "u01",
  "password": "u01pswd"
}
```

curl -X POST "http://localhost:8000/user/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"email\": \"mail01@gmail.com\",  \"username\": \"u01\",  \"password\": \"u01pswd\"}"

```
response:
{
  "status": "success",
  "message": "Successfully registered.",
  "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQ0OTMzMzAsImlhdCI6MTU5NDQ4NjEzMCwic3ViIjoyfQ.S_HYTEEQra_og3GsSpyfmtEZCifN1j_fzfXvSYO5Zcw"
}
```

Авторизация.

POST login:

endpoint - /auth/login (http://localhost:8000/auth/login)

```
example:
{
  "email": "mail01@gmail.com",
  "password": "u01pswd"
}
```

curl -X POST "http://localhost:8000/auth/login" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"email\": \"mail01@gmail.com\",  \"password\": \"u01pswd\"}"

```
response:
{
  "status": "success",
  "message": "Successfully logged in.",
  "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQ0OTM4MTgsImlhdCI6MTU5NDQ4NjYxOCwic3ViIjoyfQ.rkhCqB7A_hOKMUJy5xBYkkGI_hqhewBWCnBAqS2VGbU"
}
```

Выход пользователя.

POST logout:

endpoint - /auth/logout (http://localhost:8000/auth/logout)

curl -X POST "http://localhost:8000/auth/logout" -H  "accept: application/json" -H  "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQ0OTMzMzAsImlhdCI6MTU5NDQ4NjEzMCwic3ViIjoyfQ.S_HYTEEQra_og3GsSpyfmtEZCifN1j_fzfXvSYO5Zcw"

```
response:
{
  "status": "success",
  "message": "Successfully logged out."
}
```



