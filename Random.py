from builtins import dict

def update_dict (dictionary , li):
        for i in li :
            if(dictionary.get(i)==None):
                dictionary.__setitem__(i,1);
            else:
                dictionary.__setitem__(i,dictionary.get(i)+1)
        return dictionary

def cancel_out(dict1 , dict2):
    for i in dict1 :
        if(dict2.get(i)!=None):
            a = dict1.get(i)
            b = dict2.get(i)
            diff = abs(a-b)
            if(a>b):
                b = 0
                dict1.__setitem__(i , diff)
                dict2.__setitem__( i , b)
            else :
                a = 0
                dict2.__setitem__(i , diff)
                dict1.__setitem__( i , a)
    return dict1 , dict2
def sumof ( dictionary ):
    summation = 0
    for i in dictionary :
        summation += dictionary.get(i);
    return summation
def tostring( l ):
    string = ""
    for i in l :
        string += i
    return string
def flames_lol ( a , b):
    Name_1 = list(a);
    Name_2 = list(b);
    Name1_dict = dict();
    Name2_dict = dict();
    Name1_dict = update_dict(Name1_dict,Name_1)
    Name2_dict = update_dict(Name2_dict,Name_2)
    Name1_dict , Name2_dict = cancel_out(Name1_dict,Name2_dict)
    summation = sumof(Name2_dict) + sumof(Name1_dict)
    flames = "FLAMES"
    flames_list = list(flames)
    lenght = len(flames_list)
    while lenght>1:
        if(lenght < summation):
            cancel_this = summation - (int(summation/lenght)*lenght)-1
            flames_list.__delitem__(cancel_this)
            if(cancel_this==-1):
                lenght = len(flames_list)
                continue
            newstring = tostring(flames_list)
            newstring = newstring[cancel_this+1:]+ newstring[:cancel_this+1]
            flames_list = list(newstring)
        else :
            cancel_this = lenght - summation -1
            flames_list.__delitem__(cancel_this -1)
            if(cancel_this==-1):
                lenght = len(flames_list)
                continue
            newstring = tostring(flames_list)
            newstring = newstring[cancel_this:]+ newstring[:cancel_this]
            flames_list = list(newstring)
        lenght = len(flames_list)
    print (flames_list)
    return

flames_lol("purnachandra rao" , "")