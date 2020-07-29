<template>
  <div id="main-wrapper">
    <HeaderComponentAdministrador />
    <BarraLateralAdministrador />
    <router-view />
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponentAdministrador from "../components/HeaderComponentAdministrador";
import BarraLateralAdministrador from "../components/BarraLateralAdministrador";
import FooterComponent from "../components/FooterComponent.vue";

export default {
  name: "Administrador",
  components: {
    HeaderComponentAdministrador,
    BarraLateralAdministrador,
    FooterComponent,
  },
  data() {
    return {
      cedula: this.$route.params.cedula,
    };
  },
  // mounted() {
  //   this.$router.push({
  //     name: "bienvenido",
  //   });
  // },
};
</script>

