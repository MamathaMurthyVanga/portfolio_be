from django.db import models

class Portfolio(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True,default=True)
    title = models.CharField(db_column='title', max_length=200)
    description = models.TextField(db_column='description')
    linkedinlink = models.URLField(db_column='linkedinlink',blank=True, null=True)
    github = models.CharField(db_column='github',max_length=100,blank=True, null=True)
    email = models.EmailField(db_column='email',blank=True, null=True)
    technologies = models.CharField(db_column='technologies',max_length=500)
    image = models.ImageField(db_column='image',upload_to='project_images/', blank=True, null=True)


    class Meta:
        db_table = 'details'

    # def __str__(self):
    #     return self.title

# Create your models here.
