from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False,verbose_name="姓名")
    location = models.CharField(max_length=255,verbose_name="居住地")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "會員"
        verbose_name_plural = "會員"

class Detail(models.Model):
    line_name = "line_id"+" 名稱" 
    name = models.ForeignKey(Customer,related_name='customer',on_delete=models.CASCADE,verbose_name="姓名") 
    line_id = models.CharField(max_length=255,verbose_name = line_name,blank=True)
    email  = models.EmailField(max_length=255,verbose_name="電子郵件",blank=True)
    tel = models.CharField(max_length=10,verbose_name="電話號碼")
    create_time = models.DateTimeField(auto_now = True,verbose_name="日期")
    
    suggest = models.TextField(max_length=500,verbose_name="建議",blank=True)
     
    class Meta:
        verbose_name = "客戶意見與聯絡方式"
        verbose_name_plural = "客戶意見與聯絡方式"


