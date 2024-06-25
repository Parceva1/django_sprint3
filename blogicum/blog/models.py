from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name=('Заголовок')
    )
    description = models.TextField(
        blank=False,
        null=False,
        verbose_name=('Описание')
    )
    slug = models.SlugField(
        unique=True,
        blank=False,
        null=False,
        verbose_name=('Идентификатор'),
        help_text=('Идентификатор страницы для URL; '
                   'разрешены символы латиницы, цифры, дефис и подчёркивание.')

    )
    is_published = models.BooleanField(
        default=True,
        blank=False,
        null=False,
        verbose_name=_('Опубликовано'),
        help_text=_('Снимите галочку, чтобы скрыть публикацию.')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name=_('Добавлено')
    )

    class Meta:
        verbose_name = _('категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name=_('Название места')
    )
    is_published = models.BooleanField(
        default=True,
        blank=False,
        null=False,
        verbose_name=_('Опубликовано'),
        help_text=_('Снимите галочку, чтобы скрыть публикацию.')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name=_('Добавлено')
    )

    class Meta:
        verbose_name = _('местоположение')
        verbose_name_plural = _('Местоположения')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name=_('Название')
    )
    text = models.TextField(
        blank=False,
        null=False,
        verbose_name=_('Текст')
    )
    pub_date = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name=_('Дата и время публикации'),
        help_text=_('Если установить дату и время в будущем'
                    ' — можно делать отложенные публикации.')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_('Автор публикации')
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Местоположение')
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name=_('Категория')
    )
    is_published = models.BooleanField(
        default=True,
        blank=False,
        null=False,
        verbose_name=_('Опубликовано'),
        help_text=_('Снимите галочку, чтобы скрыть публикацию.')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name=_('Добавлено'),
        help_text=_('Снимите галочку, чтобы скрыть публикацию.')
    )

    class Meta:
        verbose_name = _('публикация')
        verbose_name_plural = _('Публикации')

    def __str__(self):
        return self.title
