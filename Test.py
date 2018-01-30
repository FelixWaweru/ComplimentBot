import codecs

a = [1,2,3,4]
i = 0
with codecs.open('test.txt', 'w') as followerText:
    while i != 3:
        followerText.write(str(a[i]) + "\n")
        print("Done")
        i = i+1
