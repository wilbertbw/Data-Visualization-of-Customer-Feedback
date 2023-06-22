import numpy as np
import matplotlib.pyplot as plt


bar_width = 0.15
figure = plt.subplots(figsize = (10,6))

brownies = ["1", "2", "3", "4", "5"]

flavor_one = [0,0,5,4,16]
flavor_two = [2,4,4,6,9]
flavor_three = [0,3,4,1,17]
flavor_four = [3,2,5,5,10]

# data cleaning
flavor_one[4] = flavor_one[4] // 2
flavor_two[4] = flavor_two[4] // 2
flavor_three[4] = flavor_three[4] // 2
flavor_four[4] = flavor_four[4] // 2

# setting position of bars
bar_one = np.arange(len(brownies))
bar_two = [x + bar_width for x in bar_one]
bar_three = [x + bar_width for x in bar_two]
bar_four = [x + bar_width for x in bar_three]

plt.bar(bar_one, flavor_one, width = bar_width, label = "Tester A")
plt.bar(bar_two, flavor_two, width = bar_width, label = "Tester B")
plt.bar(bar_three, flavor_three, width = bar_width, label = "Tester C")
plt.bar(bar_four, flavor_four, width = bar_width, label = "Tester D")

plt.xticks(bar_three, brownies)

plt.xlabel("Brownies")
plt.ylabel("FLavor Ratings")
plt.title("Flavor Ratings of Brownies")
plt.legend()

plt.show()