from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()


# Fun Exercise Facts
class FunFact(models.Model):
    fact = models.TextField()

    def __str__(self):
        return self.fact


# Daily Hints
class DailyHint(models.Model):
    hint = models.TextField()

    def __str__(self):
        return self.hint


# Recommended Exercise
class RecommendedExercise(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True, )
    recommended = models.TextField()

    def __str__(self):
        return f'(Recommended exercise is {self.name}: {self.recommended}.)'


# Customer Prompts of Encouragement
class PromptsEncouragement(models.Model):
    prompt = models.TextField()

    def __str__(self):
        return self.prompt


# Training Categories
class TrainingCategory(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True, null=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


# Training Goals
class TrainingGoal(models.Model):
    short_descr = models.CharField(max_length=100)
    long_descr = models.CharField(max_length=255)
    level = models.IntegerField()
    train_cat = models.ManyToManyField(TrainingCategory)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True, null=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.short_descr


# Training Schedules
class TrainingSchedule(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    train_pref = models.ForeignKey('TrainingPreference', blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday_workout = models.CharField(max_length=255, blank=True, null=True)
    monday_workout = models.CharField(max_length=255, blank=True, null=True)
    tuesday_workout = models.CharField(max_length=255, blank=True, null=True)
    wednesday_workout = models.CharField(max_length=255, blank=True, null=True)
    thursday_workout = models.CharField(max_length=255, blank=True, null=True)
    friday_workout = models.CharField(max_length=255, blank=True, null=True)
    saturday_workout = models.CharField(max_length=255, blank=True, null=True)
    sunday_pace = models.CharField(max_length=255, blank=True, null=True)
    monday_pace = models.CharField(max_length=255, blank=True, null=True)
    tuesday_pace = models.CharField(max_length=255, blank=True, null=True)
    wednesday_pace = models.CharField(max_length=255, blank=True, null=True)
    thursday_pace = models.CharField(max_length=255, blank=True, null=True)
    friday_pace = models.CharField(max_length=255, blank=True, null=True)
    saturday_pace = models.CharField(max_length=255, blank=True, null=True)
    sunday_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monday_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tuesday_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wednesday_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    thursday_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    friday_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    saturday_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_complete_sunday = models.BooleanField(default=False)
    is_complete_monday = models.BooleanField(default=False)
    is_complete_tuesday = models.BooleanField(default=False)
    is_complete_wednesday = models.BooleanField(default=False)
    is_complete_thursday = models.BooleanField(default=False)
    is_complete_friday = models.BooleanField(default=False)
    is_complete_saturday = models.BooleanField(default=False)
    skd_level = models.IntegerField(default=1, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True, null=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


# Training Levels
class TrainingLevel(models.Model):
    name = models.CharField(max_length=255, null=True)
    hierarchy = models.IntegerField(blank=True)
    train_cat = models.ManyToManyField(TrainingCategory, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True, null=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


# Training Preferences
class TrainingPreference(models.Model):
    name = models.CharField(max_length=255, null=True)
    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    current_train_level = models.ForeignKey(TrainingLevel, null=True, blank=True, on_delete=models.CASCADE)
    train_cat = models.ForeignKey(TrainingCategory, null=True, blank=True, on_delete=models.CASCADE)
    train_goal = models.ForeignKey(TrainingGoal, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True, null=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return f'({self.user}s training goal is {self.train_goal})'


# Training Logs
class TrainingLog(models.Model):
    train_skd = models.ManyToManyField(TrainingSchedule)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True, null=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return f'({self.user} has {self.train_skd} schedule.)'


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    cust_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_number)
