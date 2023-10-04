


def getdata(request, dict ):
    store =[]
    for i in dict:
        store.append(request.POST[i])
    return store

        
