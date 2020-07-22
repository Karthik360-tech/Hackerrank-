def timeConversion(s):
    #
    # Write your code here.
    #
    ans = ''
    list = []
    for i in range(len(s)):
        ans += s[i]
        if i != 0 and i%3 != 0 :
            ans += ' '

    list.extend(ans.rstrip().split())
    if list[5] == 'P':
        if list[0] == '12' :
             list.__delitem__(5)
             list.pop()
        else :
            list[0] = int(list[0])
            list[0] += 12
            list.__delitem__(5)
            list.pop()
    elif list[5] == 'A':
        if list[0] <= '11':
            list.__delitem__(5)
            list.pop()
        elif list[0] == '12' :
            list[0] = '00'
            list.__delitem__(5)
            list.pop()
    answer = ''.join(str(e) for e in list)
    return(answer)

print(timeConversion('06:43:44PM'))