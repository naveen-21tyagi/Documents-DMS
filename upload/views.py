from django.shortcuts import render, redirect
from .forms import DocumentsForm
# Create your views here.
def uploadFileView(request):
    if request.method =="POST":
        # request.Files must be passed here
        form = DocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # this save the record in DB and copies the file to MEDIA_ROOT
            return redirect("upload_success")
    else:
        form = DocumentsForm

    return render(request, "./upload.html", {"form":form})

def uploadSuccessView(request):
    return render(request,"./success.html")