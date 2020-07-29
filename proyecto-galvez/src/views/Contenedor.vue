<template>
  <div id="main-wrapper">
    <HeaderComponent />
    <BarraLateral />
    <router-view />
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from "../components/HeaderComponent.vue";
import BarraLateral from "../components/BarraLateral.vue";
import FooterComponent from "../components/FooterComponent.vue";

export default {
  name: "Contenedor",
  components: {
    HeaderComponent,
    BarraLateral,
    FooterComponent,
  },
  data() {
    return {
      cedula: this.$route.params.cedula,
    };
  },
  mounted() {
    this.$router.push({
      name: "bienvenido",
    });
  },
};
</script>

