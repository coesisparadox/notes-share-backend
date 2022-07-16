from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render
from .models import Posts, Review
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.
@xframe_options_sameorigin
def feed_view(request):
    if (request.method=="POST"):
        print('status1',request.POST.get('review_status'))
        if(request.POST.get('review_status')=='a'):
            caption=request.POST.get("caption")
            faculty=request.POST.get("faculty")
            sem=request.POST.get("sem")
            sub=request.POST.get("sub")
            image=request.FILES.get("file")
            user=request.user
            user=Posts(user=user,caption=caption,file=image,faculty =faculty,sem=sem,sub=sub)
            user.save()
            messages.success(request,"Successfully Posted")
    if('q' in request.GET):
        query=request.GET.get('q')
        allPosts=Posts.objects.filter(caption__icontains=query)
        print(allPosts)
    else: 
        allPosts=Posts.objects.all()      
  
    
    data={'posts':allPosts}
    print(data)
    
    return render(request,'users/feed.html',data)



def review_view(request):
    # pass
    if request.method=="POST":
        print('status2',request.POST.get('review_status'))

        if(request.POST.get('review_status')!='a'):
            print('asdasdadas')
            prod_id=request.POST.get('review_status')
            prod=prod_id.split("/")
            print('prod',prod[0])
            post=Posts.objects.get(id=prod[0])
            comment=request.POST.get('review')
            rate=request.POST.get('rate')
            user=request.user
            print("hello",post,comment,rate,user)
            Review(user=user,post=post,comment=comment,rate=rate).save()
            # return HttpResponse("Success")

            return redirect('feed-page')
        # return render(request,'users/feed.html')
        else:
           return HttpResponse("Invalid")

def home_view(request):
    return render(request,'users/index.html')

def about_view(request):
    return render(request,'users/about.html')