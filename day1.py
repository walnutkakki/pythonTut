print("help me, there're wolves in the yard!")
print("hello,'james', this is my precious ring, haha")
print(''' 나는 강하다
            너도 강하다''')
#문자열 포맷팅을 하자.
chulsoo = 20
nami = "she's woman"
print( "{0}: why he's always do bad thought? because chulsoo's age is {1}").format(nami,chulsoo)
print( "{1}: why he's always do bad thought? because chulsoo's age is {0}").format(nami,chulsoo)
print( '{1}: why he always do bad thought? because chulsooage is {0}').format(nami,chulsoo)

#문자열 포맷팅에 중괄호 위치에 주어진 인자의 값을 치환해 넣기도 합니다. 세부사항 지정이 가능합니다.
print '{0:.3f}'.format(1.0/3)
print '{0:_^11}'.format('hello')
#줄 안바꾸기에는 역시 ,을 사용하면 된다.
print "a" ,
print "ba"
print("hello"),
print("I'm coming for saving U")
#이스케이프 문자 사용하기
print('hi, jason\'s home?')
print("I am deathwing,\t the end of the world \n I am the real cataclysm!")
#순문자열.
print(r"Newlines are indicated by \n")
print(r'I\'d like to eat basic food')