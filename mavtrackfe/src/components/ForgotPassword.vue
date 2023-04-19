<template>
  <div class="container mt-5">
    <div class="card mx-auto" style="max-width: 500px;">
      <div class="card-header bg-danger text-white">
        <h1 class="mb-0">Forgot Password</h1>
      </div>
      <div class="card-body">
        <div v-if="success" class="alert alert-success">
          An email with instructions on how to reset your password has been sent to {{ email }}.
        </div>
        <div v-else>
          <form @submit.prevent="forgotPassword">
            <div class="form-group">
              <input type="email" class="form-control" id="email" placeholder="Enter Registered Email Address:" v-model="email" required>
            </div>
            <button type="submit" class="btn btn-danger">Submit</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {APIService} from '@/http/APIService';

const apiService = new APIService();

export default {
  data() {
    return {
      email: '',
      success: false,
      error: '',
    }
  },
  methods: {
    forgotPassword() {
      const email = this.email;
      try {
        const response = apiService.forgotPassword(email);
        // Handle successful response
        console.log(response);
        this.success = true;
      } catch (error) {
        // Handle error
        console.error(error);
      }
    }
  }
}
</script>