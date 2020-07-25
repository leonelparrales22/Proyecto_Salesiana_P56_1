<template>
  <aside class="left-sidebar">
    <!-- Sidebar scroll-->
    <div class="scroll-sidebar">
      <!-- Sidebar navigation-->
      <nav class="sidebar-nav">
        <ul id="sidebarnav">
          <li class="nav-devider"></li>
          <li class="nav-small-cap">Acciones</li>
          <li :class="{'active': subIsActive('/administrador/usuarios')}">
            <router-link
              class="has-arrow waves-effect waves-dark"
              :to="{ name: 'usuarios', params: { pagenow: 1 } }"
              aria-expanded="false"
            >
              <i class="mdi mdi-camera-front-variant"></i>
              <span class="hide-menu">Usuarios</span>
            </router-link>
            <ul aria-expanded="false" class="collapse"></ul>
          </li>
        </ul>
      </nav>
      <!-- End Sidebar navigation -->
    </div>
    <!-- End Sidebar scroll-->
  </aside>
</template>

<style>
</style>

<script>
export default {
  name: "BarraLateralAdministrador",
  methods: {
    subIsActive(input) {
      this.validar = true;

      const paths = Array.isArray(input) ? input : [input];

      return paths.some((path) => {
        return this.$route.path.indexOf(path) === 0; // current path starts with this path string
      });
    },
  },
};
</script>
