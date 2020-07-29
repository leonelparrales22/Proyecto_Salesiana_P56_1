<template>
  <div id="main-wrapper">
    <HeaderComponent />
    <BarraLateral />
    <div class="page-wrapper">
      <div class="container-fluid">
        <center>
          <!-- <h2 class="bienvenido text-themecolor">Bienvenido</h2> -->
          <h2 class="bienvenido">Bienvenido</h2>
        </center>
        <center class="m-t-30">
          <img src="../assets/img/cajero.jpg" class="img-circle" width="300" />
          <br />
          <br />
          <h4 class="card-title m-t-10 subtitulo">Cajero: {{this.$parent.cedula}}</h4>
        </center>
        <div class="right-sidebar">
          <div class="slimscrollright">
            <div class="rpanel-title">
              Service Panel
              <span>
                <i class="ti-close right-side-toggle"></i>
              </span>
            </div>
            <div class="r-panel-body">
              <ul id="themecolors" class="m-t-20">
                <li>
                  <b>With Light sidebar</b>
                </li>
                <li>
                  <a href="javascript:void(0)" data-theme="default" class="default-theme">1</a>
                </li>
                <li>
                  <a href="javascript:void(0)" data-theme="green" class="green-theme">2</a>
                </li>
                <li>
                  <a href="javascript:void(0)" data-theme="red" class="red-theme">3</a>
                </li>
                <li>
                  <a href="javascript:void(0)" data-theme="blue" class="blue-theme">4</a>
                </li>
                <li>
                  <a href="javascript:void(0)" data-theme="purple" class="purple-theme">5</a>
                </li>
                <li>
                  <a href="javascript:void(0)" data-theme="megna" class="megna-theme">6</a>
                </li>
                <li class="d-block m-t-30">
                  <b>With Dark sidebar</b>
                </li>
                <li>
                  <a
                    href="javascript:void(0)"
                    data-theme="default-dark"
                    class="default-dark-theme working"
                  >7</a>
                </li>
                <li>
                  <a href="javascript:void(0)" data-theme="green-dark" class="green-dark-theme">8</a>
                </li>
                <li>
                  <a href="javascript:void(0)" data-theme="red-dark" class="red-dark-theme">9</a>
                </li>
                <li>
                  <a href="javascript:void(0)" data-theme="blue-dark" class="blue-dark-theme">10</a>
                </li>
                <li>
                  <a href="javascript:void(0)" data-theme="purple-dark" class="purple-dark-theme">11</a>
                </li>
                <li>
                  <a href="javascript:void(0)" data-theme="megna-dark" class="megna-dark-theme">12</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <br />
        <br />
        <FooterComponent />
      </div>
    </div>
  </div>
</template>

<script>
import FooterComponent from "../components/FooterComponent.vue";
import HeaderComponent from "../components/HeaderComponent.vue";
import BarraLateral from "../components/BarraLateral.vue";
export default {
  name: "BienvenidoCajero",
  components: {
    FooterComponent,
    HeaderComponent,
    BarraLateral
  }
};
</script>
