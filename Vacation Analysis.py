#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Exercise - Data Analysis for Vacation Planning

''''You're planning a vacation, and you need to decide which city you want to visit. You have shortlisted four cities and identified the return flight cost, daily hotel cost, and weekly car rental cost. While renting a car, you need to pay for entire weeks, even if you return the car sooner.


| City | Return Flight (`$`) | Hotel per day (`$`) | Weekly Car Rental  (`$`) | 
|------|--------------------------|------------------|------------------------|
| Paris|       200                |       20         |          200           |
| London|      250                |       30         |          120           |
| Dubai|       370                |       15         |          80           |
| Mumbai|      450                |       10         |          70           |         


Answer the following questions using the data above:

1. If you're planning a 1-week long trip, which city should you visit to spend the least amount of money?
2. How does the answer to the previous question change if you change the trip's duration to four days, ten days or two weeks?
3. If your total budget for the trip is `$1000`, which city should you visit to maximize the duration of your trip? Which city should you visit if you want to minimize the duration?
4. How does the answer to the previous question change if your budget is `$600`, `$2000`, or `$1500`?

*Hint: To answer these questions, it will help to define a function `cost_of_trip` with relevant inputs like flight cost, hotel rate, car rental rate, and duration of the trip. You may find the `math.ceil` function useful for calculating the total cost of car rental.*'''


# In[5]:


def cost_of_trip(hotel_rent,duration,weekly_car_rent,flight_cost):
    cost = (hotel_rent)*duration+weekly_car_rent+flight_cost
    cost = math.ceil(cost)
    return cost




city1 = input("Enter the name of city:")   
cost1=cost_of_trip(20,7,200,200)
print("Trip to {} cost:{} ".format(city1,cost1))
city2 = input("Enter the name of city:")   
cost2=cost_of_trip(30,7,120,250)
print("Trip to {} cost:{}".format(city2,cost2))
city3 = input("Enter the name of city:")   
cost3=cost_of_trip(15,7,80,370)
print("Trip to {} cost:{}".format(city3,cost3))
city4 = input("Enter the name of city:")   
cost4=cost_of_trip(10,7,70,450)
print("Trip to {} cost:{}".format(city4,cost4))


if (cost1<cost2 and cost1<cost3 and cost1<cost4):
    print(city1+' is cheaper with the cost {}'.format(cost1))
if cost2<cost1 and cost2<cost3 and cost2<cost4:
    print(city1+' is cheaper with the cost {}'.format(cost1))
elif cost3<cost2 and cost3<cost1 and cost3<cost4:
    print(city3+' is cheaper with the cost {}'.format(cost3))
elif cost4<cost2 and cost4<cost1 and cost4<cost1:
    print(city4+' is cheaper with the cost {}'.format(cost4))


# In[ ]:


#for 4days
city1 = input("Enter the name of city:")   
cost1=cost_of_trip(20,4,200,200)
print("Trip to {} cost:{}".format(city1,cost1))
city2 = input("Enter the name of city:")   
cost2=cost_of_trip(30,4,120,250)
print("Trip to {} cost:{}".format(city2,cost2))
city3 = input("Enter the name of city:")   
cost3=cost_of_trip(15,4,80,370)
print("Trip to {} cost:{}".format(city3,cost3))
city4 = input("Enter the name of city:")   
cost4=cost_of_trip(10,4,70,450)
print("Trip to {} cost:{}".format(city4,cost4))

if (cost1<cost2 and cost1<cost3 and cost1<cost4):
    print(city1+' is cheaper with the cost {}'.format(cost1))
if cost2<cost1 and cost2<cost3 and cost2<cost4:
    print(city1+' is cheaper with the cost {}'.format(cost1))
elif cost3<cost2 and cost3<cost1 and cost3<cost4:
    print(city3+' is cheaper with the cost {}'.format(cost3))
elif cost4<cost2 and cost4<cost1 and cost4<cost1:
    print(city4+' is cheaper with the cost {}'.format(cost4))


# In[ ]:


#for 10 days
city1 = input("Enter the name of city:")   
cost1=cost_of_trip(20,10,200,200)
print("Trip to {} cost:{}".format(city1,cost1))
city2 = input("Enter the name of city:")   
cost2=cost_of_trip(30,10,120,250)
print("Trip to {} cost:{}".format(city2,cost2))
city3 = input("Enter the name of city:")   
cost3=cost_of_trip(15,10,80,370)
print("Trip to {} cost:{}".format(city3,cost3))
city4 = input("Enter the name of city:")   
cost4=cost_of_trip(10,10,70,450)
print("Trip to {} cost:{}".format(city4,cost4))

if (cost1<cost2 and cost1<cost3 and cost1<cost4):
    print(city1+' is cheaper with the cost {}'.format(cost1))
if cost2<cost1 and cost2<cost3 and cost2<cost4:
    print(city1+' is cheaper with the cost {}'.format(cost1))
elif cost3<cost2 and cost3<cost1 and cost3<cost4:
    print(city3+' is cheaper with the cost {}'.format(cost3))
elif cost4<cost2 and cost4<cost1 and cost4<cost1:
    print(city4+' is cheaper with the cost {}'.format(cost4))


# In[ ]:


#for 14 days
city1 = input("Enter the name of city:")   
cost1=cost_of_trip(20,14,200,200)
print("Trip to {} cost:{}".format(city1,cost1))
city2 = input("Enter the name of city:")   
cost2=cost_of_trip(30,14,120,250)
print("Trip to {} cost:{}".format(city2,cost2))
city3 = input("Enter the name of city:")   
cost3=cost_of_trip(15,14,80,370)
print("Trip to {} cost:{}".format(city3,cost3))
city4 = input("Enter the name of city:")   
cost4=cost_of_trip(10,14,70,450)
print("Trip to {} cost:{}".format(city4,cost4))


if (cost1<cost2 and cost1<cost3 and cost1<cost4):
    print(city1+' is cheaper with the cost {}'.format(cost1))
elif cost2<cost1 and cost2<cost3 and cost2<cost4:
    print(city1+' is cheaper with the cost {}'.format(cost1))
elif cost3<cost2 and cost3<cost1 and cost3<cost4:
    print(city3+' is cheaper with the cost {}'.format(cost3))
elif cost4<cost2 and cost4<cost1 and cost4<cost1:
    print(city4+' is cheaper with the cost {}'.format(cost4))


# In[ ]:


budget=1000

city1 = input("Enter the name of city:")   
cost1=cost_of_trip(20,7,200,200)
rem1 = budget-cost1
print("Trip to {} cost:{} with the remainder of amount: {}".format(city1,cost1,rem1))

city2 = input("Enter the name of city:")   
cost2=cost_of_trip(30,7,120,250)
rem2 = budget-cost2
print("Trip to {} cost:{} with the remainder of amount: {}".format(city2,cost2,rem2))

city3 = input("Enter the name of city:")   
cost3=cost_of_trip(15,7,80,370)
rem3 = budget-cost3
print("Trip to {} cost:{} with the remainder of amount: {}".format(city3,cost3,rem3))

city4 = input("Enter the name of city:")   
cost4=cost_of_trip(10,7,70,450)
rem4 = budget-cost4
print("Trip to {} cost:{} with the remainder of amount: {}".format(city4,cost4,rem4))


if (cost1<cost2 and cost1<cost3 and cost1<cost4):
    print(city1+' is cheaper with the cost {}'.format(cost1))
if cost2<cost1 and cost2<cost3 and cost2<cost4:
    print(city1+' is cheaper with the cost {}'.format(cost1))
elif cost3<cost2 and cost3<cost1 and cost3<cost4:
    print(city3+' is cheaper with the cost {}'.format(cost3))
elif cost4<cost2 and cost4<cost1 and cost4<cost1:
    print(city4+' is cheaper with the cost {}'.format(cost4))
if (rem1<rem2 and rem1<rem3 and rem1<rem4):
    print(city1+' to minimize the duration of our trip with the spare money {}'.format(rem1))
if (rem2<rem1 and rem2<rem3 and rem2<rem4):
    print(city2+' to minimize the duration of our trip with the spare money {}'.format(rem2))
if (rem3<rem2 and rem3<rem1 and rem3<rem4):
    print(city3+' to minimize the duration of our trip with the spare money {}'.format(rem3))
if (rem4<rem2 and rem4<rem3 and rem4<rem1):
    print(city4+' to minimize the duration of our trip with the spare money {}'.format(rem4))
if (rem1>rem2 and rem1>rem3 and rem1>rem4):
    print(city1+' to maximize the duration of our trip with the spare money {}'.format(rem1))
if (rem2>rem1 and rem2>rem3 and rem2>rem4):
    print(city2+' to maximize the duration of our trip with the spare money {}'.format(rem2))
if (rem3>rem2 and rem3>rem1 and rem3>rem4):
    print(city3+' to maximize the duration of our trip with the spare money {}'.format(rem3))
if (rem4>rem2 and rem4>rem3 and rem4>rem1):
    print(city4+' to maximize the duration of our trip with the spare money {}'.format(rem4))


# In[ ]:


budget=600


city1 = input("Enter the name of city:")   
cost1=cost_of_trip(20,7,200,200)
rem1 = budget-cost1
print("Trip to {} cost:{} with the remainder of amount: {}".format(city1,cost1,rem1))

city2 = input("Enter the name of city:")   
cost2=cost_of_trip(30,7,120,250)
rem2 = budget-cost2
print("Trip to {} cost:{} with the remainder of amount: {}".format(city2,cost2,rem2))

city3 = input("Enter the name of city:")   
cost3=cost_of_trip(15,7,80,370)
rem3 = budget-cost3
print("Trip to {} cost:{} with the remainder of amount: {}".format(city3,cost3,rem3))

city4 = input("Enter the name of city:")   
cost4=cost_of_trip(10,7,70,450)
rem4 = budget-cost4
print("Trip to {} cost:{} with the remainder of amount: {}".format(city4,cost4,rem4))


if (cost1<cost2 and cost1<cost3 and cost1<cost4):
    print(city1+' is cheaper with the cost {}'.format(cost1))
if cost2<cost1 and cost2<cost3 and cost2<cost4:
    print(city1+' is cheaper with the cost {}'.format(cost1))
elif cost3<cost2 and cost3<cost1 and cost3<cost4:
    print(city3+' is cheaper with the cost {}'.format(cost3))
elif cost4<cost2 and cost4<cost1 and cost4<cost1:
    print(city4+' is cheaper with the cost {}'.format(cost4))
if (rem1<rem2 and rem1<rem3 and rem1<rem4):
    print(city1+' to minimize the duration of our trip with the spare money {}'.format(rem1))
if (rem2<rem1 and rem2<rem3 and rem2<rem4):
    print(city2+' to minimize the duration of our trip with the spare money {}'.format(rem2))
if (rem3<rem2 and rem3<rem1 and rem3<rem4):
    print(city3+' to minimize the duration of our trip with the spare money {}'.format(rem3))
if (rem4<rem2 and rem4<rem3 and rem4<rem1):
    print(city4+' to minimize the duration of our trip with the spare money {}'.format(rem4))
if (rem1>rem2 and rem1>rem3 and rem1>rem4):
    print(city1+' to maximize the duration of our trip with the spare money {}'.format(rem1))
if (rem2>rem1 and rem2>rem3 and rem2>rem4):
    print(city2+' to maximize the duration of our trip with the spare money {}'.format(rem2))
if (rem3>rem2 and rem3>rem1 and rem3>rem4):
    print(city3+' to maximize the duration of our trip with the spare money {}'.format(rem3))
if (rem4>rem2 and rem4>rem3 and rem4>rem1):
    print(city4+' to maximize the duration of our trip with the spare money {}'.format(rem4))


# In[ ]:


budget=2000


city1 = input("Enter the name of city:")   
cost1=cost_of_trip(20,7,200,200)
rem1 = budget-cost1
print("Trip to {} cost:{} with the remainder of amount: {}".format(city1,cost1,rem1))

city2 = input("Enter the name of city:")   
cost2=cost_of_trip(30,7,120,250)
rem2 = budget-cost2
print("Trip to {} cost:{} with the remainder of amount: {}".format(city2,cost2,rem2))

city3 = input("Enter the name of city:")   
cost3=cost_of_trip(15,7,80,370)
rem3 = budget-cost3
print("Trip to {} cost:{} with the remainder of amount: {}".format(city3,cost3,rem3))

city4 = input("Enter the name of city:")   
cost4=cost_of_trip(10,7,70,450)
rem4 = budget-cost4
print("Trip to {} cost:{} with the remainder of amount: {}".format(city4,cost4,rem4))


if (cost1<cost2 and cost1<cost3 and cost1<cost4):
    print(city1+' is cheaper with the cost {}'.format(cost1))
if cost2<cost1 and cost2<cost3 and cost2<cost4:
    print(city1+' is cheaper with the cost {}'.format(cost1))
elif cost3<cost2 and cost3<cost1 and cost3<cost4:
    print(city3+' is cheaper with the cost {}'.format(cost3))
elif cost4<cost2 and cost4<cost1 and cost4<cost1:
    print(city4+' is cheaper with the cost {}'.format(cost4))
if (rem1<rem2 and rem1<rem3 and rem1<rem4):
    print(city1+' to minimize the duration of our trip with the spare money {}'.format(rem1))
if (rem2<rem1 and rem2<rem3 and rem2<rem4):
    print(city2+' to minimize the duration of our trip with the spare money {}'.format(rem2))
if (rem3<rem2 and rem3<rem1 and rem3<rem4):
    print(city3+' to minimize the duration of our trip with the spare money {}'.format(rem3))
if (rem4<rem2 and rem4<rem3 and rem4<rem1):
    print(city4+' to minimize the duration of our trip with the spare money {}'.format(rem4))
if (rem1>rem2 and rem1>rem3 and rem1>rem4):
    print(city1+' to maximize the duration of our trip with the spare money {}'.format(rem1))
if (rem2>rem1 and rem2>rem3 and rem2>rem4):
    print(city2+' to maximize the duration of our trip with the spare money {}'.format(rem2))
if (rem3>rem2 and rem3>rem1 and rem3>rem4):
    print(city3+' to maximize the duration of our trip with the spare money {}'.format(rem3))
if (rem4>rem2 and rem4>rem3 and rem4>rem1):
    print(city4+' to maximize the duration of our trip with the spare money {}'.format(rem4)) 


# In[ ]:


budget=1500


city1 = input("Enter the name of city:")   
cost1=cost_of_trip(20,7,200,200)
rem1 = budget-cost1
print("Trip to {} cost:{} with the remainder of amount: {}".format(city1,cost1,rem1))

city2 = input("Enter the name of city:")   
cost2=cost_of_trip(30,7,120,250)
rem2 = budget-cost2
print("Trip to {} cost:{} with the remainder of amount: {}".format(city2,cost2,rem2))

city3 = input("Enter the name of city:")   
cost3=cost_of_trip(15,7,80,370)
rem3 = budget-cost3
print("Trip to {} cost:{} with the remainder of amount: {}".format(city3,cost3,rem3))

city4 = input("Enter the name of city:")   
cost4=cost_of_trip(10,7,70,450)
rem4 = budget-cost4
print("Trip to {} cost:{} with the remainder of amount: {}".format(city4,cost4,rem4))


if (cost1<cost2 and cost1<cost3 and cost1<cost4):
    print(city1+' is cheaper with the cost {}'.format(cost1))
if cost2<cost1 and cost2<cost3 and cost2<cost4:
    print(city1+' is cheaper with the cost {}'.format(cost1))
elif cost3<cost2 and cost3<cost1 and cost3<cost4:
    print(city3+' is cheaper with the cost {}'.format(cost3))
elif cost4<cost2 and cost4<cost1 and cost4<cost1:
    print(city4+' is cheaper with the cost {}'.format(cost4))
if (rem1<rem2 and rem1<rem3 and rem1<rem4):
    print(city1+' to minimize the duration of our trip with the spare money {}'.format(rem1))
if (rem2<rem1 and rem2<rem3 and rem2<rem4):
    print(city2+' to minimize the duration of our trip with the spare money {}'.format(rem2))
if (rem3<rem2 and rem3<rem1 and rem3<rem4):
    print(city3+' to minimize the duration of our trip with the spare money {}'.format(rem3))
if (rem4<rem2 and rem4<rem3 and rem4<rem1):
    print(city4+' to minimize the duration of our trip with the spare money {}'.format(rem4))
if (rem1>rem2 and rem1>rem3 and rem1>rem4):
    print(city1+' to maximize the duration of our trip with the spare money {}'.format(rem1))
if (rem2>rem1 and rem2>rem3 and rem2>rem4):
    print(city2+' to maximize the duration of our trip with the spare money {}'.format(rem2))
if (rem3>rem2 and rem3>rem1 and rem3>rem4):
    print(city3+' to maximize the duration of our trip with the spare money {}'.format(rem3))
if (rem4>rem2 and rem4>rem3 and rem4>rem1):
    print(city4+' to maximize the duration of our trip with the spare money {}'.format(rem4))

