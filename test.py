names = ['ee', 'eeeeeeee', 'suman', int(33),'tata',55,'yayay']
import gun

for i in names:
    try:
        i = i.replace('ee', 'p')
        print(i)
    except:
        pass

