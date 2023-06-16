# Bard-with-OCR

## Bot 이용
![기말_시연결과_202110065_강다영](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/82fedc6a-aaec-4bdc-afac-52af1defd4bc)


## API 설정

### Bard에서 API key 가져오기
1. https://bard.google.com 사이트 접속 
2. 개발자도구 - Application - Storage - Cookies - https://bard.google.com 클릭
3. Name이 "_Secure-1PSID"인 Value 복사

![bard-api.png](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/56156cd6-02b7-4a26-b4af-0311bc80e9b4)

#### 라이브러리 설치
```text
pip install bardapi
```

### Telegram Chatbot에서 API 가져오기
1. @BotFather
2. /newbot 입력 후 봇 이름과 아이디 설정
3. 챗봇이 보내주는 토큰 복사

![telegram-api.png](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/65962797-a6bd-4fd4-9981-2aa1b70827e9)

#### 라이브러리 설치(버전 지정 필요)
```text
pip install python-telegram-bot==12.8
```

### MS Azure Computervision API 가져오기
1. Computervision 리소스 만들기
2. 해당 리소스의 key와 endpoint 복사

![azure-api.png](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/f61c1a55-6048-4d26-bbf8-32dcc3df430f)
![key-endpoint.png](https://github.com/riverallzero/Bard-with-OCR/assets/93754504/8b5b167e-ef8d-4a1b-ab0d-dc36d4b8fbc4)
