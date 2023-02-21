import hashlib
import urllib
from django import template
from django.utils.safestring import mark_safe


register = template.Library()

# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=40):
  default = "https://example.com/static/images/defaultavatar.jpg"
  return "https://www.gravatar.com/avatar/%s?%d" % (hashlib.md5(email).hexdigest(), urllib.urlencode({'d':default, 's':str(size)}))

# return an image tag with the gravatar
# TEMPLATE USE:  {{ email|gravatar:150 }}
@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email, size)
    return mark_safe('' % (url, size, size))