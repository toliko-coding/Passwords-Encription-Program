from tkinter import *
import os
from functools import reduce

sys.path.append(".")
from myClasses import CreateDisplay
from coding import *


'''functios :'''
def clik(Name,password,window):
    '''add task function'''

    try:
        if ' ' in Name.get():
            raise ValueError("space cannot be in the User Name")
        if ' ' in password.get():
            raise ValueError("space canoot be in the password")

    except ValueError as e:
        errorLabel = Label(window, text=e)
        errorLabel.grid(row = 7)



    else:

        try:

            keyfile = open("key.txt",'r')
        except FileNotFoundError as e:
            print(e)
            errorLabel = Label(window, text="Please set key before this option")
            errorLabel.grid(row=7)
        else:
            strkey=keyfile.read()
            keyfile.close()

            dictkey = eval(strkey)

            code = coding()
            code('import_key' , dictkey)
            hpass = code('encoding' ,password.get())


            file = open("mypasswords.txt" , 'a')
            file.write(Name.get() + ' ' + hpass + ' \n ') #+ '\n'
            file.close()

            finish = Label(window,text="added to the list")
            finish.grid(row=7)


'''function that show me my list'''
def showList():
    try:
        sfile = open("mypasswords.txt" , 'r')

    except FileNotFoundError as e:
        print(e)
        errorLabel = Label(Main,text="There is not list yet")
        errorLabel.grid(row=9)

    else:
        myDict = {}

        def goMain():
            newW.destroy()


        newW = Tk()
        newW.title("list")
        newW.geometry("400x200")

        str = sfile.read()
        print("str : ",str)


        temp = str.split(" ")
        print("temp :" , temp)


        #function that eval str type to dict type
        def strToDoict():


            count = len(temp)
            if count == 0:
                print("in count",count)
            else:
                print("good count :",count)

                tempz = list(filter(lambda x:x != '\n' , temp))

                i=0

                try:
                    while(i < count):
                        myDict[tempz[i]] = tempz[i+1]

                        i+=2

                except IndexError as e:
                        print(e)
            # print("myDict:" , myDict)


        strToDoict()
        # print(myDict)


        myLabel = Label(newW,text=str , width = 30)
        myLabel.pack()

        back = Button(newW , text = "go Back" , command = goMain)
        back.pack()

        newW.mainloop()
        sfile.close()






def DeleteList(window):
    'function that delete the current list if exicst'
    try:
        sfile = open("mypasswords.txt", 'r')

    except FileNotFoundError as e:
        print(e)
        errorLabel = Label(window, text="There is not list yet")
        errorLabel.grid(row=0)

    else:
        sfile = open("mypasswords.txt", 'w')
        sfile.write("")
        errorLabel = Label(window, text="List deleted")
        errorLabel.pack()
        sfile.close()




def add_Button():
    'function that open new Window gets UserName and password and password (encripted)'
    addW = Tk()
    addW.title("Add Password")
    addW.geometry("200x220")

    eList = []

    l1=Label(addW,text="Enter User Name")
    l1.grid(row = 0 , column =0)
    userName = Entry(addW,width = 35)
    userName.grid(row = 1 , column =0)
    eList.append(userName)

    l2 = Label(addW, text="Enter Password")
    l2.grid(row=2, column=0)
    passWord = Entry(addW, width=35)
    passWord.grid(row=3, column=0)
    eList.append(passWord)


    def run():
        clik(userName,passWord,addW)

    submit = Button(addW,text="Submit" ,command = run)
    submit.grid(row = 4 , column =0)



    def goClean():
        for entry in eList:
            entry.delete(0,END)

    clear= Button(addW,text="clear" , command = goClean)
    clear.grid(row = 5)

    def exit():
        addW.destroy()

    exit = Button(addW,text = "exit" ,command = exit)
    exit.grid(row=8)

    addW.mainloop()




def get_Button():
    'get Button function'

    getW = Tk()
    getW.title("Get Password")
    getW.geometry("300x150")

    try:
        sfile = open("mypasswords.txt" , 'r')

    except FileNotFoundError as e:
        print(e)
        getW.geometry("100x50")
        errorLabel = Label(getW,text="There is not list yet")
        errorLabel.grid(row=0)

        exitB = Button(getW,text="back" , command = getW.destroy)
        exitB.grid(row = 1)

    else:

        try:
            keyfile = open("key.txt" , 'r')

        except FileNotFoundError as e:
            errorLabel = Label(getW, text="There is no key yet")
            errorLabel.grid(row=0)

        else:

            lb1 = Label(getW , text = "Please Enter the User Name" ,font = ('calibre' , 15 , 'bold'))
            lb1.grid(row = 0)

            entry = Entry(getW , width = 35)
            entry.grid(row=1)

            def getPass():
                sfile = open("mypasswords.txt", 'r')
                str = sfile.read()
                # print("str : ", str)

                myDict = {}

                temp = str.split(" ")
                # print("temp :", temp)

                count = len(temp)
                if count == 0:
                    print("in count", count)
                else:
                    # print("good count :", count)

                    tempz = list(filter(lambda x: x != '\n', temp))

                    try:
                        if entry.get() not in tempz:
                            raise ValueError("eroor")

                    except ValueError as e:
                        print(e)
                        errorLabel = Label(getW, text="There is no user name as :" + entry.get())
                        errorLabel.grid(row=3)

                    else:

                        i = 0

                        try:
                            while (i < count):
                                myDict[tempz[i]] = tempz[i + 1]

                                i += 2

                        except IndexError as e:
                            print(e)

                        keystr = keyfile.read()
                        keydict = eval(keystr)

                        code = coding()
                        code('import_key' , keydict)

                        realpass = code('decoding' , myDict[entry.get()])

                        showPass = Label(getW, text=realpass)
                        showPass.grid(row=6)


            getB = Button(getW,text = "Get Password" , command = getPass)
            getB.grid(row=2)


            def clear():
                entry.delete(0,END)
                getW.destroy()
                get_Button()

            clearB = Button(getW,text = "Clear" , command = clear)
            clearB.grid(row=4)



            getW.mainloop()


def setKey():
    'function that run whem setKey Button active , set the key'
    window = Tk()
    window.title("Set Key")
    window.geometry("400x200")

    rotationLaberl = Label(window,text="Enter Rotation Number - 0 for no encoding" , font=('calibre',10,'bold'))
    rotationLaberl.grid(row=0)

    rotationEntry = Entry(window , width = 35)
    rotationEntry.grid(row=1)

    def submit():
        code = coding()

        code('set_key' , (int(rotationEntry.get()) , 'yes' ,'yes'))
        key = code("export_key")

        try:
            keyfile = open("key.txt", 'a')

        except FileNotFoundError as e:
            print(e)
            showLabel = Label(window, text="File EROOR : " )
            showLabel.grid(row=5)
        else:

            keyfile.write(str(key))
            keyfile.close()

            showLabel = Label(window,text = "Key is Updated , Rotation : " +rotationEntry.get())
            showLabel.grid(row = 5)




    submit = Button(window, text="Submit", command=submit)
    submit.grid(row=3)

    exitB = Button(window, text="Exit", command=window.destroy)
    exitB.grid(row=4)

    window.mainloop()





'''DRIVER'''

def init():

    login = Tk()
    login.title("Log In to the Program")
    login.geometry("200x100")
    form = Label(login,text="Enter Password ",font=('calibre',15,'bold') )
    form.grid(row=0)

    epass = Entry(login,width = 35)
    epass.grid(row=1)

    def check():
        if epass.get() == "12345":
            login.destroy()

            Main = Tk()
            Main.title("MENU")
            Main.geometry("400x400")
            title = Label(Main, text="Please Choose what you want to do:", font=('calibre', 15, 'bold'))
            title.grid(row=0)

            addButton = Button(Main, text="Add Password", height=3, width=30, command=add_Button)
            addButton.grid(row=2, column=0)

            getListButton = Button(Main, text="Get Password", height=3, width=30, command=get_Button)
            getListButton.grid(row=3, column=0)

            lookButton = Button(Main, text="See list", height=3, width=30, command=showList)
            lookButton.grid(row=4, column=0)

            setKeyButton = Button(Main, text="Set Key", height=3, width=30, command=setKey)
            setKeyButton.grid(row=5)

            exitButton = Button(Main, text="Exit", height=3, width=30, command=Main.destroy)
            exitButton.grid(row=6)

            Main.mainloop()

        else:
            login.destroy()
            init()


    passLogin = Button(login,text = "Log-In" , command = check)
    passLogin.grid(row=2)

    login.mainloop()


init()


# Main = Tk()
# Main.title("MENU")
# Main.geometry("400x400")
# title = Label(Main , text="Please Choose what you want to do:" , font=('calibre',15,'bold'))
# title.grid(row=0)
#
#
# addButton = Button(Main,text="Add Password" ,  height = 3 , width = 30 , command = add_Button)
# addButton.grid(row=2,column=0)
#
# getListButton = Button(Main,text="Get Password" , height = 3 , width = 30  , command = get_Button)
# getListButton.grid(row=3,column=0)
#
# lookButton = Button(Main,text="See list" ,  height = 3 , width = 30 ,command = showList)
# lookButton.grid(row=4,column=0)
#
# setKeyButton = Button(Main , text = "Set Key" ,height = 3 , width = 30 ,command = setKey )
# setKeyButton.grid(row=5)
#
# exitButton = Button(Main,text= "Exit" ,  height = 3 , width = 30 ,command = Main.destroy)
# exitButton.grid(row=6)
#
#
#
# Main.mainloop()





# root = Tk()
#
# root.geometry('250x200+250+200')
# Label(root, text="Position 1 : x=0, y=0", bg="#FFFF00", fg="white").place(x=5, y=0)
# Label(root, text="Position 2 : x=50, y=40", bg="#3300CC", fg="white").place(x=50, y=40)
# Label(root, text="Position 3 : x=75, y=80", bg="#FF0099", fg="white").place(x=75, y=80)
#
# root.mainloop()

# #
# ''''''
# '''open window'''
# window = Tk()
# window.title("Tolis Program")
# window.geometry("400x600")
#
# entryList = []
#
# '''create Enter name label'''
# UserNameLabel = Label(window,text="User Name :" , font=('calibre',10,'bold') ,height = 1, width = 30)
# UserNameLabel.pack()
# Name = Entry(window ,width = 30)
# Name.pack()
# entryList.append(Name)
#
#
# '''create Enter password label'''
# passwordLabel = Label(window,text="Password" , font=('calibre',10,'bold') ,height = 1, width = 30)
# passwordLabel.pack()
# password = Entry(window,width = 30)
# password.pack()
# entryList.append(password)
#
#
#
# mybutton = Button(window , text="Save" ,command=clik , height = 1 , pady = 1)
# mybutton.pack()
#
# showB = Button(window , text="Show List" ,command=showList)
# showB.pack()
#
# clearB = Button(window,text="Clear" , command = clear)
# clearB.pack()
#
# deleteList = Button(window,text="Delete List" , command = DeleteList)
# deleteList.pack()
#
# # newWB = Button(window,text="New Window" , command = newWindow)
# # newWB.pack()
#
# exitB = Button(window ,text = "Exit" ,pady = 10, command = (lambda x : x.destroy)(window))
# exitB.pack()
#
# window.mainloop()



