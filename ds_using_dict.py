ab = { 'kim'    :   'kim@naver.com',
       'jay'    :   'jay@naver.com',
       'paul'   :   'paul@daum.net',
       'ruby'   :   'rubydo@hotmail.com'
    }

print "kim's adress is" , ab['kim']


del ab['ruby']

print '\nThere are {} contacts in the ab\n' .format(len(ab))

for name, address in ab.items():
    print 'contact {} at {}'.format(name,address)

ab['guido']= 'guido@guidebox.com'

if 'guido' in ab:
    print "\nguido's address is", ab['guido']
