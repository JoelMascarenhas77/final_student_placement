


def getdata(request, dict ):
    store =[]
    for i in dict:
        store.append(request.POST[i])
    return store

        
joel =[]

class student():
        first_name =0
        last_name =0
