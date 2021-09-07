# 🍱함지마루 채팅봇

`Kakaotalk open builder`와 `flask`를 사용하여 구현한 프로그램입니다.

매번 일일이 학교 홈페이지 내 식단 안내 게시글을 확인할 필요 없이 챗봇을 통해 각 요일의 식단을 확인할 수 있습니다.

---

## ✔️프로젝트 소개

- `selenium`을 이용한 데이터 스크래핑을 이용하여 학식 메뉴를 불러와서 `table.csv`파일로 저장 후 호출마다 알려줌
- `Flask`를 사용해서 **POST** 요청 처리 후 정해진 Json 파일로 클라이언트에게 전송한다.

## ✔️프로젝트 실행방법

- `crontab -e`으로 `crontab` 파일에서 \* _/3 _ \* \* /파이썬 절대경로/ /파일 절대경로/ 추가
- `nohup python3 server.py &`를 사용하여 실행

## ✔️Python 의존성 설치

- `pip install pandas`
- `pip install bs4`
- `pip install selenium`
- `pip install flask`
-

## ✔️구글 chrome 설치

1. `wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -`
2. `sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'`
3. `sudo apt-get update`
4. `sudo apt-get install google-chrome-stable`

## ✔️추후 추가기능

- 메뉴 사진을 찍고 서버에 자동업로드 기능 추가

---

## Reference

- [카카오톡 오픈빌더](https://i.kakao.com/docs/getting-started-overview#%EC%98%A4%ED%94%88%EB%B9%8C%EB%8D%94-%EC%86%8C%EA%B0%9C)
- [학식 정보](https://www.kw.ac.kr/ko/life/facility11.jsp)
- [카카오톡 친구추가](https://pf.kakao.com/_QVKGs)

## 🧑‍💻개발자

> 🛠️[bjybs123](https://github.com/bjybs123)  
> 🐵[KiKi-Daehaksaeng](https://github.com/KiKi-Daehaksaeng)  
> 😳[kwYoohae](https://github.com/kwYoohae)

## 친구추가

![QRCodeImg](https://user-images.githubusercontent.com/74089271/132363541-fa09944a-6370-42da-bfa1-f6728f8f3196.jpg)
