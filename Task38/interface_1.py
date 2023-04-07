from inputdata import *  
def interface():     
    print("""1 - добавление, 
    2 - поиск,  
    3 - вывод на экран,  
    4 - импорт в файл,   
    5 - удаление записи,   
    6 - изменить запись """) 
    ask = int(input()) 
    if ask == 1:     
        input_data() 
    elif ask == 2:     
        search() 
    elif ask == 3:     
        print_data() 
    elif ask == 4:     
        load() 
    elif ask==5:
        delete_line()
    elif ask==6:
        change_line()
    else:     
        print("нет такой команды")