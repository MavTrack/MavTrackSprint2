from django.contrib import admin

from .models import (
    FunFact,
    DailyHint,
    RecommendedExercise,
    PromptsEncouragement,
    TrainingCategory,
    TrainingGoal,
    TrainingSchedule,
    TrainingLevel,
    TrainingPreference,
    TrainingLog,
    Customer,
)


# Customize the FunFactAdmin class
class FunFactAdmin(admin.ModelAdmin):
    list_display = ('fact',)


# Customize the DailyHintAdmin class
class DailyHintAdmin(admin.ModelAdmin):
    list_display = ('hint',)


# Customize the RecommendedExerciseAdmin class
class RecommendedExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'recommended',)

# Customize the Prompt Encouragement class
class PromptsEncouragementAdmin(admin.ModelAdmin):
    list_display = ('prompt',)

# Customize the TrainingGoalAdmin class
class TrainingGoalAdmin(admin.ModelAdmin):
    list_display = ('short_descr', 'long_descr', 'user', 'level', 'display_train_cat')

    def display_train_cat(self, obj):
        return ", ".join([train_cat.name for train_cat in obj.train_cat.all()])

    display_train_cat.short_description = 'Training Category'

    list_filter = ('level', 'user', 'created_date', 'updated_date',)
    search_fields = ('short_descr', 'long_descr',)
    ordering = ['user__username']


# Customize the TrainingCategoryAdmin class
class TrainingCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'updated_date')
    list_filter = ('created_date', 'updated_date')
    search_fields = ('name',)
    ordering = ['name']


# Customize the TrainingScheduleAdmin class
class TrainingScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'skd_level', 'created_date')
    list_filter = ('name', 'skd_level', 'created_date', 'updated_date')
    search_fields = ('name', 'skd_level',)


# Customize the TrainingPlanAdmin class
class TrainingPlanAdmin(admin.ModelAdmin):
    list_display = ('train_goal', 'train_cat', 'created_date', 'updated_date')
    list_filter = ('train_goal', 'train_cat', 'created_date', 'updated_date')
    ordering = ['train_goal']


# Customize the TrainingLevelAdmin class
class TrainingLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'hierarchy', 'created_date', 'updated_date')
    list_filter = ('created_date', 'updated_date')
    ordering = ['hierarchy']


# Customize the TrainingPreferenceAdmin class
class TrainingPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'train_cat', 'train_goal', 'current_train_level')
    list_filter = ('train_goal', 'created_date', 'updated_date')
    search_fields = ('user__username', 'train_goal__short_descr')
    ordering = ['user__username']


# Customize the TrainingLogAdmin class
class TrainingLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_date', 'updated_date')
    list_filter = ('created_date', 'updated_date')
    search_fields = ('user__username', 'train_skd__daily_task__task_descr')
    ordering = ['user__username']


# Customize the CustomerAdmin class
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'cust_number', 'email', 'created_date', 'updated_date',)
    list_filter = ('cust_number', 'name', 'city', 'created_date', 'updated_date',)
    search_fields = ('name', 'cust_number', 'email',)
    ordering = ['cust_number']


admin.site.register(FunFact, FunFactAdmin)
admin.site.register(DailyHint, DailyHintAdmin)
admin.site.register(RecommendedExercise, RecommendedExerciseAdmin)
admin.site.register(PromptsEncouragement, PromptsEncouragementAdmin)
admin.site.register(TrainingCategory, TrainingCategoryAdmin)
admin.site.register(TrainingGoal, TrainingGoalAdmin)
admin.site.register(TrainingSchedule, TrainingScheduleAdmin)
admin.site.register(TrainingLevel, TrainingLevelAdmin)
admin.site.register(TrainingPreference, TrainingPreferenceAdmin)
admin.site.register(TrainingLog, TrainingLogAdmin)
admin.site.register(Customer, CustomerAdmin)
