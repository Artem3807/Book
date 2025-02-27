from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()

    def str(self):
        return self.title

    class Meta:
        db_table = "books"
        verbose_name = "book"