from django.http import HttpResponse
import requests
def get_lanzou_url(request, params):
    print("start" + params)
    paramArr = params.split("&")
    ww = "https://wwf.lanzouq.com"
    print("start")
    uu=ww + "/"+ paramArr[1]
    pwd=paramArr[0]
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
    print(data)
    rsp1=requests.post(url,data=data,headers=headers)

    date=rsp1.text
    print("content:"+date)
    json = rsp1.json()
    res = json.get("dom")+"/file/"+ json.get("url")
    print(res)
    return HttpResponse(res)
