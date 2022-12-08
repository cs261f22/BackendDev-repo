### drf-spectacular

drf-spectacular is a schema generation tool for the Django REST framework as defined by the OpenAPI specification. It basically generates an OpenAPI compatible document from Django code, which can then be hosted by Django.

https://spec.openapis.org/oas/v3.0.3

https://drf-spectacular.readthedocs.io/en/latest/readme.html

https://www.django-rest-framework.org/topics/documenting-your-api/

#### What's Left

The default generation provides a skeleton of a document that is primarily lacking in descriptions. The examples are fine, but the documentation lacks any tangible descriptions. Modifying this entails 'customization' of functions with decorators, of which there are many for each type of function. Serializers have extend_schema_serializer, while viewsets can simply use extend_schema; this is at least the conclusion to which I've arrived. My understanding of this is clearly faulty, however - because the descriptions appear on some HTTP request methods but not others, and extend_schema_serializer seems to only allow for the display of custom example requests and responses.

https://drf-spectacular.readthedocs.io/en/latest/customization.html

```python
@extend_schema(
        summary="Deletes a Student",
        description="Deletes a Student table from the database."
    )
    def destroy(self, request, pk=None):
    	pass
```

This is an example of a custom description of a DELETE request. Getting this to work with GET or PUT is a mystery, because I'm personally not sure where they're defined.