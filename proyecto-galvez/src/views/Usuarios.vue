<template>
  <div class="page-wrapper" id="wrapper">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <div class="card">
            <div class="card-body">
              <div class="row">
                <div class="col-sm-6">
                  <h4 class="card-title tabla-titulo">Registro Usuarios</h4>
                </div>
                <div class="col-sm-6 alinear-derecha">
                  <a
                    id="boton1"
                    href="#addEmployeeModal"
                    class="btn btn-success alinear-derecha"
                    data-toggle="modal"
                  >
                    <!-- <i class="material-icons">&#xE147;</i> -->
                    <span>Añadir nuevo usuario</span>
                  </a>
                </div>
              </div>

              <hr />
              <!-- INICIO TABLA -->
              <div class="container-xl">
                <div class="table-responsive">
                  <div class="table-wrapper">
                    <table class="table table-striped table-hover" v-if="usuarios">
                      <thead>
                        <tr>
                          <th>Cédula Usuario</th>
                          <th>Rol</th>
                          <th>Editar</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="usuario in usuarios" :key="usuario.cedula_usuario">
                          <td>{{ usuario.cedula_usuario }}</td>
                          <td>{{ usuario.rol }}</td>
                          <td class="centrar-horizontal">
                            <a
                              id="boton_lapiz"
                              href="#editEmployeeModal"
                              class="edit"
                              data-toggle="modal"
                              @click="editar_celular(usuario.cedula_usuario, usuario.rol)"
                            >
                              <div class="hover01">
                                <div>
                                  <figure class="figure">
                                    <img src="../assets/img/edit.png" height="30px" />
                                  </figure>
                                </div>
                              </div>
                            </a>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <div class="clearfix">
                      <div class="hint-text">
                        Mostrando
                        <b>{{ usuarios.length }}</b> de
                        <b>{{ total }}</b> registros
                      </div>
                      <ul class="pagination" v-if="paginado">
                        <li class="page-item disabled">
                          <a href="#">Antes</a>
                        </li>
                        <li
                          v-for="n in paginado"
                          :key="n"
                          class="page-item"
                          :class="{
                            active: n === pagenow,
                          }"
                        >
                          <router-link
                            :to="{ name: 'celulares', params: { pagenow: n } }"
                            class="page-link"
                          >{{ n }}</router-link>
                        </li>
                        <li class="page-item">
                          <a href="#" class="page-link">Después</a>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
              <!--Add Modal HTML -->
              <div id="addEmployeeModal" class="modal fade">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <form @submit.prevent="mostrarCelular()">
                      <div class="modal-header">
                        <h4 class="modal-title">Añadir Usuario</h4>
                        <button
                          type="button"
                          class="close"
                          data-dismiss="modal"
                          aria-hidden="true"
                        >&times;</button>
                      </div>
                      <div class="modal-body">
                        <div class="form-group">
                          <label>Cédula Usuario</label>
                          <input
                            type="number"
                            class="form-control"
                            v-model="usuario.cedula_usuario"
                          />
                          <div
                            v-if="submitted && !$v.usuario.cedula_usuario.required"
                          >Este campo es requerido</div>
                          <div
                            v-if="submitted && $v.usuario.cedula_usuario.required && !$v.usuario.cedula_usuario.minLength || submitted && $v.usuario.cedula_usuario.required && !$v.usuario.cedula_usuario.maxLength"
                          >La cedula debe tener 10 digitos</div>
                        </div>
                        <div class="form-group">
                          <label>Contraseña</label>
                          <input type="password" class="form-control" v-model="usuario.contrasenia" />
                          <div
                            v-if="submitted && !$v.usuario.contrasenia.required"
                          >Este campo es requerido</div>
                        </div>
                        <div class="form-group">
                          <label>Rol</label>
                          <select class="form-control custom-select" v-model="usuario.rol">
                            <option value="ADMIN">ADMIN</option>
                            <option value="CAJERO">CAJERO</option>
                          </select>
                          <div v-if="submitted && !$v.usuario.rol.required">Este campo es requerido</div>
                        </div>
                        <div v-if="usuario_existeste">¡La cédula ingresada ya existe!</div>
                      </div>

                      <div class="modal-footer">
                        <input
                          type="button"
                          class="btn btn-default"
                          data-dismiss="modal"
                          value="Cancelar"
                        />
                        <input type="submit" class="btn btn-success" value="Añadir" />
                      </div>
                    </form>
                  </div>
                </div>
              </div>
              <!-- Edit Modal HTML -->
              <div id="editEmployeeModal" class="modal fade">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <form @submit.prevent="editar_celular_valores()">
                      <div class="modal-header">
                        <h4 class="modal-title">Editar Celular</h4>
                        <button
                          type="button"
                          class="close"
                          data-dismiss="modal"
                          aria-hidden="true"
                        >&times;</button>
                      </div>

                      <div class="modal-body">
                        <div class="form-group">
                          <label>Cédula Usuario</label>
                          <input
                            disabled
                            type="number"
                            class="form-control"
                            v-model="editar.cedula_usuario"
                          />
                          <div
                            v-if="submitted && !$v.editar.cedula_usuario.required"
                          >Este campo es requerido</div>
                          <div
                            v-if="submitted && $v.editar.cedula_usuario.required && !$v.editar.cedula_usuario.minLength || submitted && $v.editar.cedula_usuario.required && !$v.editar.cedula_usuario.maxLength"
                          >La cedula debe tener 10 digitos</div>
                        </div>
                        <div class="form-group">
                          <label>Rol</label>
                          <select class="form-control custom-select" v-model="editar.rol">
                            <option value="ADMIN">ADMIN</option>
                            <option value="CAJERO">CAJERO</option>
                          </select>
                          <div v-if="submitted && !$v.editar.rol.required">Este campo es requerido</div>
                        </div>
                      </div>

                      <div class="modal-footer">
                        <input
                          type="button"
                          class="btn btn-default"
                          data-dismiss="modal"
                          value="Cancelar"
                        />
                        <input type="submit" class="btn btn-info" value="Editar" />
                      </div>
                    </form>
                  </div>
                </div>
              </div>

              <!-- FIN TABLA -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
@import "./../assets/css/bootstrap.min.css";
</style>

<script>
import axios from "axios";
import { required, minLength, maxLength } from "vuelidate/lib/validators";
import { Global } from "../Global";

export default {
  name: "Usuarios",
  components: {},
  validations: {
    submitted: false,
    usuario: {
      cedula_usuario: {
        required,
        minLength: minLength(10),
        maxLength: maxLength(10),
      },
      contrasenia: {
        required,
      },
      rol: {
        required,
      },
    },
    editar: {
      cedula_usuario: {
        required,
        minLength: minLength(10),
        maxLength: maxLength(10),
      },
      rol: {
        required,
      },
    },
  },
  updated() {
    if (this.butt_actualizar) {
      this.actualizar_paginado();
      this.getCelulares();
      this.butt_actualizar = false;
    }
    console.log(this.myModel);
  },
  mounted() {
    this.pagenow = this.$route.params.pagenow;
    if (this.pagenow != null) {
      if (this.pagenow > 1) {
        this.rest += `?desde=${(this.pagenow - 1) * 7 + 1}`;
      } else {
        this.rest += `?desde=0`;
      }
    }
    this.getCelulares();
  },
  watch: {
    $route() {
      this.actualizar_paginado();
      this.getCelulares();
    },
  },
  data() {
    return {
      rest: Global.url + "todos-usuarios",
      // Paginacion
      pagenow: null,
      usuarios: [],
      paginado: 0,
      total: 0,
      // Formulario
      submitted: false,
      usuario: {
        cedula_usuario: "",
        contrasenia: "",
        rol: "",
      },
      usuario_existeste: false,
      // Editar
      editar: {
        contrasenia: "",
        rol: "",
      },
      butt_actualizar: false,
    };
  },
  methods: {
    getCelulares() {
      axios
        .get(this.rest)
        .then((data) => {
          this.usuarios = data.data.result;
          this.total = data.data.total;
          this.paginado = Math.ceil(this.total / 7);
          // this.paginado = 20
        })
        .catch((err) => {
          console.error(err);
        });
    },
    actualizar_paginado() {
      this.rest = Global.url + "todos-usuarios";
      this.pagenow = this.$route.params.pagenow;
      if (this.pagenow != null) {
        if (this.pagenow > 1) {
          this.rest += `?desde=${(this.pagenow - 1) * 7}`;
        } else {
          this.rest += `?desde=0`;
        }
      }
    },
    save() {
      axios
        .post(Global.url + "insertar-usuario", {
          cedula_usuario: this.usuario.cedula_usuario,
          contrasenia: this.usuario.contrasenia,
          rol: this.usuario.rol,
        })
        .then((response) => {
          console.log(response);
          const modal = document.getElementById("addEmployeeModal");
          modal.classList.remove("show");
          modal.setAttribute("aria-hidden", "true");
          modal.setAttribute("style", "display: none");
          const modalBackdrops = document.getElementsByClassName(
            "modal-backdrop"
          );
          document.body.removeChild(modalBackdrops[0]);
          document.getElementById("addEmployeeModal").click();
          document.getElementById("wrapper").click();
          document.getElementById("boton1").blur();
          document.getElementById("wrapper").click();
          var body = document.body;
          body.classList.remove("modal-open");
          this.usuario.cedula_usuario = "";
          this.usuario.contrasenia = "";
          this.usuario.rol = "";
          this.submitted = false;
          this.actualizar_paginado();
          this.getCelulares();
        })
        .catch((error) => {
          console.log(error.response);
          this.usuario_existeste = true;
        });
    },
    mostrarCelular() {
      this.submitted = true;
      this.$v.usuario.$touch();
      if (this.$v.usuario.$invalid) {
        return false;
      }
      this.save();
    },
    editar_celular(cedula_usuario, rol) {
      this.editar.cedula_usuario = cedula_usuario;
      this.editar.rol = rol;
    },
    editar_celular_valores() {
      this.$v.editar.$touch();
      if (this.$v.editar.$invalid) {
        console.log("ERRROR", this.$v.editar);
        return false;
      }
      const modal = document.getElementById("editEmployeeModal");
      modal.classList.remove("show");
      modal.setAttribute("aria-hidden", "true");
      modal.setAttribute("style", "display: none");
      const modalBackdrops = document.getElementsByClassName("modal-backdrop");
      document.body.removeChild(modalBackdrops[0]);
      var body = document.body;
      body.classList.remove("modal-open");
      axios
        .put(Global.url + "editar-usuario", {
          cedula_usuario: this.editar.cedula_usuario,
          rol: this.editar.rol,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error.response);
        });
      this.actualizar_paginado();
      this.getCelulares();
      this.butt_actualizar = true;
      this.editar.rol = "";
      return;
    },
  },
};
</script>
