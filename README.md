# Python-Crawler-with-RE

## 程式說明
1. [\s\S]\*?\</p>的\*?  
意思是任意長度的最短匹配(non-greedy)  
2. str.split(' ',2)  
意思是以空格為區隔方式，區隔2次(變成3個)，預設為空白符(包含\n等)及最大分割數  
3. str.strip('0')  
把頭尾的很多0去掉，預設為空白符  
4. title=r.split("title is-5 mathjax\">")[1].split("\</p>")[0].strip()  
為取一個區間的辦法，然後再去掉頭尾  
