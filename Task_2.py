file_list = ['1.txt', '2.txt', '3.txt']
list_1 = []


def open_file(file_name):

    for i in file_name:
        path = i
        print(path)
        with open(path, 'r', encoding='utf-8') as f:
            a = (f.readlines())
            test_list = {
                path: a
            }
        list_1.append(test_list)


def write_file(file_name):
    with open('write.txt', 'w', encoding='utf-8') as f:
        for i in file_name:
            f.write(str(*i.keys()))
            f.write('\n')
            f.write(str(len(*i.values())))
            f.write('\n')
            for a in i.values():
                for b in a:
                    f.write(b)
                f.write('\n')


open_file(file_list)
write_file(list_1)


def get_data(x):
    return len(str(x.values()))


list_2 = sorted(list_1, key=get_data)

open_file(file_list)
write_file(list_2)
