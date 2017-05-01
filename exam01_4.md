# 遞迴(<b>Recursion</b>) #

## 說明 ##

河內塔（Hanoi Tower)是根據一個傳說形成的數學問題：<br>
![hanoi](http://www.sfcc.edu.hk/academic_subjects/mathematics/web/6S/Denise/tower_of_Hanoi_1.gif)
<br>
有三根杆子A，B，C。A杆上有N個(N>1)穿孔圓盤，盤的尺寸由下到上依次變小。要求按下列規則將所有圓盤移至C杆：<br>
1. 每次只能移動一個圓盤。<br>
2. 大盤不能疊在小盤上面。<br>
<br>
提示：可將圓盤臨時置於B杆，也可將從A杆移出的圓盤重新移回A杆，但都必須遵循上述兩條規則。<br>
問：最少要移動多少次？<br>

三層河內塔<br>
![3層](https://raw.githubusercontent.com/pkterry777/python_review/master/Tower_of_Hanoi.gif)
<br>

## Input Format ##

幾層(int)<br>

## Output Format ##

需移動幾次?(int)<br>

## Sample Input 1 ##
```
8

```

## Sample Output 1 ##
```
255
```

## Hint ##

```
請以遞迴的方式寫出這題答案。

```
