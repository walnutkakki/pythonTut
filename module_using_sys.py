import sys                                 # import로 sys를 불러왔다. 다른 모듈 불러오려면 등록되어있는걸 하거나 만들었을 때는 sys.path 변수에 모듈 루트를 정해서 저장해주어야함.
                                           # 혹은 from 모듈명 import 변수명 을 할 수도 있음
print('This command arguments are:')       

from math import sqrt                      # math 모듈에서 sqrt변수를 가져옵니다
print "root 16 is", sqrt(16)               # 하면 root 16 is 4.0 이라고 나온다/ 

for i in sys.argv:                         # 모듈 sys 내의 argv변수를 불러와서, sys.argv라고 하면 불러올 수 있다. 변수 이름 조심.. 만일 변수 내에 argv라는 변수 있으면 충돌할수도..
    print i

print '\n\nThe PATH is', sys.path, '\n'    # 어렵다

print (sys.argv)                           # 그냥 치면 이렇게 금방 알 수 있겠다!

