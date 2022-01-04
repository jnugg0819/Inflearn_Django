from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', "")
    if q:
        qs = qs.filter(message__icontains=q)

    # render첫번재 인자 request, 두번째인자 앱이름/원하는 템플릿 이름
    # 템플릿 만들어지는 경로 instagram/templates/instagram/post_list.html
    # 밑에있는 q는 value에다가 넣게되면 해당값이 뷰에 들어가게됨.(장고 템플릿 에서 {{}}를쓰면 문자열에대한 값을 넣을수있음).
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q
    })
