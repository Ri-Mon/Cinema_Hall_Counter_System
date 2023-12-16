class Star_Cinema:
    __hall_list = [] #class attribute

    def entry_hall(self, obj): # for inserting object of hall class
        self.__hall_list.append(obj)

class Hall(Star_Cinema): # inheriting Star_Cinema class for passing obj to entry_hall method
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {} # dictionary of seats info
        self.show_list = [] # list for storing tuples
        self.__rows =  rows # row number of seat
        self.__cols = cols # column number of seat
        self._hall_no = hall_no # hall number
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time): # for storing shows
        tpl = (id, movie_name, time)
        self.show_list.append(tpl)
        self.__seats[id] = [] # storing an empty array with dictionary key
        # 2d allocation of seats : we've to allocate a 2d matrix against every movie id
        self.__seats[id] = [[0 for i in range(self.__cols)] for j in range(self.__rows)]

    def book_seats(self, sid, li): # for booking seats
        for tl in self.show_list: # fetching out ID's from show_list
            if sid == tl[0]: # id matches : check for seat availibility
                for t in li: # booking seat by assigning 1
                    self.__seats[sid][t[0]][t[1]] = 1 # booked
                print('................................................')
                print(f'\nSUCCESSFULLY BOOKED YOUR SEATS FOR THE SHOW {sid}')
                print('................................................')
            else: # ignore that case
                continue

    def view_show_list(self):
        print('->->->->->->->->->->->->->->->->___RUNNING SHOWS ON STAR CINEMA HALL___<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-\n')
        print('.......................................................................................................')
        for t in self.show_list:
            print(f' MOVIE NAME : {t[1]}         SHOW ID : {t[0]}       TIME : 16 DECEMBER 2023 AT {t[2]}')
        print('.......................................................................................................')
    
    def view_available_seats(self, id):
        print(f'\nAVAILABLE SEATS FOR SHOW {id} :')
        for j in self.__seats[id]:
            print(j)

hall = Hall(7, 7, 101) # creating hall instance of Hall Class by passing row=7, column=7 & hall_num = 101
hall.entry_show(111, 'MEN IN BLACK             ', '11.00 AM')
hall.entry_show(222, 'ICE AGE                  ', '03.00 PM')
hall.entry_show(333, 'HOW TO TRAIN YOUR DRAGON ', '05.00 PM')
hall.entry_show(444, 'HARRY POTTER & THE PYTHON', '08.00 PM')

li = [] # list for storing row-column as tuple

print('\n***********************************___WELCOME TO STAR CINEMA HALL___***********************************')
while True:
    print()
    print('CHOOSE YOUR PREFERRED QUERY FROM BELOW:')
    print('1. VIEW ALL SHOW TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    print('4. EXIT\n')
    option = int(input('ENTER AN OPTION : '))
    print()

    if option == 1:
        hall.view_show_list()
    elif option == 2:
        i = int(input('ENTER SHOW ID : '))
        flag = False
        for id in hall.show_list:
            if i == id[0]:
                flag = True
                hall.view_available_seats(i)
                break
        if not flag:
            print("INVALID SHOW ID. TRY AGAIN...")
    elif option == 3:
        print(">>>>>>>>>>SEAT BOOKING SYSTEM<<<<<<<<<<\n")
        m = int(input('ENTER SHOW ID : '))
        flag = False
        for id in hall.show_list:
            if m == id[0]:
                flag = True
                print()
                n = int(input('HOW MANY TICKETS DO YOU WANT? : '))
                for i in range(n): # iterating for n number of ticket booking 
                    while True:
                        print(f'\nENTRY FOR TICKET NO. {i+1} :')
                        x = int(input('IN WHICH  ROW  DO YOU WANT YOUR SEAT?  : '))
                        y = int(input('IN WHICH COLUMN DO YOU WANT YOUR SEAT? : '))

                        if x >= 7 or y >= 7: # invalid index
                            print('INVALID SEAT INDEX!!! PROVIDE VALID SEAT INDEX BETWEEN (0-6)')
                        elif (x,y) not in li: # valid index will be stored in list
                            li.append((x,y))
                            break
                        else:
                            print('ALREADY BOOKED!!!')
                            print('PROVIDE ANOTHER SEAT INDEX FROM AVAILABlE SEATS')
                hall.book_seats(m, li)
                break
        if not flag:   
                print("INVALID SHOW ID. TRY AGAIN...")
    elif option == 4:
        break
    else:
        print('PLEASE ENTER A VALID QUERY NUMBER')