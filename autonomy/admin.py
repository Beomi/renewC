from django.contrib import admin

from .models import UserInfo
from .models import Petition
from .models import PetitionProgress
from .models import PetitionComment
from .models import Vote
from .models import VoteChoice
from .models import VoteComment

admin.site.register(UserInfo)
admin.site.register(Petition)
admin.site.register(PetitionProgress)
admin.site.register(PetitionComment)
admin.site.register(Vote)
admin.site.register(VoteChoice)
admin.site.register(VoteComment)