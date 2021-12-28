from django.db import models

# Create your models here.


class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString
    def __str__(self):
        return self.message

    # # 메시지 글자숫자 함수로 리턴해주면 admin.py에 display_liks등록된거에 매핑되어 들어간다.
    # def message_length(self):
    #     return len(self.message)
    # # MESSAGELENGTH라나오는데 별명이라고 지어줌.
    # message_length.short_description = "메세지 글자수"
