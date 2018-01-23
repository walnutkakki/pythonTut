#-*-coding:utf-8-*- 
#SyntaxError: Non-ASCII character '\xeb' in file module_using_name.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details 오류가 뜰 때 위에 거를 씁시다.
if __name__=='__main__':                        # 모든 모듈이 가지고 있는 이름은 모듈 내의 명령을 통해 알 수 있습니다. 이 때 모듈이 외부에서 불러져왔을 때 각각 다르게 처리할 수 있게 name을 씁니다.
    print 'This program is being run by itself'
else:
    print "I'm being imported from another module"