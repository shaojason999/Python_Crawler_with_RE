# Python-Crawler-with-RE

## 程式說明
1. [\s\S]\*?\</p>的\*?  
意思是任意長度的最短匹配(non-greedy)  
2. str.split(' ',2)  
意思是以空格為區隔方式，區隔2次(變成3個)，預設為空白符(包含\n等)及最大分割數  
3. str.strip('0')  
把頭尾的很多0去掉，預設為空白符  
4. title=r.split("title is-5 mathjax\">")[1].split("\</p>")[0].strip()  
為取一個區間的辦法，然後再去掉頭尾空格  

## 畫圖套件
1. 安裝畫圖用的matplotlib.pyplot
```
$ sudo pip install --upgrade pip
$ sudo pip install matplotlib
$ sudo apt install python3-tk
```
2. 畫圖方式
```python
import matplotlib.pyplot as plt
x=[1,2,3]
y=[1,2,3]
#設定y軸刻度為1，範圍為0~3
plt.yticks(range(0,3+1,1))
plt.bar(x,y)
plt.show()
```
參考資料  
[No module named _tkinter](https://blog.csdn.net/blueheart20/article/details/78763208)  
[Changing the “tick frequency” on x or y axis in matplotlib?](https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib)  
