from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairViewSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls,user):
        token = super(MyTokenObtainPairViewSerializer,cls).get_token(user)
#custom fields
        token['username']=user.username,
        token['id']:user.id
        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True,style={'input_type': 'password'},validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True,style={'input_type':'password'})
    email =  serializers.EmailField(required=True,  validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
    
        extra_kwargs = {
            'first_name':{'required':True},
            'last_name':{'required':True}
        }

    def validate(self,attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({"password":"password fields don't match"})
        return attrs



    def create(self, validated_data):
        # user = User.objects.create(**validated_data)
        # user.save()
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# --------------------------------------PART 9--------------------------------------------------------

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,style={'input_type':'password'}, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True,style={'input_type':'password'} ,required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
# Extract username from request and grant it to variable user
        if not user.check_password(value):
#check_password is an in-built function to check current loged-in user's password. 
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
# Here look-up is done for an existing value in password field. 
        return value

    def update(self, instance, validated_data):
        
        
        user=self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})


        instance.set_password(validated_data['password'])
        instance.save()

        return instance

#------------------------------UPDATE USERPROFILE-------------------------------------

class UpdateSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    extra_kwargs={
        'first_name':{'required':True},
        'last_name':{'required':True}
    }
# Function to validate email
    def validate_email(self,value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email":"This email id is already taken"})
        return value
    
# Function to validate username
    def validate_username(self,value): # validate method should be used to validate and raise errors.
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username":"This username is already taken"})
        return value


    def update(self, instance, validated_data):
# If the user's pk matches with instance's pk  or pk of object whose JWT is being authorized     
        user=self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})


        instance.username=validated_data['username']
        instance.email=validated_data['email']
        instance.first_name=validated_data['first_name']
        instance.last_name=validated_data['last_name']
        instance.save()
        return instance