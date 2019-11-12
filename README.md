# 2019-2 객체지향 프로그래밍 프로젝트 - **우유 팀**
구성원: 2-1 정유진 | 2-5 양우현

## 1. 주제
'세종과학예술영재학교 대나무숲' 페이스북 페이지 게시글 분석 프로그램

## 2. 동기
'세종과학예술영재학교 대나무숲' 페이스북 페이지는 익명성이 보장되는 온라인 공간으로, 우리 학교의 학생을 비롯한 관계자들이 의견 표명으로 가해질 불이익을 걱정하지 않고 자신의 입장과 생각을 온전하게 표현할 수 있는 창구이기도 하다. 따라서 이 공간에서는 다양한 사람들이 어떤 분야에 관심을 갖고 있으며, 어떤 글에 공감하는지에 대한 정보를 얻을 수 있다. 그러나 이러한 정보를 교내 여러 단체에서 제대로 활용하고 있지 못하다는 생각이 들었고, 이에 페이지의 게시글을 통계적으로 정리하여 경향성을 쉽게 파악할 수 있는 프로그램을 제작하게 되었다.

## 3. 프로그램 사용 대상
학생회와 기숙사자치위원회 등 학생들의 여론을 파악해야 하는 단체

## 4. 목적
'세종과학예술영재학교 대나무숲' 페이지의 게시글을 분석하여 학생들이 어떤 분야에 관심을 갖고 있으며, 어떤 글에 공감하는가를 통계적으로 분석하고 시각화하여 사용자에게 제공한다.

## 5. 주요기능
1. 원하는 기간을 입력하면 그 기간 내의 '대나무숲' 게시글을 검색하여 리스트로 보여준다.
2. 리스트의 게시글을 올라온 시간 순서대로, 좋아요 및 공감 수 순서대로, 주제별로 정렬할 수 있다.
3. '대나무숲' 게시글을 주제별로 분류한 다음 시각화 과정을 거쳐 그래프로써 사용자에게 통계 결과를 보여주는 기능을 구현한다. 
4. (GUI를 이용하여) 사용자가 원하는 주제, 날짜 등을 입력받고 통계 결과를 출력하는 프로그램을 만든다.

## 6. 프로젝트 핵심
페이스북 페이지로부터 원하는 데이터를 가져오고, 그 데이터를 원하는대로 가공하여 정렬할 수 있어야 한다.

## 7. 구현에 필요한 라이브러리나 기술
{web parsing, Beautifulsoup, pyautogui, matplotlib, pyqt5 ...}


<기술>

web parsing : 웹 사이트에서 원하는 정보를 자동으로 수집하는 것

<라이브러리>
1. Beautifulsoup : 웹 데이터를 가져올 때 사용되는 라이브러리이다. 페이지의 HTML 소스를 가져올 때, 태그를 읽어서 우리가 이용할 부분인 게시글이나 좋아요를 분리해서 찾아주는 기능을 구현하기 위해 사용된다.

공식 사이트 - https://www.crummy.com/software/BeautifulSoup/

2. pyautogui : 파이썬을 이용하여 마우스와 키보드의 움직임을 제어할 수 있는 기능을 제공한다. 자동 스크롤을 구현하여 대나무숲의 예전 게시글들을 읽어 올 것이다. Facebook Open API를 구현하지 못하는 이뉴는, 이를 이용하려면 해당 페이지의 토큰이 필요한데, 토큰을 얻기 위해서는 이 페이지의 관리자여야 하기 때문이다.

공식 사이트 - https://pyautogui.readthedocs.io/en/latest/#

3. matplotlib : 

공식 사이트 - https://matplotlib.org/


3. pyqt5 : GUI 구성을 할 수 있는 기능을 제공한다. 

공식 사이트 - https://pypi.org/project/PyQt5/

한국어 사용법 사이트 - https://wikidocs.net/book/2165




## 8. **분업 계획**
1. 페이지를 가져오는거
2. 데이터를 시각화시키는
3. 프로그램 GUI 구현

## 9. 기타

<hr>

#### readme 작성관련 참고하기 [바로가기](https://heropy.blog/2017/09/30/markdown/)

#### 예시 계획서 [[예시 1]](https://docs.google.com/document/d/1hcuGhTtmiTUxuBtr3O6ffrSMahKNhEj33woE02V-84U/edit?usp=sharing) | [[예시 2]](https://docs.google.com/document/d/1FmxTZvmrroOW4uZ34Xfyyk9ejrQNx6gtsB6k7zOvHYE/edit?usp=sharing) | [[예시 3]](https://github.com/goldmango328/2018-OOP-Python-Light) | [[예시4]](https://github.com/ssy05468/2018-OOP-Python-lightbulb) | [[모두보기]](https://github.com/kadragon/oop_project_ex/network/members)
