# Register your models here.
from django.contrib import admin
from .models import Founder, ShowcaseImage, VideoShowcase, Announcement

# Register your models here.
admin.site.register(Founder)
admin.site.register(ShowcaseImage)
admin.site.register(VideoShowcase)
admin.site.register(Announcement)