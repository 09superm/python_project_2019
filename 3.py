import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from matplotlib import style

# 그래프 만들기
font_name = font_manager.FontProperties(fname="/System/Library/Fonts/AppleSDGothicNeo.ttc").get_name()
rc('font', family=font_name)
style.use('ggplot')

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
labels = your_input
ratio = gmvpwgt
explode = (0.1, 0.1, 0.1, 0.1, 0.1)

plt.title("Global Minimum Volatility Portfolio\n")
plt.pie(ratio, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()
