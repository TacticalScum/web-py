def path_cutter (request):
    temp_array = []

    delimiter = None
    for i in range(len(request)-1, -1, -1):
        temp_array.insert(0, request[i])
    
    for i in range(len(request)-1, -1, -1):
        if request[i] == '\\' :
            delimiter = i+1
            break 
    temp_array = temp_array[slice(delimiter)]
    file_path = ''.join(str(x) for x in temp_array)
    temp_array.clear()

    for i in range(len(request)-1, -1, -1):
        if request[i] == '\\' :
            break
        else:
            temp_array.insert(0, request[i])
    file_name = ''.join(str(x) for x in temp_array)
    temp_array.clear()

    for i in range(len(request)-1, -1, -1):
        if request[i] == '.' :
            temp_array.insert(0, request[i])
            break
        else:
            temp_array.insert(0, request[i])
    file_extension = ''.join(str(x) for x in temp_array)

    path = ('Путь', file_path)
    name = ('Имя', file_name)
    extension = ('Расширение', file_extension)

    return path, extension, name


file_path = 'C:\\Windows\\System32\\drivers\\etc\\ReadMe.txt'
print(path_cutter(file_path))
