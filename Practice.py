def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                # temp = a_list[i]
                # a_list[i] = a_list[i + 1]
                # a_list[i + 1] = temp

                #Python支持对两个数字同时进行交换！a,b = b,a就可以交换a和b的值了。
                a_list[i],a_list[i+1] = a_list[i+1], a_list[i]
        pass_num = pass_num - 1


if __name__ == '__main__':
    a_list=[20, 40, 30, 90, 50, 80, 70, 60, 110, 100]
    short_bubble_sort(a_list)
    print(a_list)