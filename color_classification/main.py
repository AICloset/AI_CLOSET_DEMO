from queue import Queue
import color
import sys

sys.path.append('C:\\ai_closet_demo')
from yolov5 import detect

if __name__ == "__main__":
    
    result = ""
    # 색상분류
    que = Queue()
    que = color.execute("C:\\ai_closet_demo\image\\adidas.png", que)
    # print(que.get())
    result += f'{que.get()}'

    # 브랜드 로고 식별
    detect.main_ide("C:\\ai_closet_demo\image\\adidas.png")
    if(detect.logo_name):
        result += f'{detect.logo_name} 입니다. '
    # print(detect.logo_name)
    print(result)
