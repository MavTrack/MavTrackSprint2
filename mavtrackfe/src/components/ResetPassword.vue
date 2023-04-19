<template>
  <form class="container mt-5" @submit.prevent="resetPassword">
    <div class="form-group">
      <input type="hidden" name="uidb64" :value="uidb64">
      <input type="hidden" name="token" :value="token">
      <label for="new_password" class="text-danger">New password:</label>
      <input type="password" name="new_password" class="form-control" v-model="newPassword">
    </div>
    <div class="form-group">
      <label for="confirm_password" class="text-danger">Confirm password:</label>
      <input type="password" name="confirm_password" class="form-control" v-model="confirmPassword">
    </div>
    <button type="submit" class="btn btn-danger">Reset password</button>
  </form>
</template>

<script>
import {APIService} from '@/http/APIService';

const apiService = new APIService();

export default {
  props: ['uidb64', 'token'],
  data() {
    return {
      newPassword: '',
      confirmPassword: ''
    };
  },
  methods: {
    resetPassword() {
      try {
        const response = apiService.resetPassword({
          uidb64: this.uidb64,
          token: this.token,
          new_password: this.newPassword,
          confirm_password: this.confirmPassword
        });
        console.log(response.data);
        // handle success
      } catch (error) {
        console.error(error);
        // handle error
      }
    }
  },
}
</script>


