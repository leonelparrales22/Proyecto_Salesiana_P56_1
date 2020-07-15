<template>
  <div id="main-wrapper">
    Inicia Sesion
    <Login />
  </div>
</template>

<script>
import Login from "./components/Login.vue";

export default {
  name: "Login",
  components: {
    Login,
  },
};
</script>

<style>
@import "./assets/css/bootstrap.min.css";
@import "./assets/css/style.css";
@import "./assets/css/blue-dark.css";
</style>
