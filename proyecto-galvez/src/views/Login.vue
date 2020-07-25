<template>
  <div>
    <!-- ============================================================== -->
    <!-- Preloader - style you can find in spinners.css -->
    <!-- ============================================================== -->
    <!-- <div class="preloader">
      <div class="loader">
        <div class="loader__figure"></div>
        <p class="loader__label">Admin Pro</p>
      </div>
    </div>-->
    <!-- ============================================================== -->
    <!-- Main wrapper - style you can find in pages.scss -->
    <!-- ============================================================== -->
    <section id="wrapper" class="login-register login-sidebar fondo">
      <div class="login-box card">
        <div class="card-body">
          <form class="form-horizontal form-material" @submit.prevent="login()">
            <a href="javascript:void(0)" class="text-center db">
              <img src="../assets/img/logo-icon.png" alt="Home" style="width: 50px;" />
              <br />
              <img src="../assets/img/logo-text.png" alt="Home" style="width: 150px;" />
            </a>
            <br />
            <br />
            <div class="form-group m-t-40">
              <div class="col-xs-12">
                <input
                  name="cedula"
                  v-model="usuario.cedula"
                  class="form-control"
                  type="text"
                  placeholder="Cédula"
                  v-on:blur="appear_alert_cedula()"
                />
              </div>
            </div>
            <div class="alert" v-if="submitted_1 && !$v.usuario.cedula.required">
              <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
              <label>Cédula requerida</label>
            </div>
            <div
              class="alert"
              v-if="submitted_1 && $v.usuario.cedula.required && !$v.usuario.cedula.minLength || submitted_1 && $v.usuario.cedula.required && !$v.usuario.cedula.maxLength "
            >
              <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
              <label>Cédula debe tener 10 digitos</label>
            </div>
            <br />
            <div class="form-group">
              <div class="col-xs-12">
                <input
                  name="password"
                  class="form-control"
                  type="password"
                  placeholder="Contraseña"
                  v-on:blur="appear_alert_contrasenia()"
                  v-model="usuario.contrasenia"
                />
              </div>
            </div>
            <div class="alert" v-if="submitted_2 && !$v.usuario.contrasenia.required">
              <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
              <label>Contraseña requerida</label>
            </div>
            <!-- <div class="form-group row">
                        <div class="col-md-12">
                            <div class="checkbox checkbox-primary pull-left p-t-0">
                                <input id="checkbox-signup" type="checkbox" class="filled-in chk-col-light-blue">
                                <label for="checkbox-signup"> Remember me </label>
                            </div>
                            <a href="javascript:void(0)" id="to-recover" class="text-dark pull-right"><i class="fa fa-lock m-r-5"></i> Forgot pwd?</a> </div>
            </div>-->
            <br />
            <div class="form-group text-center m-t-20">
              <div class="col-xs-12">
                <button
                  id="boton"
                  class="btn btn-info btn-lg btn-block text-uppercase btn-rounded"
                  type="submit"
                >INICIAR SESIÓN</button>
              </div>
            </div>
            <div class="row">
              <!-- <div class="col-xs-12 col-sm-12 col-md-12 m-t-10 text-center">
                            <div class="social"><a href="javascript:void(0)" class="btn  btn-facebook" data-toggle="tooltip" title="Login with Facebook"> <i aria-hidden="true" class="fa fa-facebook"></i> </a> <a href="javascript:void(0)" class="btn btn-googleplus" data-toggle="tooltip" title="Login with Google"> <i aria-hidden="true" class="fa fa-google-plus"></i> </a> </div>
              </div>-->
            </div>
            <div class="form-group m-b-0">
              <!-- <div class="col-sm-12 text-center">
                            Don't have an account? <a href="pages-register2.html" class="text-primary m-l-5"><b>Sign Up</b></a>
              </div>-->
            </div>
          </form>
          <div class="alert" v-if="no_se_encontro_usuario">
            <span
              id="usuario_no_encontrado"
              class="closebtn"
              onclick="this.parentElement.style.display='none';"
            >&times;</span>
            Cédula o Contraseña inválida.
          </div>
        </div>
      </div>
    </section>
    <!-- Hola Mundo 
    <router-link class="has-arrow waves-effect waves-dark" to="/preventa" aria-expanded="false">
      <i class="mdi mdi-cart"></i>
      <span class="hide-menu">Ventas</span>
    </router-link>-->
  </div>
</template>

<style>
@import "../assets/css/login-register-lock.css";
</style>

<script>
import axios from "axios";
import { required, minLength, maxLength } from "vuelidate/lib/validators";
// import Vue from "vue";
// import VueRouter from "vue-router";
// Vue.use(VueRouter);

export default {
  name: "Login",
  data() {
    return {
      submitted_1: false,
      submitted_2: false,
      no_se_encontro_usuario: false,
      usuario: {
        cedula: "",
        contrasenia: "",
      },
      result: [],
    };
  },
  methods: {
    appear_alert_cedula() {
      this.submitted_1 = true;
    },
    appear_alert_contrasenia() {
      this.submitted_2 = true;
    },
    appear_no_se_encontro_usuario() {
      this.no_se_encontro_usuario = !this.no_se_encontro_usuario;
    },
    login() {
      this.submitted_1 = true;
      this.submitted_2 = true;

      this.$v.$touch();
      if (this.$v.$invalid) {
        console.log("ERRROR", this.$v);
        return false;
      }
      axios
        .get("http://localhost:3100/login", {
          params: {
            cedula_usuario: this.usuario.cedula,
            contrasenia: this.usuario.contrasenia,
          },
        })
        .then((data) => {
          this.result = data.data.result;
          if (this.result.length > 0) {
            console.log(this.result[0].cedula_usuario);
            console.log(this.result[0].contrasenia);
            console.log(this.result[0].rol);
            if (this.result[0].rol == "ADMIN") {
              this.$router.push("/administrador/");
            } else {
              this.$router.push("/contenedor/");
            }
          } else {
            console.log("No se encontro usuario");
            this.appear_no_se_encontro_usuario();
            setTimeout(() => {
              this.appear_no_se_encontro_usuario();
            }, 1200);
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  validations: {
    submitted_1: false,
    submitted_2: false,
    usuario: {
      cedula: {
        required,
        minLength: minLength(10),
        maxLength: maxLength(10),
      },
      contrasenia: {
        required,
      },
    },
  },
};
</script>