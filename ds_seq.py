shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# Indexing or 'Subscription' operation #
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]
print 'Character 0 is', name[0]
# Slicing on a list #
print 'Item 1 to 3 is', shoplist[1:3]   # 1 to 3 is 1 and 2
print 'Item 2 to end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1] # 1 to -1 is 1 and -2
print 'Item start to end is', shoplist[:] #[a:b:c] - a = from / b = to (but there's no b value, like '<' ) / c = step / if [1:5:2] there'll be 1 3  
print 'Special example', shoplist[0:3:3] # only 1st value, apple
# Slicing on a string #
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]