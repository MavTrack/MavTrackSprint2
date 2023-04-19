<template>
  <div>
    <!--Welcome Message-->
    <div class="container-fluid">
      <div class="row">
        <div class="col">
          <h1>MavTrack</h1>
          <h5>Welcome {{ validUserName }}!</h5>
        </div>
      </div>
    </div>

    <!--Fun Facts-->
    <div class="container-fluid">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="card-body">
            <div class="card p-1 shadow">
              <h4 class="card-title">Fun Exercise Fact</h4>
              <p class="card-text">
                {{ funFacts[Math.floor(Math.random() * funFacts.length)].fact }}
              </p>
            </div>
          </div>
        </div>

        <!--Daily Hints-->
        <div class="col-md-6">
          <div class="card-body">
            <div class="card p-1 shadow">
              <h4 class="card-title">Daily Hints</h4>
              <p class="card-text">
                {{ dailyHints[Math.floor(Math.random() * dailyHints.length)].hint }}
              </p>
            </div>
          </div>
        </div>

        <!--Recommended Exercises-->
        <div class="col-md-6">
          <div class="card-body">
            <div class="card p-1 shadow">
              <h4 class="card-title">Recommended Exercises</h4>
              <p class="card-text">
                {{ recommendedExercises[Math.floor(Math.random() * recommendedExercises.length)].recommended }}
              </p>
            </div>
          </div>
        </div>
      </div>

      <!--Go To Training Plan Button-->
      <div class="row justify-content-center">
        <div class="col-4">
          <br>
          <button class="btn btn-danger btn-block mb-3" @click="goToTrainingPlan">Start Training</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import router from "../router";
import {APIService} from "@/http/APIService.js";

const apiService = new APIService();

export default {
  name: "Home",

  data: () => ({
    funFacts: [],
    dailyHints: [],
    recommendedExercises: [],
    validUserName: "Guest",
  }),

  mounted() {
    this.getUser();
  },

  methods: {
    goToTrainingPlan() {
      this.$router.push('/training-plans');
    },
    loadFunFact() {
      apiService
          .getFunFactList()
          .then((response) => {
            this.funFacts = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
    },
    loadDailyHint() {
      apiService
          .getDailyHintList()
          .then((response) => {
            this.dailyHints = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
    },
    loadRecommendedExercise() {
      apiService
          .getRecommendedExerciseList()
          .then((response) => {
            this.recommendedExercises = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
    },
    getUser() {
      if (
          localStorage.getItem("isAuthenticates") &&
          JSON.parse(localStorage.getItem("isAuthenticates")) === true
      ) {
        this.validUserName = JSON.parse(localStorage.getItem("log_user"));
      }
    },
  },

  created() {
    this.loadFunFact();
    this.loadDailyHint();
    this.loadRecommendedExercise();
  },
};
</script>

<style scoped>
h1, h4 {
  color: rgb(230, 43, 70);
}

.card {
  background: black;
  color: whitesmoke;
  border: 1px solid whitesmoke;
}
</style>
