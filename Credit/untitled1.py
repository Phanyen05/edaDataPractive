# sets in python
# dict ={"key": "value"}
set1 ={1,2,3,4,5,6,7,"monday","tuesday"}
set2 ={1,2,3,4,5,6,7,"monday","tuesday",200,100}
set2.difference(set1)


set2.add(1000)
# khong duplicate dc
set2.remove(5)
 #  kiem tra so 10 co trong set 3 khong
10 in set2
# input : neéu ko có 9 và 11 thì thêm số 9  và 11
# nếu ko có số 12 và monday thì thêm số 12
#  còn tất cả trường hợp còn lại thì xóa "tueday"
set5 ={1,2,3,4,5,6,7,"monday","tuesday",200,100}
if 9 and 11 not in set5:
    set5.add(9,11)
elif 12 and "monday" not in set3:
    set5.add(12)

if 9 not in set3:
    if 11 not in set3
        set3.add(9)
        set3.add(11)

if 9 and 11 not in set3:
       set3.add(9)
       set3.add(11)


if 'monday' in set3:
    set3.add(12)
else:
    set3.remove('tueday')
year =[19,20,21]
c= []
for i in year :
   if i==  8 or i ==20:
    c.append(i)
    print(c)
