from django.shortcuts import render
from editing.models import *
import docx
from docx import Document


# Create your views here.
def index(request):
    
    return render(request,'index.html')

def download(request):
    context = {'file':FilesAdmin.objects.all()}
    return render(request,'download.html',context)

def editing(request):
    if request.method =='POST':
        com_name = request.POST['com_name']
        short_name = request.POST['short_name']
        scope = request.POST['scope']
        date = request.POST['date']
        img = request.POST.get('img', 'default value')
        print(img)
        #print(img)
# calling function by passing .docx as argument
        #print (readtxt(r'C:\Users\Programmer\operation\document\media_cdn\media\SOC_8NK5iCG.docx'))
                
    else:
        return render(request,'download.html')

    return render(request,'download.html')
    
    
def readtxt(docx_file):
    
    # opening the docx
    document = Document(r'C:\Users\Programmer\operation\document\media_cdn\media\SOC_8NK5iCG.docx')
    print(document)

    # counter var for conditioning
    counter = 0
    fullText = []
    for para in document.paragraphs:
        print(para.text)
        # replacing the first line
        if counter == 3:
            para.text = 'This is the best company'
        else:
            pass
        fullText.append(para.text)
        counter += 1
        # changes saving
        document.save(r'C:\Users\Programmer\operation\document\media_cdn\media\SOC_8NK5iCG.docx')

    return '\n'.join(fullText)


