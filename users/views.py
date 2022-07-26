from django.shortcuts import render, get_object_or_404, redirect
from main.models import Blog
from .models import User

# Create your views here.
def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        'user':user,
        'blogs':Blog.objects.filter(writer=user),
        # 'followings' :
        # 'followers' :
    }

    return render(request, 'users/mypage.html', context)

"""
def follow(request, id):
    user=request.user
    followed_user=get_object_or_404(User, pk=id)
    # 요기에 코드 추가 ★
    return redirect('users:mypage', followed_user.id)
"""