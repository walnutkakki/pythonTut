print 'simpleguy'
shoplist = ['bob','pang','myun']
mylist=shoplist

del shoplist[0]

print 'the rest things are', shoplist
print 'mylist is', mylist

print '\n\n this is full copy example'
mylist = shoplist[:]    #참조하게되어서 

del mylist[0]

print 'the rest things are', shoplist
print 'mylist is ', mylist

