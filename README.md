# RA_work
Итоговая работа по курсу Rubius. Файловый менеджер.

В папке CommandLineApp готовое приложение командной строки с функциями файлового менеджера + серверную часть. (запускать main из этой папки)

После запуска сервера вывести набор команд можно командой HELP.

## Команда 
### GET_FILES
Выводит список всех файлов из директории запуска программы.

Атрибуты:
- HELP -- выводит справку о команде;
- {folder_name} -- имя папки, из которой хотим получить список файлов; если папка по указанному адресу будетне найдена, программа выдаст соотвествующее предупреждение.
- при вводе неизвестного атрибута, пойвится предупреждение о неизвестной команде.

Ответы сервера:
- OK -- команда выполнена;
- Unknown command: {command_name} -- неизвестная команда;
- Access denied -- доступ к указанной директории запрещен.

### PUT_FOLDER {folder_name}
Добавлет новую папку в указанную директорию. Команда с обязательным атрибутом в виде пути создания папки.
При использовании без атрибутов, получим ошибку: ERROR: no attribute in command. Use HELP attribute.

Атрибуты:
- HELP -- выводит справку о команде;
- {folder_name} -- имя папки с путем для создания; если такая папка уже существует, то увидим ошибку.
- при вводе неизвестного атрибута, появится предупреждение о неизвестной команде.

Ответы сервера:
- OK -- команда выполнена;
- ERROR: no attribute in command. Use HELP attribute -- не задан атрибут к команде, посмотрите справку; 
- ERROR: "{name}" is already exists -- данное имя уже существует;
- Unknown command: {command_name} -- неизвестная команда.

### DELETE_FOLDER {folder_name}
Удаляет указанную папку.
Команда с обязательным атрибутом в виде пути к папке.
При использовании без атрибутов, получим ошибку: ERROR: no attribute in command. Use HELP attribute.

Атрибуты:
- HELP -- выводит справку о команде;
- {folder_name} -- имя папки с путем для удаления; если такая папка не существует, то увидим ошибку;
- при вводе неизвестного атрибута, появится предупреждение о неизвестной команде.

Ответы сервера:
- OK -- команда выполнена;
- ERROR: no attribute in command. Use HELP attribute -- не задан атрибут к команде, посмотрите справку; 
- ERROR: Folder "{name}" not found. -- данное имя не существует;
- Unknown command: {command_name} -- неизвестная команда.

### PUT_FILE {file_name}
Добавлет новый файл в указанную директорию. 
Команда с обязательным атрибутом в виде пути создания файла.
При использовании без атрибутов, получим ошибку: ERROR: no attribute in command. Use HELP attribute.

Атрибуты:
- HELP -- выводит справку о команде;
- {file_name} -- имя файла с путем для создания; если такой файл уже существует, то увидим ошибку;
- при вводе неизвестного атрибута, появится предупреждение о неизвестной команде.

Ответы сервера:
- OK -- команда выполнена;
- ERROR: no attribute in command. Use HELP attribute -- не задан атрибут к команде, посмотрите справку; 
- ERROR: "{name}" is already exists -- данное имя уже существует;
- Unknown command: {command_name} -- неизвестная команда;

### DELETE_FILE {file_name}
Удаляет указанный файл.
Команда с обязательным атрибутом в виде пути к файлу.
При использовании без атрибутов, получим ошибку: ERROR: no attribute in command. Use HELP attribute.

Атрибуты:
- HELP -- выводит справку о команде;
- {file_name} -- имя файла с путем для удаления; если такой файл не существует, то увидим ошибку;
- при вводе неизвестного атрибута, появится предупреждение о неизвестной команде.

Ответы сервера:
- OK -- команда выполнена;
- ERROR: no attribute in command. Use HELP attribute -- не задан атрибут к команде, посмотрите справку; 
- ERROR: File "{name}" not found. -- данное имя не существует;
- Unknown command: {command_name} -- неизвестная команда.

### OPEN_FILE {file_name}
Показывает содержимое указанного файла.
Команда с обязательным атрибутом в виде пути к файлу.
При использовании без атрибутов, получим ошибку: ERROR: no attribute in command. Use HELP attribute.

Атрибуты:
- HELP -- выводит справку о команде;
- {file_name} -- имя файла с путем для откытия; если такой файл не существует, то увидим ошибку;
- при вводе неизвестного атрибута, появится предупреждение о неизвестной команде.

Ответы сервера:
- OK -- команда выполнена;
- ERROR: no attribute in command. Use HELP attribute -- не задан атрибут к команде, посмотрите справку; 
- ERROR: File "{name}" not found. -- данное имя не существует;
- Unknown command: {command_name} -- неизвестная команда.

### ADD_TO_FILE {file_name} {data}
Записывает в указанный файл указанные данные.
Команда с обязательными атрибутами в виде пути файла.
При использовании без атрибутов, получим ошибку: ERROR: no attribute in command. Use HELP attribute.

Атрибуты:
- HELP -- выводит справку о команде;
- {file_name} -- имя файла с путем до него; если такой файл не существует, то увидим ошибку;
- {data} -- данные для записи в файл.
- при вводе неизвестного атрибута, появится предупреждение о неизвестной команде.

Ответы сервера:
- OK -- команда выполнена;
- ERROR: no attribute in command. Use HELP attribute -- не задан атрибут к команде, посмотрите справку; 
- ERROR: File "{name}" not found. -- данное имя не существует;
- Unknown command: {command_name} -- неизвестная команда.