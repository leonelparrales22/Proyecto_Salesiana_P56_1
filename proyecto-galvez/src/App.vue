<template>
  <div id="main-wrapper">
    <!-- <Loading /> -->
    <router-view />
  </div>
</template>

<script>

export default {
  name: "App",
  components: {
    // Loading,
  },
};
</script>

<style>
@import "./assets/css/bootstrap.min.css";  
@import "./assets/css/style.css";
@import "./assets/css/blue-dark.css";
@import "./assets/css/efecto-imagen.css";

</style>
