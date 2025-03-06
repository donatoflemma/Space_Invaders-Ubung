import json

#data = {
#    'scarpe':'bianche' , 'camicia':'nera',
#    'mocassini':'bianchi','sciarpa':'blu',
#    'bottiglia':'gialla','maglia':'celeste'
#}

#with open('Muster_data.txt','w') as test:  # 'w' serve per dire che se non esiste lo deve creare 
#    json.dump(data,test)   # per scrivere il file 

with open('Muster_data.txt') as test_file:
    data= json.load(test_file)
    for chiave,valore in data.items():
        print(f"{chiave}:{valore}")
        