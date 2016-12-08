# django
from django.db import models
from django.conf import settings

# python
from datetime import date

# pip

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class UserInfo(TimeStampModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    paid_until = models.DateField(default=date.today)

    @property
    def is_paid(self):
        if date.today() < self.paid_until:
            return True
        return False

    def __str__(self):
        if self.is_paid:
            paid = '학생회비: O'
        else:
            paid = '학생회비: X'
        return str(self.user.username) + '/' + paid


class Petition(TimeStampModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    valid_until = models.DateField(default=date.today)

    def __str__(self):
        return self.title


class PetitionProgress(TimeStampModel):
    petition = models.ForeignKey(Petition)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.petition.__str__()+ ': #{} '.format(self.pk) + self.title


class PetitionComment(TimeStampModel):
    petition = models.ForeignKey(Petition)
    comment = models.TextField()

    def __str__(self):
        if len(self.comment) < 20:
            return self.petition.__str__() + '의 #{}번 덧글: '.format(self.pk) + self.comment
        else:
            return self.petition.__str__() + '의 #{}번 덧글: '.format(self.pk) + self.comment[:20]


class Vote(TimeStampModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class VoteChoice(TimeStampModel):
    vote = models.ForeignKey(Vote)
    choice = models.CharField(max_length=200)

    def __str__(self):
        return self.vote.__str__() + ':' + self.choice


class VoteComment(TimeStampModel):
    vote = models.ForeignKey(Vote)
    comment = models.TextField()

    def __str__(self):
        if len(self.comment) < 20:
            return self.vote.__str__() + '의 #{}번 덧글: '.format(self.pk) + self.comment
        else:
            return self.vote.__str__() + '의 #{}번 덧글: '.format(self.pk) + self.comment[:20]
