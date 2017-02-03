from django.contrib import admin

from .models import UserInfo
from .models import Petition
from .models import PetitionProgress
from .models import PetitionComment
from .models import Vote
from .models import VoteChoice
from .models import VoteComment
from .models import PetitionFile
from .models import PetitionImage

admin.site.register(UserInfo)
admin.site.register(PetitionProgress)
admin.site.register(PetitionComment)
admin.site.register(Vote)
admin.site.register(VoteChoice)
admin.site.register(VoteComment)


class PetitionFileInline(admin.TabularInline):
    model = PetitionFile
    extra = 1

class PetitionImageInline(admin.TabularInline):
    model = PetitionImage
    extra = 1


@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    inlines = [PetitionFileInline, PetitionImageInline, ]
    list_display = ['id', 'title', 'valid_until',]
    list_display_links = ['title', ]
    search_fields = ['title', ]
    list_editable = ['valid_until', ]