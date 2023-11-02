import logging

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeBaseInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Укажите основной раздел')

        self.count_is_main_tag = 0

        for form in self.forms:
            if self.count_is_main_tag > 0 and form.cleaned_data.get('is_main'):
                raise ValidationError('Основным может быть только 1 тег')
            else:
                if form.cleaned_data.get('is_main'):
                    logging.info(f"{form.cleaned_data.get('tag')} - основной раздел")
                    self.count_is_main_tag += 1
                else:
                    continue
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeBaseInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass