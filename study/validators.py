from django.core.exceptions import ValidationError
import re


def validate_youtube_links(value):
    youtube_pattern = re.compile(r'^https?://(?:www\.)?youtube\.com/.+')

    if not youtube_pattern.match(value):
        raise ValidationError("Ссылки на сторонние ресурсы, кроме youtube.com, не разрешены.")
