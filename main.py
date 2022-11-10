from queue import Queue
import sys

sys.path.append('C:\\ai_closet_demo\\color_classification')
from color_classification import color

sys.path.append('C:\\ai_closet_demo')
from yolov5 import detect

sys.path.append('C:\\ai_closet_demo\\pattern_recognize')
from pattern_recognize import pattern

if __name__ == "__main__":
    
    src = sys.argv[1]
    # src = "C:\\ai_closet_demo\\image\\polo.jpeg"
    
    # print("색분류")
    result = ""
    # 색상분류
    que = Queue()
    que = color.execute(src, que)
    # print(que.get())
    result += f'{que.get()}'
    # print("로고----------")

    # 브랜드 로고 식별
    detect.main_ide(src)
    if(detect.logo_name):
        result += f'{detect.logo_name}, '
    # print(detect.logo_name)
    # print("-무늬---------")

    # 무늬 식별 
    pattern.classify_pattern(src)
    result += f'{pattern.pattern_name}'

    print(result + "입니다.")