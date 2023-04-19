<template>
  <div>
    <!-- Nav Bar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-gradient">
      <div class="container navcontainer">
        <!-- Logo -->
        <a class="navbar-brand" href="#">MavTrack App</a>

        <!-- Toggle Button for Mobile View -->
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <!-- Navigation Links -->
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ml-auto">

            <!-- Home Link -->
            <li class="nav-item active">
              <router-link class="nav-link" to="/" exact active-class="active">Home</router-link>
            </li>

            <!-- Training Plans Link -->
            <li class="nav-item">
              <router-link class="nav-link" :to="{name: 'TrainingPlans'}" active-class="active">Plans</router-link>
            </li>

            <!-- Training Preferences Link -->
            <li class="nav-item">
              <router-link class="nav-link" :to="{name: 'TrainingPreferencesCreate'}" active-class="active">Preferences</router-link>
            </li>

            <!-- Training Schedules Link -->
            <li class="nav-item">
              <router-link class="nav-link" :to="{name: 'TrainingSchedules'}" active-class="active">Schedules</router-link>
            </li>

            <!-- About Link -->
            <li class="nav-item">
              <router-link class="nav-link" :to="{name: 'about'}" active-class="active">About</router-link>
            </li>

            <!-- Login and Register Links - Visible only if not authenticated -->
            <li class="nav-item" v-if="!authenticated" @click="login">
              <router-link class="nav-link" active-class="active" :to="{name: 'Auth'}">Log in</router-link>
            </li>
            <li class="nav-item" v-if="!authenticated" @click="register">
              <router-link class="nav-link" active-class="active" :to="{name: 'Register'}">Register</router-link>
            </li>

            <!-- Logout Link - Visible only if authenticated -->
            <li class="nav-item" v-if="authenticated" @click="logout">
              <router-link class="nav-link" :to="{name: 'Auth'}">Logout</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Router View -->
    <router-view/>
  </div>
</template>

<script>
import router from './router';
import {APIService} from './http/APIService';

const apiService = new APIService();
export default {
  name: 'App',
  data: () => ({
    authenticated: false,
    dialog: false,
    menu: [
      {title: 'Home', url: "/"},
      {title: 'Customers', url: "/customer-list"},
    ]
  }),
  mounted() {
    apiService.getCustomerList().then(response => {
      this.authenticated = true;
    }).catch(error => {
      if (error.response.status === 401) {
        localStorage.removeItem('isAuthenticates');
        localStorage.removeItem('log_user');
        localStorage.removeItem('token');
        this.authenticated = false;
      }
    });
    console.log('this.authenticated--' + this.authenticated);
  },
  methods: {
    logout() {
      localStorage.removeItem('isAuthenticates');
      localStorage.removeItem('log_user');
      localStorage.removeItem('token');
      this.authenticated = false;
      // router.push('/');
      window.location = "/"
    },
    login() {
      router.push("/auth");
    },
  }
};
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  //color: #2c3e50;
}

nav {
  background-color: #fff !important;
}

.navbar {
  background-color: rgb(72, 72, 72) !important;
}

.navcontainer {
  background-color: black;
}

.navbar-brand {
  color: rgb(230, 43, 70) !important;
  padding-left: 0.60em !important;
}

.navbar-toggler-icon {
  background-image: url('data:image/svg+xml;charset=utf-8,<svg viewBox="0 0 30 30" xmlns="http://www.w3.org/2000/svg"><path stroke="rgba(230,43,70,1)" stroke-width="2" stroke-linecap="round" stroke-miterlimit="10" d="M4 7h22M4 15h22M4 23h22"/></svg>') !important;
  border: 1px rgba(230, 43, 70, 0.5) solid !important;
}

.navbar-nav .nav-link {
  color: whitesmoke !important;
  font-weight: bold;
  text-transform: uppercase;
}

.navbar-nav .nav-link:hover {
  color: rgba(230, 43, 70, 0.75) !important;
}

.navbar-nav .nav-link.active {
  color: red !important;
}
</style>