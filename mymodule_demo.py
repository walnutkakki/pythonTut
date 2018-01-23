#-*-coding:utf-8-*- 
import mymodule

mymodule.say_hi()

print 'Version', mymodule.__ver__       #AttributeError : 변수명을 잘못 설정했을 때 나옴, 이름이 다른게 없어서 그냥 version을 ver으로만 바꿈. 