<template>
  <div>
    <div class="container-fluid">
      <div class="row justify-content-center">
        <div class="col-md-8">
          <!--Display Training Schedule if Any-->
          <div v-if="trainingSchedules.length > 0">
            <h2 class="text-danger">Your Training Schedule</h2>
            <div class="table-responsive">
              <table class="table table-striped table-bordered">
                <thead>
                <tr class="table-danger">
                  <th>Name</th>
                  <th>Day Tasks</th>
                </tr>
                </thead>
                <tbody>
                <!--Display List of Training Schedules-->
                <tr v-for="schedule in trainingSchedules" :key="schedule.id">
                  <td>{{ schedule.name }}</td>
                  <td>
                    <ul>
                      <li v-if="schedule.sunday">Sunday:
                        <span v-for="task in schedule.daily_task" :key="task.id">
                          <span v-if="task.day === 'Sunday'">
                            {{ task.distance }} miles in {{ task.pace }} minutes
                          </span>
                        </span>
                        <button class="btn btn-outline-danger btn-sm" @click="isComplete()">{{ 'Not Complete' }}
                        </button>
                      </li>
                      <li v-if="schedule.monday">Monday:
                        <span v-for="task in schedule.daily_task" :key="task.id">
                          <span v-if="task.day === 'Monday'">
                            {{ task.distance }} miles in {{ task.pace }} minutes
                          </span>
                        </span>
                        <button class="btn btn-outline-danger btn-sm" @click="isComplete()">{{ 'Not Complete' }}
                        </button>
                      </li>
                      <li v-if="schedule.tuesday">Tuesday:
                        <span v-for="task in schedule.daily_task" :key="task.id">
                          <span v-if="task.day === 'Tuesday'">
                            {{ task.distance }} miles in {{ task.pace }} minutes
                          </span>
                        </span>
                        <button class="btn btn-outline-danger btn-sm" @click="isComplete()">{{ 'Not Complete' }}
                        </button>
                      </li>
                      <li v-if="schedule.wednesday" class="d-flex align-items-center justify-content-center">Wednesday:
                        <span v-for="task in schedule.daily_task" :key="task.id" class="text-center">
                          <span v-if="task.day === 'Wednesday'" class="text-center">
                            {{ task.distance }} miles in {{ task.pace }} minutes
                          </span>
                        </span>
                        <button class="btn btn-outline-danger btn-sm float-right" @click="isComplete()">{{ 'Not Complete' }}
                        </button>
                      </li>
                      <li v-if="schedule.thursday">Thursday:
                        <span v-for="task in schedule.daily_task" :key="task.id">
                          <span v-if="task.day === 'Thursday'">
                            {{ task.distance }} miles in {{ task.pace }} minutes
                          </span>
                        </span>
                        <button class="btn btn-outline-danger btn-sm" @click="isComplete()">{{ 'Not Complete' }}
                        </button>
                      </li>
                      <li v-if="schedule.friday">Friday:
                        <span v-for="task in schedule.daily_task" :key="task.id">
                          <span v-if="task.day === 'Friday'">
                            {{ task.distance }} miles in {{ task.pace }} minutes
                          </span>
                        </span>
                        <button class="btn btn-outline-danger btn-sm" @click="isComplete()">{{ 'Not Complete' }}
                        </button>
                      </li>
                      <li v-if="schedule.saturday">Saturday:
                        <span v-for="task in schedule.daily_task" :key="task.id">
                          <span v-if="task.day === 'Saturday'">
                            {{ task.distance }} miles in {{ task.pace }} minutes
                          </span>
                        </span>
                        <button class="btn btn-outline-danger btn-sm" @click="isComplete()">{{ 'Not Complete' }}
                        </button>
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
    <!--    <div class="container mt-3">-->
    <!--      <h2 class="text-danger">What To Change Training Level</h2>-->
    <!--      <div class="card">-->
    <!--        <div class="card-body">-->

    <!--        </div>-->
    <!--      </div>-->
    <!--    </div>-->

    <button class="btn btn-danger" @click="savePreference">Next Level</button>
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
  },
  created() {
    this.loadTrainingPreferences()
    this.loadTrainingSchedules()
  },
}
</script>
<style scoped>
.table td {
  padding: 8px;
}

.table td:first-child {
  font-weight: bold;
}

.table li {
  list-style: none;
  margin-bottom: 4px;
}

.table-responsive {
  overflow-x: auto;
}

.table {
  font-size: 14px;
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
