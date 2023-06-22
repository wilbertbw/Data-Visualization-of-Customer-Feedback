import numpy as np
import matplotlib.pyplot as plt


bar_width = 0.15
figure = plt.subplots(figsize = (10,6))

brownies = ["1", "2", "3", "4", "5"]

aroma_one = [0,0,4,2,19]
aroma_two = [2,3,4,4,12]
aroma_three = [0,4,3,3,15]
aroma_four = [4,1,5,4,11]

# data cleaning
aroma_one[4] = aroma_one[4] // 2
aroma_two[4] = aroma_two[4] // 2
aroma_three[4] = aroma_three[4] // 2
aroma_four[4] = aroma_four[4] // 2

# setting position of bars
bar_one = np.arange(len(brownies))
bar_two = [x + bar_width for x in bar_one]
bar_three = [x + bar_width for x in bar_two]
bar_four = [x + bar_width for x in bar_three]

plt.bar(bar_one, aroma_one, width = bar_width, label = "Tester A")
plt.bar(bar_two, aroma_two, width = bar_width, label = "Tester B")
plt.bar(bar_three, aroma_three, width = bar_width, label = "Tester C")
plt.bar(bar_four, aroma_four, width = bar_width, label = "Tester D")

plt.xticks(bar_three, brownies)

plt.xlabel("Brownies")
plt.ylabel("Aroma Ratings")
plt.title("Aroma Ratings of Brownies")
plt.legend()

plt.show()
