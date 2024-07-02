def string(str1, str2):
    str1l=len(str1)
    str2l=len(str2)

    for i in range(0, (str1l-str2l+1)):
        j=0
        while j<str2l and str1[i+j]==str2[j]:
            j=j+1
        if j==str2l:
            return i
    return -1

res=string("hello", "llo")
print(res)