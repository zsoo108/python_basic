# 2) 패키지 내 모듈을 미리 iomport
from .graphic.render import render_test


# 1) 패키지 변수 및 함수 정의
VERSION = 3.5

def print_version_info():
    print(f'The version of this game is {VERSION}.')

# 3) 패키지 초기화
# 패키지를 처음 import할 때 초기화 코드가 실행된다.
print("Initialzing game ...")