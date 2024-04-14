import requests

def get_lanzou_direct_link():
    uu=input("蓝奏链接：")
    pwd=input("密码:")
    ww = "https://wwf.lanzouq.com"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.236.400 QQBrowser/12.4.5605.400",
             "Referer": ww}
    
    # 发送GET请求获取网页内容
    rsp = requests.get(uu, headers=headers)
    txt = rsp.text
    start = txt.find("var skdklds = '") + len("var skdklds = '")
    end= txt.find("';",start)
    sign=txt[start:end]

    urlstart = txt.find("url : '", end) + len("url : '")
    urlend = txt.find("',", urlstart)
    url=ww + txt[urlstart:urlend]

    data={'action':'downprocess','sign':sign,'p':pwd}
    rsp1=requests.post(url,data=data,headers=headers)

    date=rsp1.text
    print("content:"+date)
    json = rsp1.json()
    
    print(json.get("dom")+"/file/"+ json.get("url"))


if __name__ == "__main__":
    get_lanzou_direct_link()
