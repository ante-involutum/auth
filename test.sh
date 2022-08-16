curl -i -X GET http://tink.test:30089/demo-2 -H 'Authorization: admin'
{
    "disable": false,
    "request_headers": [
    "Authorization"
    ],
    "request_method": "GET",
    "upstream_headers": [
    "X-User-ID"
    ],
    "uri": "http://auth.tink:8001/auth/authorization/"
}

curl -i -H "Content-type: application/json" -X GET -d '{"name": "admin","password": "admin"}' http://tink.test:30089/demo-1
{
    "disable": false,
    "request_method": "POST",
    "uri": "http://auth.tink:8001/auth/password/"
}
