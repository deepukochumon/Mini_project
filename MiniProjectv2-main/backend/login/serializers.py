from rest_framework import serializers
from .models import labs

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    user_type=serializers.CharField()
    print('data serialized')

class attendance_query_serializer(serializers.Serializer):
    class_s = serializers.CharField()
    s_no = serializers.IntegerField()
    e_no = serializers.IntegerField()
    date = serializers.DateField()
    batch = serializers.CharField()
    diary = serializers.ListField(child=serializers.CharField())
    classes=serializers.ListField(child=serializers.CharField())
    batches_selected=serializers.ListField(child=serializers.CharField())


    def __init__(self, faculty_id=None, batches_selected=None, classes=None, diaries=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['batches_selected']=serializers.ListField(child=serializers.CharField(), initial=batches_selected)
        self.fields['classes']=serializers.ListField(child=serializers.CharField(), initial=classes)
        self.fields['diary']=serializers.ListField(child=serializers.CharField(), initial=diaries)


        '''if faculty_id is not None and batches_selected is not None and classes is not None:
            classes = set(classes)
            self.fields['class_s'].choices = [(obj, obj) for obj in classes]

            lab_insta = labs.objects.filter(faculty_handling_id=faculty_id, clas__in=classes, batch__in=batches_selected)
            self.fields['diary'].choices = [(obj, f"{obj.lab_name}-{obj.batch}") for obj in lab_insta]

            unique_batches = set(batches_selected)
            self.fields['batch'].choices = [(obj, obj) for obj in unique_batches]'''

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass