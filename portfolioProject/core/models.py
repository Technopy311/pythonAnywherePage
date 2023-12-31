from django.db import models

class Photo(models.Model):
    title = models.CharField("Title", max_length=20, null=False, default="")
    description = models.TextField("Description", max_length=100, null=False, default="")
    capture_date = models.DateField("Capture date", null=False)
    photo = models.ImageField("Photo", null=True, default=None)


class Project(models.Model):
    title = models.CharField("Title", max_length=20, null=False, default="")
    excerpt = models.CharField("Excerpt", max_length=40, null=False, default="")
    description = models.TextField("Description", max_length=600, null=False, default="")
    main_photo = models.ImageField("Main picture", null=False, default=None)
    
    photo_2 = models.ImageField("Photo 2", null=True, default=None)
    photo_3 = models.ImageField("Photo 3", null=True, default=None)
    
    start_date = models.DateField("Started date", null=False)
    end_date = models.DateField("End date", null=True, default=None)
    project_link = models.CharField("Project Link", max_length=65,  null=True, default=None)

