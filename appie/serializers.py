from rest_framework import serializers
from appie.models import Student
from appie.validators import starts_with_r

# class StudentSerializer(serializers.Serializer):
#     # id = serializers.IntegerField()
#     name = serializers.CharField(max_length = 55,validators = [starts_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length = 50)

#     # for creating student
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance
    
#     #field level validation
#     def validate_roll(self,value):
#         if value >= 2000:
#             raise serializers.ValidationError('We are already occupied')
#         return value
    
    # #object level validation
    # def validate(self,data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'rohit' and ct.lower() != 'kannada':
    #         raise serializers.ValidationError('city must be Kannada.')
    #     return data
    
###Here starts with ModelSerializer concept
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only = True)
    ## argument as validator
    # name = serializers.CharField(validators = [starts_with_r])
    class Meta:
        model = Student
        fields = ['name','roll','city']
        # read_only_fields = ['name','city']
        #we can give different property using extra_kwargs
        # extra_kwargs = {
        #     'name':{'read_only':True},
        # }

    
    #field level validation
    def validate_roll(self,value):
        if value >= 2000:
            raise serializers.ValidationError('We are already occupied')
        return value    
        
    #object level validation
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'anish' and ct.lower() != 'lalitpur':
            raise serializers.ValidationError('city must be Lalitpur.')
        return data