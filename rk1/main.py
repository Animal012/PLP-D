import re


class CD_Disk:
    def __init__(self, id_number, name, memory_size, lib_id):
        self.id_number = id_number
        self.name = name
        self.memory_size = memory_size
        self.lib_id = lib_id


class LibOfCD:
    def __init__(self, id_number, name):
        self.id = id_number
        self.name = name


class Disk_Lib:
    def __init__(self, lib_id, cd_id):
        self.lib_id = lib_id
        self.cd_id = cd_id


libs = [
    LibOfCD(1, "Central Library"),
    LibOfCD(2, "West Library"),
    LibOfCD(3, "East Library"),
    LibOfCD(4, "North Library"),
    LibOfCD(5, "South Library")
]


disks = [
    CD_Disk(1, "The Godfather", 16384, 1),
    CD_Disk(2, "The Shawshank Redemption", 1024, 2),
    CD_Disk(3, "Taxi Driver", 1024, 3),
    CD_Disk(4, "Schindler's List", 8192, 1),
    CD_Disk(5, "One Flew Over the Cuckoo's Nest", 2048, 2),
    CD_Disk(6, "The Godfather Part II", 512, 1),
    CD_Disk(7, "Se7en", 512, 3),
    CD_Disk(8, "Inception", 2048, 4),
    CD_Disk(9, "Goodfellas", 1024, 4),
    CD_Disk(10, "The Silence of the Lambs", 4096, 5)
]

lib_disk = [
    Disk_Lib(1, 1),
    Disk_Lib(2, 2),
    Disk_Lib(3, 3),
    Disk_Lib(1, 4),
    Disk_Lib(2, 5),
    Disk_Lib(1, 6),
    Disk_Lib(3, 7),
    Disk_Lib(4, 8),
    Disk_Lib(4, 9),
    Disk_Lib(5, 10)
]


def main():
    # Соединение данных один-ко-многим
    one_to_many = [(d.name, d.memory_size, lib.name)
                   for lib in libs
                   for d in disks
                   if d.lib_id == lib.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(lib.name, dl.lib_id, dl.cd_id)
                         for lib in libs
                         for dl in lib_disk
                         if lib.id == dl.lib_id]
    many_to_many = [(d.name, d.memory_size, lib_name)
                    for lib_name, lib_id, disk_id in many_to_many_temp
                    for d in disks if d.id_number == disk_id]

    print('Задание Д1')
    res_11 = []
    for disk_name, memory_size, lib_name in one_to_many:
        matches = re.findall(r'\b\w+st\b', disk_name)
        if matches:
            res_11.append((disk_name, lib_name))
    print(res_11)
    # средний размер диска в библиотеке
    print('\nЗадание Д2')
    res_12 = {}
    for lib in libs:
        l_disks = list(filter(lambda i: i[2] == lib.name, one_to_many))
        if len(l_disks) > 0:
            l_disks_size = [x for _, x, _ in l_disks]
            res_12[lib.name] = int(sum(l_disks_size)/len(l_disks_size))
    print(sorted(res_12.items(), key=lambda item: item[1]))
    print('\nЗадание Д3')
    res_13 = {}
    for lib in libs:
        if lib.name[0] == 'C':
            l_disks = list(filter(lambda i: i[2] == lib.name, many_to_many))
            l_disks_names = [x for x, _, _ in l_disks]
            res_13[lib.name] = l_disks_names
    print(res_13)


if __name__ == '__main__':
    main()