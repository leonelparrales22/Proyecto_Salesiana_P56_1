<template>
  <aside class="left-sidebar">
    <!-- Sidebar scroll-->
    <div class="scroll-sidebar">
      <!-- Sidebar navigation-->
      <nav class="sidebar-nav">
        <ul id="sidebarnav">
          <li class="nav-devider"></li>
          <li class="nav-small-cap">Acciones</li>
          <li active-class="active">
            <router-link
              class="has-arrow waves-effect waves-dark"
              to="/preventa"
              aria-expanded="false"
            >
              <i class="mdi mdi-cart"></i>
              <span class="hide-menu">Ventas</span>
            </router-link>
            <ul aria-expanded="false" class="collapse"></ul>
          </li>
          <li>
            <router-link
              class="has-arrow waves-effect waves-dark"
              to="/cliente"
              aria-expanded="false"
            >
              <i class="mdi mdi-account-circle"></i>
              <span class="hide-menu">Clientes</span>
            </router-link>
            <ul aria-expanded="false" class="collapse"></ul>
          </li>
          <li>
            <router-link
              class="has-arrow waves-effect waves-dark"
              :to="{ name: 'celulares', params: { pagenow: 1 } }"
              aria-expanded="false"
            >
              <i class="mdi mdi-camera-front-variant"></i>
              <span class="hide-menu">Celulares</span>
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

<script>
export default {
  name: "BarraLateral"
};
</script>
