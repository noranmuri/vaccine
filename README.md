# vaccine
open source team project

06/12 조정우
6/12일 첫만남 조원들과 처음 만나고 깃허브에 contributor를 추가하고 조장님께서 repository를 만들어 주셨다 우리 repository이름의 유래는 코로나를 빨리 이겨내고 대면강의를 하고싶다는 마음에서 백신이라는 이름을 지었다.

06/12 황성윤 
  과제가 형상화 되지 않아서 일단 스스로 첫 페이지를 만들어 보고 회의하기로 했다. 약간 기대중 ^_^

06/12 홍지승
 오늘 팀원들을 만나서 팀명을 코로나를 이겨내자는 마음으로 vaccine으로 짓고 repository를 만들었다. 다음주 월요일까지 html를 각자 구현해오기로 했다.

06/20 홍지승
 startpage html과 url inputpage html을 만듬
 startpage를 css를 사용해 디자인하고 button을 누르면 연결되는 기능까지 구현.
 
06/20 조정우
-단일 url주소 입력 텍스트를 크롤링하는 것을 구현현함

6/23 조정우
-크롤링 및 분석 처리 상태 표시 (성공/실패/중복 url 있음 등의 상태 메세지 보여줌)
-pandas의 dataFrame을 이용해서 flask에서 표를 만들어 html로 옮겨주는 시도를 해보았다.

6/27 조정우
-웹페이지를 분석하는 시간을 구현함
-url크롤링 한 후 결과 html을 구현함
-url주소를 binary string 에서 string 으로 변경 시켜주는 코드를 구현함.

6/28 조정우
-마지막 결과 출력 화면인 table.html을 표형식으로 출력하도록 구현하였다.
-css코드와 html코드를 합쳤다(코드를 합치는 과정에서 오류를 찾아냄).


06/20 황성윤
-파일 업로드 받는 html 생성
-app.py 에 업로드 된 파일 저장하는 코드 수정 중

06/22 황성윤
- 파일 업로드 받는 html(fileInput.html) 수정
- app.py 파일 받아오는 부부 수정 완료 -> 파일을 한 줄씩 읽어서 크롤링 하는 부분 구현해야함
- 파일의 한 줄씩 읽으면서 크롤링 하는 코드를 완료하였다. 

06/25 황성윤
- 크롤링한 데이터를 바탕으로 표를 만들기 -> 표 만드는 방법 구현하다가 포기,,

06/26 황성윤
- 크롤링한 데이터를 text파일로 만들어서 단어 기준으로 나누어 개수 카운트하여 표로 나타나도록 page 생성 (table.html) --> css로 table 모양 구현해야 함
