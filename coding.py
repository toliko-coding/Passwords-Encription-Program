from functools import reduce

def inc_dec_char(char,num):

    if num < 0:
        if char == '9':
            return 'a'
        if char == 'z':
            return 'A'
        if char == 'Z':
            return '1'
        else:
            temp = bytes(char, 'utf-8')
            temp = temp[0] + 1
            return chr(temp)

    else:
        if char == 'a':
            return '9'
        if char == 'A':
            return 'z'
        if char == '1':
            return 'Z'
        else:
            temp = bytes(char, 'utf-8')
            temp = temp[0] - 1
            return chr(temp)


temp = {'a' : 'a','b' : 'b','c' : 'c','d' : 'd','e' : 'e','f' : 'f','g' : 'g','h' : 'h','i' : 'i','j': 'j','k': 'k','l': 'l','m': 'm','n': 'n', 'o': 'o','p': 'p','q': 'q','r': 'r','s': 's','t': 't','u': 'u','v': 'v','w': 'w','x': 'x','y': 'y','z': 'z',
                    'A' : 'A','B' : 'B','C' : 'C','D' : 'D','E' : 'E','F' : 'F','G' : 'G','H' : 'H','I' : 'I','J' : 'J','K' : 'K','L' : 'L','M' : 'M','N' : 'N','O' : 'O','P' : 'P','Q' : 'Q','R' : 'R','S' : 'S','T' : 'T','U' : 'U','V' : 'V','W' : 'W','X' : 'X','Y' : 'Y','Z' : 'Z',
                    '0' : '0','1' : '2','2' : '2','3' : '3','4' : '4','5' : '5','6' : '6','7' : '7','8' : '8','9' : '9',}


"function that increace or decreace the char num times"
def change_char(char,num):
    c = char
    if num < 0 :
        num = num * -1
        for _ in range(num):
            c = inc_dec_char(c , num)

    else:
        for _ in range(num):
            c = inc_dec_char(c , num)

    return c


"dispatch function with message passing to make encoding or decoding according to given keys "
def coding():
    theDic = {'reverse_word' : False, 'reverse_string' : False}
    theKey = theDic


    def dis(msg,args=None):

        '''message passing key to export the current encoding key'''
        if msg == 'export_key':
            nonlocal theKey
            if len(theKey) == 2:
                return "empty key"

            return theKey

        '''message passing key to set the given encoding key'''
        if msg == 'set_key':
            f1 = False
            f2 = False
            if args[1] == 'yes':
                f1 = True
            if args[2] == 'yes':
                f2 = True

            theKey = theDic
            theKey['reverse_word'] = f1
            theKey['reverse_string'] = f2




            temp = {'a' : 'a','b' : 'b','c' : 'c','d' : 'd','e' : 'e','f' : 'f','g' : 'g','h' : 'h','i' : 'i','j': 'j','k': 'k','l': 'l','m': 'm','n': 'n', 'o': 'o','p': 'p','q': 'q','r': 'r','s': 's','t': 't','u': 'u','v': 'v','w': 'w','x': 'x','y': 'y','z': 'z',
                    'A' : 'A','B' : 'B','C' : 'C','D' : 'D','E' : 'E','F' : 'F','G' : 'G','H' : 'H','I' : 'I','J' : 'J','K' : 'K','L' : 'L','M' : 'M','N' : 'N','O' : 'O','P' : 'P','Q' : 'Q','R' : 'R','S' : 'S','T' : 'T','U' : 'U','V' : 'V','W' : 'W','X' : 'X','Y' : 'Y','Z' : 'Z',
                    '0' : '0','1' : '1','2' : '2','3' : '3','4' : '4','5' : '5','6' : '6','7' : '7','8' : '8','9' : '9',}

            temp = dict(map(lambda x : (x[0] , change_char(x[1],args[0]) ), temp.items()))
            print(temp)
            theKey.update(temp)
            print('DONE - set of new key')




        '''message passing key to make the key empty'''
        if msg == 'empty_key' :
            theKey = 'empty key'
            print("Done - the key now is empty")


        '''message passing key to update the current key to new key that given as arrgument'''
        if msg == 'import_key':
            if type(args) == type(theKey):
                theKey = args
                print('DONE - new key is imported and updated')
            else:
                print("Error : The key must be a Dict type value ")


        '''message passing key to encode the value that given according to the key'''
        if msg == 'encoding':
            if len(theKey) == 2 :
                return "The key is empty , please set key"

            print("Encoding the Message ..")
            temp =[]
            temp2=[]
            for char in args:
                temp.append(char)

            for char in temp:
                temp2.append(theKey[char])

            newstr =  reduce(lambda x,y:x+y , temp2)

            if theKey["reverse_word"] == True:
                # rtemp = newstr.split()
                # rtemp.reverse()
                # newstr = reduce(lambda x,y : x + ' ' + y , rtemp)
                pass


            if theKey["reverse_string"] == True:
                # rtemp = newstr.split()
                # rt = []
                # for word in rtemp:
                #     rt.append(word[::-1])
                #
                # newstr = reduce(lambda x, y: x + ' ' + y, rt)
                pass

            return newstr


        '''message passing key to decode the arrgument that given according to current key'''
        if msg == 'decoding':

            print("decoding...")
            oldstr = args
            if len(theKey) == 2:
                return 'key empty'

            # if theKey["reverse_string"] == True:
            #     rtemp = oldstr.split()
            #     rt = []
            #     for word in rtemp:
            #         rt.append(word[::-1])
            #     oldstr = reduce(lambda x, y: x + ' ' + y, rt)
            #
            # if theKey['reverse_word'] == True:
            #     rtemp = oldstr.split()
            #     rtemp.reverse()
            #
            #     oldstr = reduce(lambda x, y: x + ' ' + y, rtemp)
            #     #print('After reverse words')
            #     #print(oldstr)

            reverseDict = {value:key for key ,value in theKey.items()}
            listo = []
            listo2 = []
            for char in oldstr:
                listo.append(char)
            for char in listo:
                listo2.append(reverseDict[char])

            oldstr = reduce(lambda x,y : x + y , listo2)
            return oldstr

    return dis