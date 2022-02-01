import  urequests as requests
import  time;
import  ujson;

def ft_HTTP_com():
    post_data = ujson.dumps({'test':'123'})
    request_url = "http://95.217.167.216:8080/api/v1//telemetry"
    res = requests.post(request_url, headers = {'content-type':'application/json'},
            data = post_data).json();
    print(res);

def main():
    ft_HTTP_com();

main();
