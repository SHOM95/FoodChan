# FoodChan
웹페이지 프로젝트

# 1일차
- flask 기본적인 내용 이해해야함
- 디비 서버는 이미 구축
- 호스팅 서버 고민중 - 코드 공유는 깃헙으로 하되 메인 서버도 고민해봐야함
- 일단 flask로 기본 기능 - 게시판, 로그인, 로그아웃, 회원가입 기능 넣자
- 기능 - session 검증 필요!

#### 9월 1일 2시 기본 템플릿 및 css,js 코드 추가 및 restful.py 수정
	9월 1일 17시~22시 restful.py 삭제 및 flask 튜토리얼에 따른 코드 작성 완료.
#### 9월 1일 2시 35분 코드는 안돌아 가지만 restful.py 코드 일단 수정함.
	9월 1일 17시~22시 restful.py 삭제 및 flask 튜토리얼에 따른 코드 작성 완료.
####                  안돌아가는 원인 찾아야함
	9월 1일 17시~22시 restful.py 삭제 및 flask 튜토리얼에 따른 코드 작성 완료.


# 2일차
- 지금까지 짜여진 코드를 바탕으로 회원가입에 관한 코드를 작성해야함.
- 현재 테스트 DB 에 테이블 추가 완료.
- 회원가입 페이지 (html) 및 해당 html 에서 구현한 이벤트들(예: 버튼클릭)에 대한 함수를 flaskr.py 에서 구현해야함.

#### 9월 2일 새벽3시 52분 회원가입 페이지 기초공사 완료 ( 기본 코드 작성 완료 ) 및 로그인 검증 1차 개선 완료
	코드 읽을 때 python이 객체지향인점을 알아야 한다. __init__ 과 관련된 객체지향적 특징 검색하길!!
#### 9월 2일 오후 2시 40분 회원가입 검증 2차 개선 완료. 일단 중복 비번에 대해서 걸러내도록 수정함.
	어떻게 하면 1. 2. 3. 이런식으로 db에서 id 값을 가져와서 앞에 숫자를 표시할 수 있을까?
	jinja2를 좀 더 파악해야 할 듯.

# 3일차
#### 9월 3일 4시 15분 bootstrap 디자인 추가 개발 준비 완료
#### 9월 3일 20시 - 23시 기획 작성( start page, 사용자별 개인 메인 페이지, 알림 표시 디자인 등.)

# 4일차
#### 9월 4일 오전 1시-4시 반 메인 페이지 현재 제작 플라스크 페이지에 추가

# 5일차
#### 9월 5일 startpage 부분 전체 플라스크 페이지에 이식 중
#### 9월 5일 6시 30분 ~ 8시 7분 register page 코드 변경 및 주석 변경함. css 디자인도 개선함.
	이제 이메일 입력과 비밀번호 재확인 기능도 넣을까 생각해본다.
	본격적인 전체 틀 변경, 우리에게 맞는 서버 코드 변경이 필요해보인다.

# 6일차
#### 9월 6일 ~6시 30분 홈페이지 로고 변경 및 이동 url 변경
#### 9월 6일 8시 30분 ~ 10시 49분 실제 메인 페이지 적용 (html 코드만) flaskr.py의 메인 페이지 부분과 이에대해 로그인 검증하는 부눈 tmeplate 마다 submit, redirect 경로 업데이트함.
	일단 초기 형태 완성

#7일차
#### 9월 7일 7시 30분 ~ 8시 23분 등록 페이지 업데이트
- 1. template.html 파일 : 비밀번호 검증과 이메일 입력 부분 주석 해제
- 2-1. flaskr.py 파일 : 상단 클레스에서 데이터베이스에서 이메일이 전 계정에서 사용되었는지 가져와서 검증하는 부분 추가
- 2-2. flaskr.py 파일 :  하단 route 부분에서 등록 검증 추가
- 3. schema.sql 파일 : text column 추가
- 데이터 베이스 재생성 필요함( flaskr.db 부분 오류나면 sqlite browser로 수정부탁드림.)

> readme 와 일정과 분리함 (9월 13일 오후 1시 38분)



# 8일차

2월 15일 error 및 flash 메세지 팝업 끌 수 있도록 수정함. 세부 디자인 수정.



# 9일차

2월 16일 -2월 17일 게시판 생성. 게시판의 목차, 제목, 글쓴이를 표시. 제목을 클릭하면 제목과 글쓴이 이름이 뜸과 동시에 글을 확인할 수 있게 땨로 template 폴더에 html 파일 생성함.

sqlite3에서 목차의 번호가 자동으로 생성될때, 글이 삭제된 이후에도 삭제된 글의 순번을 따라서 번호가 계속 이어지게 된다. 이 부분에 대해서 수정 및 공부 필요.

ex > 1,2,3,4,5 -> 2번과 5번 글 삭제 -> 재정렬도 설정 안함. 및 이후 번호 생성에 대해 설정 안함

이를 다음번에 작업할때 생각해야함.



# 10일차

2월 21일 - 2월 22일

글 쓸때 제목이 동일할 경우 검사하도록 python 파일 수정.

게시판 목록과 글쓰기 페이지를 분리함.

기타 세부적인 코드 및 디자인 수정함.

초기 화면 slider 이미지 변경 및 fabicon.ico 사진 추가함.

