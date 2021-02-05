from z3 import *

s = Optimize()
RT01, RT02, RT03, RT04, RT05 = Ints('RT01, RT02, RT03, RT04, RT05')
reqs = [RT01, RT02, RT03, RT04, RT05]
 
# Array size is N.
# No value can be less than 0 or more than N. Representing index numbers in an array with the span of 0 - N.
for i in (reqs):
   s.add(i >= 0)

for i in (reqs):
   s.add(i < len(reqs))


#No duplications, only distinct unique values.
d = Distinct(RT01, RT02, RT03, RT04, RT05)
s.add(d)

#Prioritization
s.add_soft(RT01 < RT04, 1)
s.add_soft(RT01 < RT05, 1)
s.add_soft(RT01 < RT02, 1)
s.add_soft(RT01 < RT03, 1)

s.add_soft(RT04 < RT02, 1)
s.add_soft(RT04 < RT03, 1)

s.add_soft(RT05 < RT02, 1)
s.add_soft(RT05 < RT03, 1)

#Dependencies

s.add_soft(RT03 < RT02, 1)
s.add_soft(RT03 < RT01, 1)
s.add_soft(RT03 < RT04, 1)

s.add_soft(RT02 < RT01, 1)
s.add_soft(RT02 < RT04, 1)





#Get all lists with same minimum cost, maximum size 10.
cost = 0
currentcost = 0
for i in range (10):
    s.check()
    m = s.model()
    cost = m.evaluate(s.objectives()[0]).as_long()
    if cost <= currentcost or i == 1 :
     requirements_list = {
      "RT01" : m[RT01].as_long(),
      "RT02" : m[RT02].as_long(),
      "RT03" : m[RT03].as_long(),
      "RT04" : m[RT04].as_long(),
      "RT05" : m[RT05].as_long(),
       }
     currentcost = cost


   #Sort the list so that the prioritization is in descending order.
     sorted_list = sorted(requirements_list.items() , key=lambda x: x[1])


   #Ignore the previous models
     s.add(Or(RT01 != s.model()[RT01], RT02 != s.model()[RT02], RT03 != s.model()[RT03], RT04 != s.model()[RT04], RT05 != s.model()[RT05]))


   #Print the requirementslist
     print("Requirement order ", i)
     for key in sorted_list:
       print(key[0])
       


  #Print the cost.
     print("Cost: ", cost)
     print("---------------------------------------")
print("No more sets with the same minimum cost")
