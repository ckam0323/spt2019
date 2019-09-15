with open('/root/nsd1904/tn914/dl.py') as f1:
    set1 = set(f1)

with open('/root/nsd1904/devops03/download.py') as f2:
    set2 = set(f2)

print(set2 - set1)

with open('/root/chongfu.txt','w') as f3:
    f3.writelines(set2 - set1)
