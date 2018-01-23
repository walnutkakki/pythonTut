shoplist = ['apple', 'mango', 'bigpie']
print 'I have to buy', len(shoplist), 'things in the supermarket'
print 'What I have to buy is', 
for item in shoplist: print item,
print '\n also I have to buy is ', 
shoplist.append('rice'), 
print shoplist
print '\n'
shoplist.sort()
print '\nthis is lists', shoplist

print'\nthis', shoplist[0] 
olditem = shoplist[0]
del shoplist[0]
print olditem, 'is what I bought yesterday'
print '\n', shoplist, 'is my wannabe item today'