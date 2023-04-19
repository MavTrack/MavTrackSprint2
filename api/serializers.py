from .models import *
from django.contrib.auth import get_user_model, authenticate
from rest_framework_jwt.serializers import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers

User = get_user_model()


# Fun Exercise Facts
class FunFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunFact
        fields = ['id', 'fact']


# Daily Hints
class DailyHintSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyHint
        fields = ['id', 'hint']


# Recommended Exercise
class RecommendedExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedExercise
        fields = ['id', 'name', 'recommended']


# Customer Prompts of Encouragement
class PromptsEncouragementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromptsEncouragement
        fields = '__all__'


# Training Categories
class TrainingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCategory
        fields = ['id', 'name', 'created_date', 'updated_date']


# Training Goals
class TrainingGoalSerializer(serializers.ModelSerializer):
    train_cat = TrainingCategorySerializer(many=True, read_only=True)

    class Meta:
        model = TrainingGoal
        fields = ['id', 'short_descr', 'long_descr', 'level', 'train_cat', 'user', 'created_date', 'updated_date']


# Training Levels
class TrainingLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingLevel
        fields = '__all__'


# Training Schedules
class TrainingScheduleGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingSchedule
        fields = '__all__'
        # fields = ['id', 'name', 'train_pref', 'user', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        #           'saturday', 'workout', 'is_achieved', 'daily_task', 'created_date']


# Training Preference Create
class TrainingPreferenceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingPreference
        fields = '__all__'


class TrainingScheduleCreateSerializer(serializers.ModelSerializer):
    train_pref = TrainingPreferenceCreateSerializer(read_only=True)

    class Meta:
        model = TrainingSchedule
        fields = '__all__'


# Get Training Preferences
class TrainingPreferenceGetSerializer(serializers.ModelSerializer):
    train_cat = TrainingCategorySerializer(read_only=True)
    train_goal = TrainingGoalSerializer(read_only=True)
    current_train_level = TrainingLevelSerializer(read_only=True)

    class Meta:
        model = TrainingPreference
        fields = '__all__'

    # # Example of how to Print out what is being validated
    # def create(self, validated_data):
    #     print('Creating new TrainingTest object with data:', validated_data)
    #     training_test = TrainingPreference.objects.create(**validated_data)
    #     return training_test

    # def create(self, validated_data):
    #     print('Creating new TrainingPreference object with data:', validated_data)
    #     training_test = TrainingPreference.objects.create(
    #         name=validated_data['name'],
    #         train_cat=validated_data['train_cat'],
    #         user=validated_data['user']
    #     )
    #     print('Created new TrainingPreference object:', training_test)
    #     return training_test


# Training Logs
class TrainingLogSerializer(serializers.ModelSerializer):
    train_skd = TrainingScheduleGetSerializer(many=True, read_only=True)

    class Meta:
        model = TrainingLog
        fields = ['id', 'train_skd', 'user', 'created_date', 'updated_date']


# Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True, style={'input_type': 'password'},
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True,
                         'min_length': 6},
            'password2': {'write_only': True,
                          'min_length': 6}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# Forgot Password
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError('User with this email address does not exist')
        return value


# Rest Password
class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=128)
    confirm_password = serializers.CharField(max_length=128)
    reset_token = serializers.CharField(max_length=64)
    uidb64 = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True)

    def validate(self, data):
        # Validate that the new password and confirm password match
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError('New password and confirm password do not match')

        # Decode the uidb64 to get the user ID
        try:
            uid = force_text(urlsafe_base64_decode(data['uidb64']))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError('Invalid reset password link')

        # Validate the token
        token_generator = default_token_generator
        if not token_generator.check_token(user, data['token']):
            raise serializers.ValidationError('Invalid reset password link')

        # Authenticate the user using the reset token
        user = authenticate(reset_token=data['reset_token'])
        if not user:
            raise serializers.ValidationError('Invalid reset token')

        return data

    def save(self):
        # Set the user's new password
        user = User.objects.get(pk=force_text(urlsafe_base64_decode(self.validated_data['uidb64'])))
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


# Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'name', 'address', 'cust_number', 'city', 'state', 'zipcode', 'email', 'cell_phone')
