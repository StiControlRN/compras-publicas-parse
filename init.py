from datetime import date, datetime
import fileinput
import os
import csv
import sys

def getfiles ():
    path = os.path.join(os.getcwd(),'planilhas')
    planilhas = [file for file in os.listdir(path)]
    return planilhas

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def parse(filename,writer):
    formatados = 0
    try:
        replaceAll('planilhas/'+filename,'"',"") #replaces all " for nothing
    except Exception as e:
        print('Ocorreu um erro ao eliminar as " da planilha', e)
    try:
        with open('planilhas/'+filename, newline='') as csvfile:
            planilha = csv.reader(csvfile, delimiter='|')
            for index, row in enumerate(planilha):
                if(index > 0):
                    new_row = [row[0],datetime.strptime(row[1], "%d/%m/%Y  %H:%M:%S").date(),row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11].replace(';',"").replace(',',".")]
                    writer.writerow(new_row)
                formatados = index
        print('Linhas formatadas: '+str(formatados))
    except Exception as e:
        print("Deu ruim: ",e)
    

if __name__ == '__main__':
    hoje = date.today().strftime("%d-%m-%Y")
    planilhas = getfiles()
    path = os.path.join(os.getcwd(), 'resultado/')
    if os.path.exists(path):
        if os.path.isdir(path):
            if os.path.isfile(os.path.join(path,'resultado-'+hoje+'.csv')):
                path = os.path.join(path,'resultado-'+hoje+'.csv')
                print("Apagando execuçao anterior")
                os.remove(path)
        else:
            os.mkdir(path)
    else:
            os.mkdir(path)
    f = open('resultado/resultado-'+hoje+'.csv', 'w', encoding='UTF8')
    writer = csv.writer(f,delimiter =";", lineterminator = '\n')
    header = ['numnfe','dtemissao','chavenfe','cnpjemitente','razaosocialemitente','municipioorigem','uforigem','cnpjdestinatario','razaosocialdestinatario','municipiodestino','ufdestino','vlroperacao']
    writer.writerow(header)
    print(planilhas)
    for num,planilha in enumerate(planilhas):
        print("Planilha: "+str(num+1)+" de " + str(len(planilhas)))
        parse(planilha,writer)
    f.close()
    print("Concluido")