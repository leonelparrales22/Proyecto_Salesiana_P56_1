<template>
  <div id="main-wrapper">
    <HeaderComponent />
    <BarraLateral />
    <router-view />
  </div>
</template>

<script>

import HeaderComponent from "../components/HeaderComponent.vue";
import BarraLateral from "../components/BarraLateral.vue";

export default {
  name: "Contenedor",
  components: {
    HeaderComponent,
    BarraLateral
  },
};
</script>

