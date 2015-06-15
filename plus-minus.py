def stats(array,length):
    pos = 0.0
    neg = 0.0
    zero = 0.0
    for i in array:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        elif i == 0:
            zero += 1
    print round(pos / length, 3)
    print round(neg / length, 3)
    print round(zero / length, 3)


data_size = int(raw_input().strip())

data = [int(i) for i in raw_input().strip().split()]

stats(data,data_size)
