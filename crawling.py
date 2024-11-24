import requests
from lxml import html

# URL을 문자열로 작성해야 합니다.
url = 'https://www.schoolinfo.go.kr/Main.do'

# 웹 페이지 요청
response = requests.get(url)

# 응답 상태 코드가 200일 경우 (정상적으로 페이지가 로드된 경우)
if response.status_code == 200:
    # HTML 콘텐츠 파싱
    tree = html.fromstring(response.content)

    # XPath로 '학교명' 입력 필드 찾기
    school_name_xpath = '//*[@id="SEARCH_KEYWORD"]'

    # XPath로 해당 요소 찾기
    school_name_element = tree.xpath(school_name_xpath)

    # 추출된 요소가 존재하는지 확인하고 출력
    if school_name_element:
        print("학교명 입력 필드가 존재합니다.")
    else:
        print("학교명 입력 필드를 찾을 수 없습니다.")
else:
    print("웹 페이지를 불러오는 데 실패했습니다.")

