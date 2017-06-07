from django.db import models


class BirthPerson(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def babe_boomer_status(self):
        """BirthPerson의 베이비부머 상태를 알려준다"""
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre Boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby Boomer"
        else:
            return "Post Boomer"

    @property
    def full_name(self):
        """BirthPerson객체의 이름 전체를 반환한다"""
        return '%s %s' % (self.first_name, self.last_name)