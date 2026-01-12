coffee = [2,3,1,2,4]
sleep = [7,6,8,7.5,5.5]

mean_coffee = sum(coffee)/len(coffee)
mean_sleep = sum(sleep)/len(sleep)

sorted_coffee = sorted(coffee)
sorted_sleep = sorted(sleep)

md_coffee = sorted_coffee[2]
md_sleep = sorted_sleep[2]

print(f"average cups of coffee: {mean_coffee} | median: {md_coffee}")
print(f"average hours of sleep: {mean_sleep} | median: {md_sleep}")
