import requests
import json
import os

# 配置开始 
user = os.environ["USER"]
account = user.split( )[0] # 账号
password = user.split( )[1] # 密码
school_id = user.split( )[2] # 学校ID
sign_gps = os.environ["SIGN_GPS"]  # 签到坐标（注意小数点取后6位）
longitude = sign_gps.split(",")[0] # 经度
latitude = sign_gps.split(",")[1] # 纬度
data = {
  "account":account,
  "password":password,
  "school_id":school_id,
  "longitude":longitude,
  "latitude":latitude,
  "address_name":os.environ["ADDRESS_NAME"] 
}
headers = {'Content-Type': 'application/json'}

# 打印配置信息
print("配置信息：")
print(f"账号: {account}")
print(f"密码: {password}")
print(f"学校ID: {school_id}")
print(f"经度: {longitude}")
print(f"纬度: {latitude}")
print(f"签到地址: {data['address_name']}")

response = requests.post(url='https://service-nm4jylpg-1251957121.gz.apigw.tencentcs.com/release/xixunyun', headers=headers, data=json.dumps(data))

# 检查响应状态码
print(f"响应状态码: {response.status_code}")

# 打印响应内容
print("响应内容：")
try:
    response_json = response.json()
    print(json.dumps(response_json, ensure_ascii=False, indent=4))  # 格式化打印JSON
    print(response_json["data"])
except json.JSONDecodeError:
    print("响应内容不是有效的JSON格式")
    print(response.text)  # 打印原始响应文本

SCKEY=os.environ["SCKEY"]
if len(SCKEY) >= 1:
  url = 'https://sctapi.ftqq.com/'+SCKEY+'.send'
  requests.post(url, data={"title": "习讯云签到提醒", "desp": response.json()["data"]})
