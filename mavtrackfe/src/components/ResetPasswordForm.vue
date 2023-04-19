<template>
  <div class="container mt-5">
    <div class="card mx-auto" style="max-width: 500px;">
      <div class="card-header bg-danger text-white">
        <h1 class="mb-0">Reset Password</h1>
      </div>
      <div class="card-body">
        <ResetPasswordForm/>
      </div>
    </div>
  </div>
</template>

<script>
import ResetPasswordForm from './ResetPassword';

export default {
  name: 'ResetPasswordPage',
  components: {
    ResetPasswordForm,
  },
};
</script>
