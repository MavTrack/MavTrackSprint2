<template>
  <div>
    <!--Page Title-->
    <div class="container-fluid mt-3 title">
      <div class="row">
        <div class="col">
          <h2 style="color: rgba(230, 43, 70, 1);">Customize Your Training Plan</h2>
        </div>
      </div>
    </div>

    <!--Name Training Plan-->
    <div class="container py-5">
      <div class="row">
        <div class="col-md-7 mb-5 mx-auto text-center">
          <h3 class="mb-4">Name Your Training Plan</h3>
          <input type="text" v-model="name" placeholder="Name Your Training Plan"
                 style="border-color: rgb(230, 43, 70)">
        </div>

        <!--List to select categories-->
        <div class="col-md-6 mx-auto text-center">
          <h4 class="mb-4">Choose Your Fitness Training Category</h4>
          <ul class="list-group">
            <li v-for="category in categories" :key="category.id" :value="category.id" class="list-group-item">
              <button class="btn btn-outline-danger btn-block" @click="selectCategory(category)">
                {{ category.name }}
              </button>
            </li>
          </ul>
        </div>

        <!--List to select goals-->
        <div class="col-md-6" v-if="selectedCategory">
          <h4 class="mb-4">Choose Your Fitness Training Goal</h4>
          <ul class="list-group">
            <li v-for="goal in goals.filter(g => g.train_cat.some(c => c.name === this.selectedCategory.name))"
                :key="goal.id"
                :value="goal.id"
                class="list-group-item">
              <button class="btn btn-outline-danger btn-block" @click="selectGoal(goal)">
                {{ goal.short_descr }}
              </button>
            </li>
          </ul>
        </div>

        <!--List to select levels-->
        <div class="col-md-6" v-if="selectedGoal">
          <h4 class="mb-4">Choose Your Training Level</h4>
          <ul class="list-group">
            <li v-for="level in levels" :key="level.id" :value="level.id" class="list-group-item">
              <button class="btn btn-outline-danger btn-block" @click="selectLevel(level)">
                {{ level.name }}
              </button>
            </li>
          </ul>
        </div>

        <!--List to select days-->
        <div class="col-md-6" v-if="selectedLevel">
          <h4 class="mb-4">Choose Your Fitness Training Days</h4>
          <div>
            <label class="btn btn-outline-danger btn-block">
              <input type="checkbox" v-model="days.sunday" class="d-none"/> Sunday
            </label>
            <label class="btn btn-outline-danger btn-block">
              <input type="checkbox" v-model="days.monday" class="d-none"/> Monday
            </label>
            <label class="btn btn-outline-danger btn-block">
              <input type="checkbox" v-model="days.tuesday" class="d-none"/> Tuesday
            </label>
            <label class="btn btn-outline-danger btn-block">
              <input type="checkbox" v-model="days.wednesday" class="d-none"/> Wednesday
            </label>
            <label class="btn btn-outline-danger btn-block">
              <input type="checkbox" v-model="days.thursday" class="d-none"/> Thursday
            </label>
            <label class="btn btn-outline-danger btn-block">
              <input type="checkbox" v-model="days.friday" class="d-none"/> Friday
            </label>
            <label class="btn btn-outline-danger btn-block">
              <input type="checkbox" v-model="days.saturday" class="d-none"/> Saturday
            </label>
          </div>
        </div>
      </div>

      <!--User Error Message-->
      <div class="container mt-3">
        <div class="card">
          <div class="card-body">
            <h3 v-if="errorMessage" class="btn-danger">{{ errorMessage }}</h3>
          </div>
        </div>
      </div>

      <!--User Selected Preferences-->
      <div v-if="selectedLevel" class="container mt-3">
        <h2 class="text-danger">You have selected:</h2>
        <div class="card">
          <div class="card-body">
            <p class="card-text">Category: <strong>{{ selectedCategory.name }}</strong></p>
            <p class="card-text">Goal: <strong>{{ selectedGoal.short_descr }}</strong></p>
            <p class="card-text">Level: <strong>{{ selectedLevel.name }}</strong></p>
            <p class="card-text">Your training days are: <strong>{{ selectedDays.join(', ') }}</strong></p>
          </div>
        </div>
      </div>
    </div>

    <!--Cancel Button-->
    <button class="btn btn-secondary mr-3" @click="cancelPreference">Cancel</button>

    <!--Create Schedule Button-->
    <button class="btn btn-danger" @click="savePreference">View Schedule</button>

  </div>
</template>
<script>
import {APIService} from '@/http/APIService';
import router from '@/router';

const apiService = new APIService();

export default {
  data() {
    return {
      name: '',
      days: {
        monday: false,
        tuesday: false,
        wednesday: false,
        thursday: false,
        friday: false,
        saturday: false,
        sunday: false,
      },
      sundayWorkout: '',
      mondayWorkout: '',
      tuesdayWorkout: '',
      wednesdayWorkout: '',
      thursdayWorkout: '',
      fridayWorkout: '',
      saturdayWorkout: '',
      sundayPace: '',
      mondayPace: '',
      tuesdayPace: '',
      wednesdayPace: '',
      thursdayPace: '',
      fridayPace: '',
      saturdayPace: '',
      sundayDistance: '',
      mondayDistance: '',
      tuesdayDistance: '',
      wednesdayDistance: '',
      thursdayDistance: '',
      fridayDistance: '',
      saturdayDistance: '',
      categories: [],
      goals: [],
      levels: [],
      trainingPreferences: [],
      selectedCategory: null,
      selectedGoal: null,
      selectedLevel: null,
      selectedPreference: [],
      errorMessage: '',
    };
  },
  mounted() {
    this.getCustomers();
  },
  methods: {
    // Get User
    getCustomers() {
      apiService.getCustomerList().then(response => {
        this.customers = response.data.data;
        console.log('Customers', this.customers)
        this.customerSize = this.customers.length;
        if (localStorage.getItem("isAuthenticates")
            && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
          this.validUserName = JSON.parse(localStorage.getItem("log_user"));
        }
      }).catch(error => {
        if (error.response.status === 401) {
          localStorage.removeItem('isAuthenticates');
          localStorage.removeItem('log_user');
          localStorage.removeItem('token');
          router.push("/auth");
        }
      });
    },
    // Load Training Categories
    loadCategories() {
      apiService.getTrainingCategoryList()
          .then((response) => {
            this.categories = response.data;
            console.log('Categories', this.categories);
          })
          .catch((error) => {
            console.log('Error Load Categories', error);
          });
    },
    // Load Training Goals
    loadGoals() {
      apiService.getTrainingGoalList()
          .then((response) => {
            this.goals = response.data;
            console.log('Goals', this.goals);
          })
          .catch((error) => {
            console.log('Error Load Goals', error);
          });
    },
    // Load Training Levels
    loadLevels() {
      apiService.getTrainingLevelList()
          .then((response) => {
            this.levels = response.data;
            console.log('Levels', this.levels);
          })
          .catch((error) => {
            console.log('Error Load Levels', error);
          });
    },
    // Load Training Preferences
    loadTrainingPreferences() {
      apiService.getTrainingPreferenceList()
          .then((response) => {
            this.trainingPreferences = response.data;
            console.log('Load Preferences', this.trainingPreferences);
          })
          .catch((error) => {
            console.log('Error Load Preferences', error);
          });
    },
    // User Selected Training Category
    selectCategory(category) {
      this.selectedCategory = category;
      this.selectedGoal = '';
    },
    // User Selected Training Goal
    selectGoal(goal) {
      this.selectedGoal = goal;
      this.selectedLevel = '';
    },
    // User Selected Training Level
    selectLevel(level) {
      this.selectedLevel = level;
    },

    // Validate Training Preference Form
    validateForm() {
      let message = '';

      // Form Error Messages
      if (!this.name) {
        message = 'Please enter a name';
      } else if (!this.selectedCategory) {
        message = 'Please select a category';
      } else if (!this.selectedGoal) {
        message = 'Please select a goal';
      } else if (!this.selectedLevel) {
        message = 'Please select a level';
      } else if (this.selectedDays.length === 0) {
        message = 'Please select a least one day';
      }

      // Display the message to the user
      if (message) {
        this.errorMessage = message;
        return false;
      }
      return true;
    },

    // Save Preferences To Database
    savePreference() {
      // Validate that all preferences are valid
      if (this.validateForm()) {
        const preferenceData = {
          name: this.name,
          train_cat: this.selectedCategory.id,
          train_goal: this.selectedGoal.id,
          monday: this.days.monday,
          tuesday: this.days.tuesday,
          wednesday: this.days.wednesday,
          thursday: this.days.thursday,
          friday: this.days.friday,
          saturday: this.days.saturday,
          sunday: this.days.sunday,
          current_train_level: this.selectedLevel.id,
        };
        apiService.createTrainingPreference(preferenceData)
            .then((response) => {
              console.log('Create Preferences', response.data);
              this.trainingPreferences.push(response.data);
              this.createDailyTask()
            })
            .catch((error) => {
              console.log('Error Create Pref', error);
            });
      }
    },

    createDailyTask() {
      // Create Training Schedule Logic
      if (this.selectedCategory.name === 'Running' && this.selectedGoal.short_descr === '5K' &&
          this.selectedLevel.name === 'Beginner') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Sunday Workout Run"
              this.sundayPace = "11:00"
              this.sundayDistance = 1.0
              break
            case 'Monday':
              this.mondayWorkout = "Monday Workout Run"
              this.mondayPace = "11:15"
              this.mondayDistance = 1.1
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Tuesday Workout"
              this.tuesdayPace = "11:15"
              this.tuesdayDistance = 1.1
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Wednesday Workout"
              this.wednesdayPace = "11:15"
              this.wednesdayDistance = 1.1
              break
            case 'Thursday':
              this.thursdayWorkout = "Thursday Workout"
              this.thursdayPace = "11:15"
              this.thursdayDistance = 1.1
              break
            case 'Friday':
              this.fridayWorkout = "Friday Workout"
              this.fridayPace = "11:15"
              this.fridayDistance = 1.1
              break
            case 'Saturday':
              this.saturdayWorkout = "Saturday Workout"
              this.saturdayPace = "11:15"
              this.saturdayDistance = 1.1
              break
          }
        })
      } else if (this.selectedCategory.name === 'Running' && this.selectedGoal.short_descr === 'Half Marathon' &&
          this.selectedLevel.name === 'Beginner') {
        this.selectedDays.forEach(day => {
          switch (day) {
            case 'Sunday':
              this.sundayWorkout = "Sunday Workout Run"
              this.sundayPace = "10:30"
              this.sundayDistance = 1.0
              break
            case 'Monday':
              this.mondayWorkout = "Monday Workout Run"
              this.mondayPace = "10:45"
              this.mondayDistance = 1.1
              break
            case 'Tuesday':
              this.tuesdayWorkout = "Tuesday Workout"
              this.tuesdayPace = "11:15"
              this.tuesdayDistance = 1.1
              break
            case 'Wednesday':
              this.wednesdayWorkout = "Wednesday Workout"
              this.wednesdayPace = "11:15"
              this.wednesdayDistance = 1.1
              break
            case 'Thursday':
              this.thursdayWorkout = "Thursday Workout"
              this.thursdayPace = "11:15"
              this.thursdayDistance = 1.1
              break
            case 'Friday':
              this.fridayWorkout = "Friday Workout"
              this.fridayPace = "11:15"
              this.fridayDistance = 1.1
              break
            case 'Saturday':
              this.saturdayWorkout = "Saturday Workout"
              this.saturdayPace = "11:15"
              this.saturdayDistance = 1.1
              break
          }
        })
      }
      this.createSchedule()
    },

    // User Selected Training Task
    createSchedule(task) {
      // Save The Training Preference ID
      if (this.trainingPreferences.length > 0) {
        this.selectedPreference.push(this.trainingPreferences[this.trainingPreferences.length - 1].id);
      }
      // Schedule Data
      const scheduleData = {
        name: this.name,
        sunday_workout: this.sundayWorkout,
        monday_workout: this.mondayWorkout,
        tuesday_workout: this.tuesdayWorkout,
        wednesday_workout: this.wednesdayWorkout,
        thursday_workout: this.thursdayWorkout,
        friday_workout: this.fridayWorkout,
        saturday_workout: this.saturdayWorkout,
        sunday_pace: this.sundayPace,
        monday_pace: this.mondayPace,
        tuesday_pace: this.tuesdayPace,
        wednesday_pace: this.wednesdayPace,
        thursday_pace: this.thursdayPace,
        friday_pace: this.fridayPace,
        saturday_pace: this.saturdayPace,
        sunday_distance: this.sundayDistance,
        monday_distance: this.mondayDistance,
        tuesday_distance: this.tuesdayDistance,
        wednesday_distance: this.wednesdayDistance,
        thursday_distance: this.thursdayDistance,
        friday_distance: this.fridayDistance,
        saturday_distance: this.saturdayDistance,
        train_pref: this.selectedPreference,
        monday: this.days.monday,
        tuesday: this.days.tuesday,
        wednesday: this.days.wednesday,
        thursday: this.days.thursday,
        friday: this.days.friday,
        saturday: this.days.saturday,
        sunday: this.days.sunday,
      };
      apiService.createTrainingSchedule(scheduleData)
          .then((response) => {
            console.log('Create Schedule', response.data);
            router.push("/training-schedules/");
          })
          .catch((error) => {
            console.log('Error Create Schedule', error);
          });
    },
    cancelPreference() {
      router.push("/training-plans");
    }
  },
  computed: {
    // User Selected Training Days
    selectedDays() {
      const day = [];
      if (this.days.monday) day.push('Monday');
      if (this.days.tuesday) day.push('Tuesday');
      if (this.days.wednesday) day.push('Wednesday');
      if (this.days.thursday) day.push('Thursday');
      if (this.days.friday) day.push('Friday');
      if (this.days.saturday) day.push('Saturday');
      if (this.days.sunday) day.push('Sunday');
      return day;
    },
  },
  created() {
    this.loadCategories();
    this.loadGoals();
    this.loadLevels();
    this.loadTrainingPreferences()
  },
};
</script>

<style scoped>


</style>