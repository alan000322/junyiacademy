# 何家慈_均一平台教育基金會平台發展組_實習生遠端筆試
## 1. 
解答如Q1.py
## 2. 
解答如Q2.py
## 3. 
解答：
1. 假設袋子上標示鉛筆、標示原子筆、標示混合分別為A,B,C，並假設實際袋裡的物品為鉛筆、原子筆、混合分別為a,b,c
2. 若在沒有條件限制下，A,B,C與a,b,c兩組進行配對，會有3x2x1=6種可能。但依照題意，A不能跟a在一起、B不能跟b在一起、C不能跟c在一起，則因此會發現剩下兩種可能：
```
    (1)「A配對到b，B配對到c、C配對到a」:號稱是鉛筆袋，內容為原子筆；號稱為原子筆袋，內容為混合；號稱為混合袋，但內容只有鉛筆。
    (2)「A配對到c，B配對到a、C配對到b」:號稱是鉛筆袋，內容為混合　；號稱為原子筆袋，內容為鉛筆；號稱為混合袋，但內容只有原子筆。
```
3. 因此：
```
若隨機拿到號稱為鉛筆　的袋子：抽到是鉛筆的話，　必為第(2)狀況；抽到是原子筆的話，狀況不明
若隨機拿到號稱為原子筆的袋子：抽到是原子筆的話，必為第(1)狀況；抽到是鉛筆　的話，狀況不明
若隨機拿到號稱為混合　的袋子：抽到是鉛筆的話，　必為第(1)狀況；抽到是原子筆的話，必為第(2)狀況
```
## 4. 
雖然看起來題目敘述是對的，然而實際上確實存在一些錯誤。

重新審視到底消費者端的角度而言：
原先要價900元，實際只要750元，但服務員暗槓60元，也就是說實際上，消費者「以為」便宜90元，總價為810元，也就是為什麼服務員退還90元。
也就是說，這810元（三人分的話，1人需付270元），**再加上**服務員退還的**90元**，才會是900元，而非去加服務員暗槓的60元。
