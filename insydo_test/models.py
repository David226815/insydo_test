"""
Models file for insydo_test project
"""
# from django.contrib.auth.models import User
from django.db import models


class QuestionBanks(models.Model):
    """
    Table to store question banks
    """
    # q_id = models.AutoField(primary_key=True, db_column='q_id')
    # q_qs = models.TextField(db_column='q_qs', default='')
    # q_name = models.CharField(db_column='q_name', default='', max_length=50)
    # q_paid = models.BooleanField(db_column='q_paid', default=True)
    # q_price = models.PositiveIntegerField(db_column='q_price', default=0)
    # q_language = models.PositiveSmallIntegerField(db_column='q_language', choices=LANGUAGE, default=LANGUAGE_ENGLISH)
    # q_sect = models.PositiveSmallIntegerField(db_column='q_sect', choices=TEST_SECTION, default=TEST_SECTION_NONE)
    # q_course = models.PositiveSmallIntegerField(db_column='q_course', choices=EXAMINATION_TYPE, default=EXAMINATION_TYPE_NONE)

    def __unicode__(self):
        return self.q_name