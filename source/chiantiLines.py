import PyPDF2,os,pickle
from chianti import chiantiIons

chiantiPDFs = sorted([x for x in os.listdir("chianti")],key=lambda x: x.find("_"))
ionList = []
wvlList = []

for pdf in chiantiPDFs:
    f = open("chianti/"+pdf,"rb") #open as read binary
    reader = PyPDF2.PdfFileReader(f)
    nP = reader.numPages

    for i in range(1,nP):
        page = reader.getPage(i)
        lines = [x for x in page.extractText().split() if len(x) >= 7 and "." in x and x[0].isalpha()]
        for line in lines:
            for j,char in enumerate(line):
                if char.isdigit():
                    ionList.append(line[:j])
                    idx = line.find(".")
                    wvlList.append(line[j:idx+5])
                    break

ch = chiantiIons(ionList,wvlList)
with open("chianti_db.pkl","wb") as output:
    pickle.dump(ch,output,pickle.HIGHEST_PROTOCOL)