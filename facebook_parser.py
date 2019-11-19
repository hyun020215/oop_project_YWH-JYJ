import bs4
from selenium import webdriver
from datetime import datetime

TARGET_URL = 'https://www.facebook.com/SASABamboo/'  # 세종과학예술영재학교 대나무숲 페이지 주소


def webdriver_maker():
    """
    headless 브라우저(창이 안뜨는)를 위해서 설정.
    https://beomi.github.io/2017/09/28/HowToMakeWebCrawler-Headless-Chrome/
    :return: webdriver (크롬)을 생성
    """
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")

    #return webdriver.Chrome('D:/우현 데이타/고등학교/세종과학예술학교/공부/2019 과목/2학기/객체지향프로그래밍/2019-OOP-Python-Milk/chromedriver.exe',
    #                        options=options)
    return webdriver.Chrome('C:/Users/USER/PycharmProjects/2019-OOP-Python-Milk/chromedriver.exe',options=options)


def timestamp_to_str(timestamp):
    """
    timestamp 를 2000.00.00 00:00:00 형태로 변환
    :param timestamp: timestamp
    :return: 2000.00.00 00:00:00
    """
    return datetime.fromtimestamp(timestamp).strftime("%Y.%m.%d %H:%M:%S")


def post_crawl(start, end):
    """
    start 와 end 의 날짜 형식은 2000.00.00 이다.
    :param start: 크롤링을 시작하는 시간(start 에서부터)
    :param end: 크롤링을 끝내는 시간(end 까지)
    :return:
    """

    start = list(map(int,start.split('.')))  # [2000,00,00]
    end = list(map(int,end.split('.')))
    inform = []  # 게시글 정보를 담을 리스트

    driver = webdriver_maker()
    driver.get(TARGET_URL)

    # 페이지 스크롤링 코드
    while driver.find_element_by_tag_name('div'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Divs = driver.find_element_by_tag_name('div').text
        if 'End of Results' in Divs:  # 영어 버전에서 작동하는 코드
            print('end')
            break

    html = driver.page_source  # html 추출

    soup = bs4.BeautifulSoup(html, 'html.parser')  # bs4에게 부탁
    posts = soup.select('div.userContentWrapper')  # 게시물이 포함되어 있는 <div class='userContentWrapper'> 검색

    first_post_pass = True

    for post in posts:
        # 첫 포스트 제외 | 오래된 포스트일 가능성이 높음.
        if first_post_pass is True:
            first_post_pass = False
            continue

        j = post.select('div')
        temp = []
        temp.append(timestamp_to_str(int(j[15].select('abbr')[0].get('data-utime').strip())))  # 날짜 출력
        temp.append(j[16].getText().strip())  # 내용 출력
        try:
            for i in range(0,6): # 좋아요 종류 6가지
                temp.append(j[26].select('._1n9k')[i].contents[0].get('aria-label'))
        except IndexError:
            pass
        inform.append(temp)

    print(inform)
    print('END')

    driver.quit()  # 드라이버 사용 종료. 이 코드가 없을 경우 프로세스가 남게 됨.


post_crawl('2000.00.00','2000.00.00')