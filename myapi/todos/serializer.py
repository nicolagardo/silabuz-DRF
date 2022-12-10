from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
       model = Todo
       fields = (
        "id",
        "title",
        "body",
        "created_at",
        "updated_at",
        "deleted_at",
        "done_at",
        "status",
       )
       read_only_fields = (
       'created_at', 
    #    'done_at', 
       'updated_at', 
       'deleted_at',
       )

class TodoSerializer2(serializers.ModelSerializer):
    class Meta:
       model = Todo
       fields = (
        '__all__',
       )
       read_only_fields = (
       'created_at', 
    #    'done_at', 
       'updated_at', 
       'deleted_at',
       )

      
    

    
class TestTodoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    body = serializers.CharField()

    lista = "!#$%&/()="

    def validate_title(self, value):
        if "$" in value:
            raise serializers.ValidationError(
                "Error, el título no puede tener el símbolo de $")
        return value

    def validate_body(self, value):
        if "$" in value:
            raise serializers.ValidationError(
                "Error, el título no puede tener el símbolo de $")
        return value

    def validate_body(self, value):
        if self.lista not in value:
            return value
        raise serializers.ValidationError(
            "Error, el título no puede tener el símbolo de &")
    