<template>
  <div id="main-wrapper">
    <!-- <Loading /> -->
    <HeaderComponent />
    <BarraLateral />
    <router-view />
  </div>
</template>

<script>
import HeaderComponent from "./components/HeaderComponent.vue";
import BarraLateral from "./components/BarraLateral.vue";

export default {
  name: "App",
  components: {
    HeaderComponent,
    // Loading,
    BarraLateral,
  },
};
</script>

<style>
@import "./assets/css/bootstrap.min.css";
@import "./assets/css/style.css";
@import "./assets/css/blue-dark.css";
</style>
