from os import walk, remove
from os.path import getsize, join
from itertools import groupby


def are_files_duplicates(file_path):
    file_list = [[walk_path[0], walk_file,
                 getsize(join(walk_path[0], walk_file))]
                 for walk_path in walk(file_path)
                 for walk_file in walk_path[2]]
    file_list.sort(key=lambda x: x[1:])
    grouped_files = groupby(file_list, key=lambda x: x[1:])
    for key, group in grouped_files:
        next(group)
        for element in group:
            print('Удаляем дубликат %s, %d bytes'
                  % (join(element[0], element[1]), element[2]))
            remove(join(element[0], element[1]))

if __name__ == '__main__':
    folder = input('Введите путь к каталогу: ')
    are_files_duplicates(folder)
