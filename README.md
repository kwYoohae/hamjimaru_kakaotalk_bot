# 🍱함지마루 채팅봇

`Kakaotalk open builder`와 `flask`를 사용하여 구현한 프로그램입니다.

매번 일일이 학교 홈페이지 내 식단 안내 게시글을 확인할 필요 없이 챗봇을 통해 각 요일의 식단을 확인할 수 있습니다.

---

## ✔️프로젝트 소개

- `requests`을 이용한 데이터 스크래핑을 이용하여 학식 메뉴를 불러와서 `table.csv`파일로 저장 후 호출마다 알려줌
- `Flask`를 사용해서 **POST** 요청 처리 후 정해진 Json 파일로 클라이언트에게 전송한다.

## ✔️프로젝트 실행방법

- `nohup python3 menu.py 1> /dev/null 2>&1 &`을 사용하여 실행
- `nohup python3 server.py &`를 사용하여 실행

## ✔️Python 의존성 설치

- `pip install pandas`
- `pip install bs4`
- `pip install requests`
- `pip install flask`
- `pip install schedule`

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
