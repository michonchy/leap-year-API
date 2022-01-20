import json
from socket import EAI_FAIL

# import requests
# 西暦を入力したらその年が閏（うるう）年かどうかを判定するプログラムを作成せよ。
# なお、4で割り切れる年のうち、100で割り切れないか、400で割り切れる年は閏年である。

class InvalidError(Exception):
    pass
def is_number(x: str):
    if x.startswith("-"):
        x = x[1:]
    if not x.isdigit():
        return False
    return True
def number(x):
    if not is_number(x):
        raise InvalidError("整数値を入力してください。")
    return int(x)

def is_leap_year(n):
    if n % 100 == 0 and n % 400 != 0:
        return "not leap year"
    elif n % 4 == 0:
        return "leap year"
    else:
        return "not leap year"
    
    

def validate_number(x):
    if x < 0:
        raise InvalidError("整数値を入力してください。")


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    print(event)
    try:
        n = event.get('queryStringParameters').get('numbers')
        n = number(n)
        validate_number(n)
        print(n)
    except Exception as e:
        return{
        "statusCode": 400,
        "headers":{
            "Content-type": "application/json;charset=UTF-8"
        },
        "body":json.dumps({
            "message":str(e)
        },ensure_ascii=False).encode("utf8"),
    }
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": is_leap_year(n),
            # "location": ip.text.replace("\n", "")
        }),
    }
