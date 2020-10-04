# Thanks to "A Byte of Python" by Swaroop Chitlur, "Problem Solving" chapter

import os
import time
import zipfile

# list for files and directories
source = []

while True:
    source.append(input('''Введите путь до файлов, которые Вам нужно заархивировать. Например: C:\Windows
Для имён с пробелами нужно использовать двойные кавычки. Например: "C:\Old dir"
(Для перехода к следующей части программы введите 'c', для выхода введите 'q')\n'''))
    if source.count('c') == 1:
        source.remove('c')
        break
    elif source.count('q') == 1:
        sys.exit()

target_dir = input('Введите путь, куда должен быть помещён архив. Например: C:\Backups\n')

# os.sep: '/'(Linux), '\\'(Windows), ':'(Mac OS)
today = target_dir + os.sep + time.strftime('%Y.%m.%d')
now = time.strftime('%H.%M.%S')

comment = input('Если необходимо, введите комментарий. Для пропуска нажмите "Enter": \n')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# creates directory if it doesn't exist
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)

# creates zipfile for writing
backup = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)

try:
    for path in source:
        # for files
        if os.path.isfile(path):
            backup.write(path)
        else:
            # for directories
            for root, dirs, files in os.walk(path):
                for file in files:
                    backup.write(os.path.join(root, file))
except Exception:
    print('Создание резервной копии НЕ УДАЛОСЬ')
else:
    backup.close()
    print('Резервная копия успешно создана в', target)
    input('Нажмите "Enter" для завершения программы:')
