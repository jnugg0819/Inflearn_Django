from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d')
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString
    def __str__(self):
        return self.message

    # Default 정렬 추가  id순 정렬.
    class Meta:
        ordering = ['-id']

    # # 메시지 글자숫자 함수로 리턴해주면 admin.py에 display_liks등록된거에 매핑되어 들어간다.
    # def message_length(self):
    #     return len(self.message)
    # # MESSAGELENGTH라나오는데 별명이라고 지어줌.
    # message_length.short_description = "메세지 글자수"


class Comment(models.Model):
    # 외래키는 Post테이블과 관련있는다.
    # Cascade는 FK로 참조하는 다른모델의 Record도 삭제
    # 여기서 Post라고 써도되고 'Post'라고 문자열처럼 써도되고 , 앞에 앱이름을 써도된다.('instagram/Post')
    # 이때는 다른앱의 모델을 쓰고싶을떄 쓴다.
    # post_id 라는 필드가 생성됩니다.
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, limit_choices_to={'is_public': True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
