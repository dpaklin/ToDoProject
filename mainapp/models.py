from django.db import models

from django.conf import settings


class CreatedAtModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name="создан",
        auto_now_add=True
    )

    class Meta:
        abstract = True


class Project(CreatedAtModel):
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='project'
    )

    name = models.CharField(
        verbose_name='название',
        max_length=64,
    )
    details = models.TextField(
        verbose_name='описание',
        blank=True
    )
    repository_link = models.CharField(
        verbose_name='репозиторий',
        max_length=256,
        blank=True
    )
    is_active = models.BooleanField(  # False - удален
        verbose_name='активен',
        default=True
    )
    is_completed = models.BooleanField(
        verbose_name='выполнен',
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'


class ToDo(CreatedAtModel):
    project = models.ForeignKey(
        Project,
        related_name='todo',
        on_delete=models.CASCADE,
        verbose_name='проект'
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='creator',
        verbose_name='автор'
    )

    name = models.CharField(
        verbose_name='название',
        max_length=64,
    )
    content = models.TextField(
        verbose_name='текст',
        blank=True
    )
    is_active = models.BooleanField(  # False - удалена
        verbose_name='активен',
        default=True
    )
    is_completed = models.BooleanField(
        verbose_name='выполнен',
        default=False
    )
    updated_at = models.DateTimeField(
        verbose_name='обновлен',
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'