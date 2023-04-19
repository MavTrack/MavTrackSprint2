<template>
  <div class="container-fluid">
    <!--Welcome Title -->
    <div class="row align-items-center justify-content-center">
      <div class="col col-12 align-items-center justify-content-center text-danger">
        <blockquote><h2>
          {{ validUserName }}'s Training Plans
          </h2>
          <footer>
            <h4>
              <em>MavTrack</em>
            </h4>
          </footer>
        </blockquote>
      </div>
      <div class="col-12 col-md-10 col-lg-10 col-12 align-items-center justify-content-center">
        <div class="alert alert-success" v-if="showMsg === 'new'" :value="true">
          New training plan has been added.
        </div>
        <div class="alert alert-success" v-if="showMsg === 'update'" :value="true">
          Training plan information has been updated.
        </div>
        <div class="alert alert-success" v-if="showMsg === 'deleted'" :value="true">
          Selected training plan has been deleted.
        </div>
      </div>
    </div>

    <!-- Data table Small Screen-->
    <div class="row align-items-center justify-content-center">
      <div class="d-md-none" id="collapsable-card" style="width: 80%">
        <button type="button"
                class="btn btn-primary"
                @click="addNewPlan"
                style="background-color: white;
                border-color: white"
        >
          <svg xmlns="http://www.w3.org/2000/svg"
               width="50"
               height="50"
               fill="#0275d8"
               class="bi bi-plus-circle-fill"
               viewBox="0 0 16 16"
          >
            <path
                d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
          </svg>
        </button>
        <div class="card" v-for="plan in plans" v-bind:key="plan">
          <div class="card-header" :id="'heading' + plan.pk">
            <button class="btn btn-link collapsed"
                    data-bs-toggle="collapse"
                    :data-bs-target="'#collapse' + plan.pk"
                    aria-expanded="true"
                    :aria-controls="'collapse' + plan.pk"
            >
              <h6 style="color: #0275d8; float: left">{{ plan.name }}</h6>
            </button>
          </div>
          <div :id="'collapse' + plan.pk"
               class="collapse"
               :aria-labelledby="'heading' + plan.pk"
               data-bs-parent="#collapsable-card"
          >
            <div class="card-body">
              <p><b>Name:</b> {{ plan.name }}</p>
              <p><b>Category:</b> {{ plan.train_cat.name }}</p>
              <p><b>Goal:</b> {{ plan.train_goal.short_descr }}</p>
              <p><b>Level:</b> {{ plan.current_train_level.name }}</p>

              <div class="btn-group">
                <button @click="deletePlan(plan)"
                        style="background-color: transparent;
                        padding: 0;"
                >
                  <svg @click="deletePlan"
                       xmlns="http://www.w3.org/2000/svg"
                       width="20"
                       height="20"
                       fill="currentColor"
                       class="bi bi-trash-fill"
                       viewBox="0 0 16 16">
                    <path
                        d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

       <!-- Data table Large Screen-->
      <div class="col col-12 col-md-10 d-none d-xl-block d-lg-block d-md-block">
        <table class="table table-hover table-striped table-bordered" style="overflow-y: auto" :headers="headers">
          <thead>
          <tr class="table-danger">
            <th scope="col">Name</th>
            <th scope="col">Category</th>
            <th scope="col">Goal</th>
            <th scope="col">Level</th>
            <th scope="col">Delete</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="plan in plans" v-bind:key="plan">
            <th scope="row">
              <router-link :to="{ name: 'TrainingSchedules' }">{{ plan.name }}</router-link>
            </th>
            <td>{{ plan.train_cat.name }}</td>
            <td>{{ plan.train_goal.short_descr }}</td>
            <td>{{ plan.current_train_level.name }}</td>
            <td @click="deletePlan(plan)">
              <button style="background-color: transparent; padding: 0;">
                <svg @click="deletePlan"
                     xmlns="http://www.w3.org/2000/svg"
                     width="16"
                     height="16"
                     fill="currentColor"
                     class="bi bi-trash-fill"
                     viewBox="0 0 16 16"
                >
                  <path
                      d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                </svg>
              </button>
            </td>
          </tr>
          </tbody>
        </table>
        <button type="button" class="btn btn-danger" @click="addNewPlan">Add New Training Plan</button>
      </div>
    </div>
  </div>
</template>
<script>
import router from '../router';
import {APIService} from '@/http/APIService';


const apiService = new APIService();

export default {
  name: "TrainingPlanList",
  data: () => ({
    plans: [],
    validUserName: "Guest",
    planSize: 0,
    showMsg: '',
    isMobile: false,
    headers: [
      {text: 'Name', sortable: false, align: 'left',},
      {text: 'Category', sortable: false, align: 'left',},
      {text: 'Goal', sortable: false, align: 'left',},
      {text: 'Level', sortable: false, align: 'left',},
      {text: 'Update', sortable: false, align: 'left',},
      {text: 'Delete', sortable: false, align: 'left',}
    ],
  }),
  mounted() {
    this.getCustomers();
    this.showMessages();
  },
  methods: {
    onResize() {
      if (window.innerWidth > 600)
        this.isMobile = false;
      else
        this.isMobile = true;
    },
    showMessages() {
      console.log(this.$route.params.msg)
      if (this.$route.params.msg) {
        this.showMsg = this.$route.params.msg;
      }
    },
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
    loadPlans() {
      apiService.getTrainingPreferenceList()
          .then((response) => {
            this.plans = response.data;
            console.log('Plans', this.plans);
          })
          .catch((error) => {
            console.log('Error Load Plans', error);
          });
    },
    addNewPlan() {
      if (localStorage.getItem("isAuthenticates")
          && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
        router.push('/training-preferences/');
      } else {
        router.push("/auth");
      }
    },
    updatePlan(plan) {
      console.log('plans', plan)
      router.push('/training-preferences/' + plan.id);
    },
    deletePlan(plan) {
      if (confirm("Do you really want to delete?")) {
        apiService.deletePlan(plan.id).then(response => {
          if (response.status === 204) {
            router.push('/training-plans/')
            this.loadPlans()
            this.showMsg = 'deleted'
          }
        }).catch(error => {
          if (error.response.status === 401) {
            localStorage.removeItem('isAuthenticates');
            localStorage.removeItem('log_user');
            localStorage.removeItem('token');
            router.push("/auth");
          }
        });
      }
    }
  },
  created() {
    this.loadPlans()
  },
};
</script>
<style>
button {
  padding: 1rem;
  border: 0;
  cursor: pointer;
}
</style>