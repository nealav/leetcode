def next_time_permute(S):

    hour = int(S[:2])
    min = int(S[3:])
    t1 = S[:2] + S[3:]

    while True:
        min -= 1
        if (min == -1):
            min = 59
            hour -= 1
            if (hour == -1):
                hour = 23
        t2 = ''
        if (hour < 10):
            t2 = t2 + '0' + str(hour)
        else: t2 = t2 + str(hour)
        if (min < 10):
            t2 = t2 + '0' + str(min)
        else: t2 = t2 + str(min)

        if (subset(t1, t2)):
            print(str(t2[:2]) + ':' + str(t2[2:]))
            return t2[:2] + ':' + t2[3:]

def subset(S1, S2):
    l1 = list(S1)
    l2 = list(S2)
    return set(l2).issubset(set(l1))