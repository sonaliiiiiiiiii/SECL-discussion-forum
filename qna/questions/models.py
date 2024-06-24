from django.db import models

class users(models.Model):
    sname = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    upass = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class post_q(models.Model):
    pquestion = models.CharField(max_length=1000)
    puser = models.CharField(max_length=100)

    def __str__(self):
        return self.pquestion

class qna_db(models.Model):
    qid = models.CharField(max_length=100)
    answr = models.CharField(max_length=1000)
    auser = models.CharField(max_length=100)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.answr

class Vote(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    answer = models.ForeignKey(qna_db, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10)  # 'upvote' or 'downvote'

    class Meta:
        unique_together = ('user', 'answer')