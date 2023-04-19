<template>
  <div>
    <div class="container-fluid">
      <div class="row justify-content-center">
        <div class="col-md-8">
          <!--Display Training Schedule if Any-->
          <div v-if="trainingSchedules.length > 0">
            <h2 class="text-danger">Your Training Schedule</h2>
            <!--Fun Facts-->
            <div class="container-fluid">
              <div class="row justify-content-center">
                <div class="col-md-6">
                  <div class="card-body">
                    <div class="card p-1 shadow">
                      <p class="card-text text-danger">
                        {{ promptEncouragement[Math.floor(Math.random() * promptEncouragement.length)].prompt }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="table-responsive">
              <table class="table table-hover table-striped table-bordered">
                <thead>
                <tr class="table-danger">
                  <th scope="col">Name</th>
                  <th scope="col">Day Tasks</th>
                </tr>
                </thead>
                <tbody>
                <!--Display List of Training Schedules-->
                <tr v-for="schedule in trainingSchedules" :key="schedule.id">
                  <td class="align-middle text-center">{{ schedule.name }}</td>
                  <td>
                    <ul>
                      <li v-if="schedule.sunday">Sunday:
                        <span>{{ schedule.sunday_workout }}: {{schedule.sunday_pace}} Minutes for {{schedule.sunday_distance}}</span>
                        <br>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="isComplete()">
                          {{ 'Not Complete' }}
                        </button>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="levelUp">Level Up</button>
                      </li>
                      <li v-if="schedule.monday">Monday:
                        <span>{{ schedule.monday_workout }}: {{schedule.monday_pace}} Minutes for {{schedule.monday_distance}}</span>
                        <br>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="isComplete()">
                          {{'Not Complete'}}
                        </button>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="levelUp">Level Up</button>
                      </li>
                      <li v-if="schedule.tuesday">Tuesday:
                        <span>{{ schedule.tuesday_workout }}: {{schedule.tuesday_pace}} Minutes for {{schedule.tuesday_distance}}</span>
                        <br>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="isComplete()">
                          {{ 'Not Complete' }}
                        </button>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="levelUp">Level Up</button>
                      </li>
                      <li v-if="schedule.wednesday">Wednesday:
                        <span>{{ schedule.wednesday_workout }}: {{schedule.wednesday_pace}} Minutes for {{schedule.wednesday_distance}}</span>
                        <br>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="isComplete()">
                          {{ 'Not Complete' }}
                        </button>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="levelUp">Level Up</button>
                      </li>
                      <li v-if="schedule.thursday">Thursday:
                        <span>{{ schedule.thursday_workout }}: {{schedule.thursday_pace}} Minutes for {{schedule.thursday_distance}}</span>
                        <br>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="isComplete()">{{ 'Not Complete' }}
                        </button>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="levelUp">Level Up</button>
                      </li>
                      <li v-if="schedule.friday">Friday:
                        <span>{{ schedule.friday_workout }}: {{schedule.friday_pace}} Minutes for {{schedule.friday_distance}}</span>
                        <br>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="isComplete()">{{ 'Not Complete' }}
                        </button>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="levelUp">Level Up</button>
                      </li>
                      <li v-if="schedule.saturday">Saturday:
                        <span>{{ schedule.saturday_workout }}: {{schedule.saturday_pace}} Minutes for {{schedule.saturday_distance}}</span>
                        <br>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="isComplete()">{{ 'Not Complete' }}
                        </button>
                        <button class="btn btn-outline-danger btn-xs ml-3 my-2" @click="levelUp">Level Up</button>
                      </li>
                    </ul>
                  </td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div v-else>
            <p class="text-muted text-center">No Running Schedule Found</p>
          </div>
        </div>
      </div>
    </div>

    <!--Next level-->
    <div class="container mt-3">
      <h2 class="text-danger"></h2>
      <div class="card">
        <div class="card-body">
          <button class="btn btn-danger" @click="goToTrainingPlans">Training Plans</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import {APIService} from '@/http/APIService';
import router from '@/router';

const apiService = new APIService();

export default {
  data() {
    return {
      trainingPreferences: [],
      trainingSchedules: [],
      promptEncouragement: [],
    }
  },
  mounted() {
    this.getCustomers();
  },
  methods: {
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
    loadTrainingPreferences() {
      apiService.getTrainingPreferenceList()
          .then((response) => {
            this.trainingPreferences = response.data;
            console.log('Preferences', this.trainingPreferences);
          })
          .catch((error) => {
            console.log('Error Load Preferences', error);
          });
    },
    loadTrainingSchedules() {
      apiService.getTrainingScheduleList()
          .then((response) => {
            this.trainingSchedules = response.data.data;
            console.log('Schedules', this.trainingSchedules);
          })
          .catch((error) => {
            console.log('Error Load Goals', error);
          });
    },
    loadPromptEncouragement() {
      apiService.getPromptsEncouragementList()
          .then((response) => {
            this.promptEncouragement = response.data;
            console.log('Prompts', this.promptEncouragement);
          })
          .catch((error) => {
            console.log('Error Load Prompt', error);
          });
    },
    goToTrainingPlans() {
      router.push("/training-plans/");
    }
  },
  created() {
    this.loadTrainingPreferences()
    this.loadTrainingSchedules()
    this.loadPromptEncouragement()
  },
}
</script>
<style scoped>
.table th {
  font-size: 20px;
}
.table td {
  padding: 8px;
}

.table td:first-child {
  font-weight: bold;
  font-size: 18px;
}

.table li {
  list-style: none;
  margin-bottom: 4px;
}

.table-responsive {
  overflow-x: auto;
}

.table {
  font-size: 16px;
}

@media screen and (max-width: 768px) {
  .table-responsive {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

@media screen and (max-width: 576px) {
  .table-responsive {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

</style>
