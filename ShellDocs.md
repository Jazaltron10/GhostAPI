### 01 - 05 
``` python

 ~/P/Dj/Co/GhostAPI  make shell 
python manage.py shell
Python 3.12.4 (main, Jun  6 2024, 18:26:44) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth import get_user_model
>>> user = get_user_model()
>>> u = user.objects.first()
>>> from backend.models import Article
>>> article = Article(title = "This is my second title", description = "This is my second description")
>>> article
<Article: This is my second title>
>>> article.save()
>>> from backend.models import Article
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> a = Article(title='django rest framework', description='this is the description for django rest framework')
>>> a.save()
>>> from backend.serializers import ArticleSerializer
>>> serializer = ArticleSerializer(a)
>>> serializer.data
{'title': 'django rest framework', 'description': 'this is the description for django rest framework', 'slug': 'django-rest-framework', 'published': '2024-09-29T17:54:51.760395Z'}
>>> 
>>> 
>>> # To Serialize the data 
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"title":"django rest framework","description":"this is the description for django rest framework","slug":"django-rest-framework","published":"2024-09-29T17:54:51.760395Z"}'
>>> 
>>> 
>>> 
>>> # Now to deserialize 
>>> 
>>> import io
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> 
>>> # Now we restore those native data types into our fully populated object and instances
>>> serializer = ArticleSerializer(data=data)
>>> serializer.is_valid()
True
>>> serializer.validated_data
{'title': 'django rest framework', 'description': 'this is the description for django rest framework'}
>>> 
>>> 
```

### 06 - ModelSerializer 
``` python
 ~/P/Dj/Co/GhostAPI  make shell 
python manage.py shell
Python 3.12.4 (main, Jun  6 2024, 18:26:44) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from backend.serializers import ArticleSerializer
>>> serializer = ArticleSerializer()
>>> print(repr(serializer))
ArticleSerializer():
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=255)
    description = CharField(style={'base_template': 'textarea.html'})
    slug = SlugField(allow_unicode=False, max_length=255)
    published = DateTimeField(read_only=True)
>>> 
```

