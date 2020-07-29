<template>
  <!-- ============================================================== -->
  <!-- Topbar header - style you can find in pages.scss -->
  <!-- ============================================================== -->
  <header class="topbar">
    <nav class="navbar top-navbar navbar-expand-md navbar-light">
      <!-- ============================================================== -->
      <!-- Logo -->
      <!-- ============================================================== -->
      <div class="navbar-header">
        <router-link :to="{ name: 'administrador'}" class="navbar-brand">
          <!-- Logo icon -->
          <b>
            <!--You can put here icon as well // <i class="wi wi-sunset"></i> //-->
            <!-- Dark Logo icon -->
            <img src="../assets/img/logo-icon.png" alt="homepage" class="dark-logo" />
            <!-- Light Logo icon -->
            <img src="../assets/img/logo-light-icon.png" alt="homepage" class="light-logo" />
          </b>
          <!--End Logo icon -->
          <!-- Logo text -->
          <span>
            <!-- dark Logo text -->
            <img src="../assets/img/logo-text.png" alt="homepage" class="dark-logo" />
            <!-- Light Logo text -->
            <img src="../assets/img/logo-light-text.png" class="light-logo" alt="homepage" />
          </span>
        </router-link>
      </div>
      <!-- ============================================================== -->
      <!-- End Logo -->
      <!-- ============================================================== -->
      <div class="navbar-collapse">
        <!-- ============================================================== -->
        <!-- toggle and nav items -->
        <!-- ============================================================== -->
        <ul class="navbar-nav mr-auto">
          <!-- This is  -->
          <li class="nav-item">
            <a
              class="nav-link nav-toggler hidden-md-up waves-effect waves-dark"
              href="javascript:void(0)"
            >
              <i class="ti-menu"></i>
            </a>
          </li>
          <li class="nav-item">
            <a
              class="nav-link sidebartoggler hidden-sm-down waves-effect waves-dark"
              href="javascript:void(0)"
            >
              <i class="ti-menu"></i>
            </a>
          </li>
          <li class="nav-item hidden-sm-down"></li>
          <li></li>
          <div class="centrado">
            <a class="btn btn-warning btn-lg">
              <span class="glyphicon glyphicon-log-out"></span>Administrador
            </a>
          </div>
        </ul>

        <router-link to="/login">
          <a href="#" class="btn btn-danger btn-lg">
            <span class="glyphicon glyphicon-log-out"></span> Cerrar Sesión
          </a>
        </router-link>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "HeaderComponentAdministrador",
};
</script>
