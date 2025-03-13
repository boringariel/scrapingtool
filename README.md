# Scrapingtool
---
파이썬 웹 스크래핑을 위한 편리한 도구, 스크래핑툴을 소개합니다.
</p>

이 패키지는 웹 스크래핑을 할 때 일반적으로 사용되는 기능을 사전 정의해 놓았습니다. 만약 필요한 기능이 있다면 [개발자]("mailto://jwkang3929@naver.com") 에게 알려주세요!
</p></br></br>

## 설치
---
이 패키지를 설치하려면 다음과 같은 명령어를 실행해 주세요.
</p>

`pip install git+https://github.com/boringariel/scrapingtool.git`
</p></br></br>

## 요구사양
---
스크래핑툴을 설치하기 위해서는 아래 요구사양을 만족해야 합니다.
</p>

* Python >= 3.8
* selenium >= 4.0.0
* requests
* chrome, edge, opera 중 하나 이상의 웹 브라우저

</p></br></br>

## 사용법
---
다음 코드를 실행하여 크롬 유저 에이전트 정보를 확인할 수 있습니다.
</p>

`user_agent = scrapingtool.get_chrome_user_agent()`
</p>

엣지를 이용하고 있다면 다음 코드를 이용할 수 있습니다.
</p>

`user_agent = scrapingtool.get_edge_user_agent()`

오페라를 이용한다면 다음 코드를 이용할 수 있습니다.
</p>

`user_agent = scrapingtool.get_opera_user_agent()`
</p>

만약 내 브라우저 정보를 모르거나, 자동으로 실행하고 싶다면 아래 코드를 이용할 수 있습니다.
</p>

`user_agent = scrapingtool.get_auto_user_agent()`
</p></br></br>

만약 `requests.get()` 함수와 같은 명령을 수행할 때, 이 패키지를 이용해 user agent 정보를 입력하려면 아래와 같이 코드를 실행합니다.
</p>

```python
url='https://www.example.com'
refer='https://www.example.com'
content_type='application/json'
user_agent_input='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'

response = scrapingtool.get(
    url=url, refer=refer, content_type=content_type, user_agent_input=user_agent_input
)
```
</p>

코드 실행시에는 requests.get() 함수와 동일한 형태의 return이 반환됩니다.
</p>

이 때, refer, content_type, user_agent_input 는 필요하지 않은 경우 생략할 수 있습니다.
