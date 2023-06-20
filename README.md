# 💬 Bard-with-OCR
텔레그램 봇을 이용한 채팅형태의 <strong>Bard</strong><br/>
<strong>OCR</strong>을 이용해 텍스트 기반의 이미지를 첨부한 대화도 가능하다.<br/>
본 서비스는 <strong>무료</strong>로 이용 가능하다.

## Chat Result
![1](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/df1314b9-78dc-4194-96d6-e7098fdce8bc)


## Setting

### Bard API key
1. 개발자도구 - Application - Storage - Cookies - https://bard.google.com 클릭
2. Name이 "_Secure-1PSID"인 Value 복사

![2](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/a24127ca-03ac-481c-afdb-8252af967ded)

#### install library
```text
pip install bardapi
```

### TelegramBot API 
1. @BotFather
2. /newbot 입력 후 봇 이름과 아이디 설정
3. 챗봇이 보내주는 토큰 복사

![3](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/d2b7f6e1-c81b-4ff0-a18d-e0c20745fc3c)

#### install library(version)
```text
pip install python-telegram-bot==12.8
```

### MS Azure Computervision API
1. Computervision 리소스 만들기
2. 해당 리소스의 key와 endpoint 복사

![4](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/e3bbf45b-ad50-4835-a7e3-3848cf236195)
![5](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/675436d1-f46a-420d-ade4-ce54fefb8dec)


#### install library
```text
pip install azure.cognitiveservices.vision.computervision
```
