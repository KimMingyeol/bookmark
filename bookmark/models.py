from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        #객체 출력 시 return 값(문자열)을 나타냄
        return "이름 : "+self.site_name+", 주소 : " + self.url
    def get_absolute_url(self):
        #수정이 완료된 후 이동할 페이지를 선언하는 것, 이동할 url을 반환한다.
        return reverse('detail', args=[str(self.id)])