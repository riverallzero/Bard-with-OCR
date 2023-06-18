# 💬 Bard-with-OCR
텔레그램 봇을 이용한 채팅형태의 <strong>Bard</strong><br/>
<strong>OCR</strong>을 이용해 텍스트 기반의 이미지를 첨부한 대화도 가능하다.

## Chat Result
![기말_시연결과_202110065_강다영](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/82fedc6a-aaec-4bdc-afac-52af1defd4bc)


## Setting

### Bard API key
1. 개발자도구 - Application - Storage - Cookies - https://bard.google.com 클릭
2. Name이 "_Secure-1PSID"인 Value 복사

![bard-api.png](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/56156cd6-02b7-4a26-b4af-0311bc80e9b4)

#### install library
```text
pip install bardapi
```

### TelegramBot API 
1. @BotFather
2. /newbot 입력 후 봇 이름과 아이디 설정
3. 챗봇이 보내주는 토큰 복사

![telegram-api.png](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/b5a88e86-2dbc-4b7a-8c8c-5d2427547741)

#### install library(version)
```text
pip install python-telegram-bot==12.8
```

### MS Azure Computervision API
1. Computervision 리소스 만들기
2. 해당 리소스의 key와 endpoint 복사

![azure-api.png](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/f61c1a55-6048-4d26-bbf8-32dcc3df430f)
![key-endpoint.png](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/8b5b167e-ef8d-4a1b-ab0d-dc36d4b8fbc4)


#### install library
```text
pip install azure.cognitiveservices.vision.computervision
```
