import os 
import pickle
from termcolor import colored

def sprint(text):
    text = 'System Message === '+text
    print(text)

if(not os.path.exists('starterData')):
    sprint('Data file not found ! Auto create the data file "starterData" in current path !')
    open('starterData','wb')
    sprint('Data file finished !')
file = open('starterData','r+b')
store={}
while 1:
        try:
            sprint('loading data')
            store = pickle.load(file)
        except (EOFError):
            break
sprint('Finish loading')



def addPath(name, path):
#    file = open('starterData','rb')
    path = str(path.replace(os.sep,"/"))
    print('add name="', name,'" , path="',path,'"' )
    store[name] = path
    pickle.dump(store,open('starterData','wb'))

def openFile(name):
    print('Ready to open ',name)
    try:
        os.startfile(store[name])
    except Exception as e:
        sprint('Application not found !'+e)

def showPath(query):
  
    if(query=='all'):
        print(store)
      
    elif(query in store):
        print('name:',query,'path:',store[query])
    else:
        sprint('name not found !')
    
    
def clearPath(query):
    if(query=='all'):
        pickle.dump({},open('starterData','wb'))
        sprint('All data has clear ! Please restart the programe !')
    else:
        store.pop(query,None)
        pickle.dump(store,open('starterData','wb'))
        sprint(query+' data has clear ! ')

def callHelp():
    print('"add" name path')
    print('"open" name')
    print('"show" name/"all"')
    print('"clear" name/"all"')
    print('"help"')

def handle_input():
    query = input('Input query >>>')
    query = query.split(" ",2)
   
    if(str(query[0])=='add' and len(query) >= 3):
        addPath(query[1],str(query[2]))
    elif(query[0]=='open' and len(query) >= 2):
        openFile(query[1])
    elif(query[0]=='show' and len(query) >= 2):
        showPath(query[1])
    elif(query[0]=='clear' and len(query) >= 2):
        clearPath(query[1])
    elif(query[0]=='help'):
        callHelp()
    else:
        sprint('Invalid query ! Input "help" to see all query')
        
while 1:
        try:
            handle_input()
        except (EOFError):
            print(EOFError)
            break





