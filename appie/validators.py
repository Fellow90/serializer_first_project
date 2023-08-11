from rest_framework import serializers

#validator function so that first index of the name should be r
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with R')