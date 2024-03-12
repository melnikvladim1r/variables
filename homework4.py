immutable_var = 1,2,3,4,"enter"
print(immutable_var)
immutable_var = (1,2,3,4,"enter",[100,200,"alt"])
print(immutable_var)
print(immutable_var[1])
print(immutable_var[5])
print(immutable_var[4])
print(immutable_var)
immutable_var[5][2]=300
print(immutable_var)
# immutable_var[4]=5 # не меняет
mutable_list = [1,2,3,4,5,"enter","alt",[10,20,30]]
print(mutable_list)
print(mutable_list[5])
mutable_list[5]=6
print(mutable_list)
print(mutable_list[2:7:2])
mutable_list.append(100)
print(mutable_list)
# immutable_var.append(100)
# print(immutable_var) не меняет
mutable_list.remove(4)
print(mutable_list)
