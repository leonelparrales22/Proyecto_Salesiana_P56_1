<template>
  <div class="page-wrapper" id="wrapper">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <div class="card">
            <div class="card-body">
              <div class="row">
                <div class="col-sm-6">
                  <h4 class="card-title tabla-titulo">Registro Clientes</h4>
                </div>
                <div class="col-sm-6 alinear-derecha">
                  <a
                    id="boton1"
                    href="#addEmployeeModal"
                    class="btn btn-success alinear-derecha"
                    data-toggle="modal"
                  >
                    <!-- <i class="material-icons">&#xE147;</i> -->
                    <span>Añadir nuevo celular</span>
                  </a>
                </div>
              </div>

              <hr />
              <!-- INICIO TABLA -->
              <div class="container-xl">
                <div class="table-responsive">
                  <div class="table-wrapper">
                    <table class="table table-striped table-hover" v-if="clientes">
                      <thead>
                        <tr>
                          <th>Nombre</th>
                          <th>Cedula</th>
                          <th>Direccion</th>
                          <th>Editar</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="cliente in clientes" :key="cliente.cedula_cliente">
                          <td>{{cliente.apellido_cliente}} {{"\t"}} {{"\t"}} {{ cliente.nombre_cliente }}</td>
                          <td>{{ cliente.cedula_cliente }}</td>
                          <td>{{ cliente.direccion_cliente }}</td>

                          <td class="centrar-horizontal">
                            <a
                              id="boton_lapiz"
                              href="#editEmployeeModal"
                              class="edit"
                              data-toggle="modal"
                              data-book-id="LEONELPAPIPARRALES"
                              @click="editar_celular(cliente.cedula_cliente, cliente.nombre_cliente,cliente.apellido_cliente, cliente.direccion_cliente )"
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
                        <b>{{ clientes.length }}</b> de
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
                            :to="{ name: 'clientes', params: { pagenow: n } }"
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
                        <h4 class="modal-title">Añadir Cliente</h4>
                        <button
                          type="button"
                          class="close"
                          data-dismiss="modal"
                          aria-hidden="true"
                        >&times;</button>
                      </div>
                      <div class="modal-body">
                        <div class="form-group">
                          <label>Cedula</label>
                          <input type="number" class="form-control" v-model="cliente.cedula" />
                          <div
                            v-if="submitted && !$v.cliente.cedula.required"
                          >Este campo es requerido</div>
                          <div
                            v-if="submitted && $v.cliente.cedula.required && !$v.cliente.cedula.minLength || submitted && $v.cliente.cedula.required && !$v.cliente.cedula.maxLength"
                          >La cedula debe tener 10 digitos</div>
                        </div>
                        <div class="form-group">
                          <label>Nombre</label>
                          <input type="text" class="form-control" v-model="cliente.nombre" />
                          <div
                            v-if="submitted && !$v.cliente.nombre.required"
                          >Este campo es requerido</div>
                        </div>
                        <div class="form-group">
                          <label>Apellido</label>
                          <input class="form-control" v-model="cliente.apellido" />
                          <div
                            v-if="submitted && !$v.cliente.apellido.required"
                          >Este campo es requerido</div>
                        </div>
                        <div class="form-group">
                          <label>Direccion</label>
                          <input class="form-control" v-model="cliente.direccion" />
                          <div
                            v-if="submitted && !$v.cliente.direccion.required"
                          >Este campo es requerido</div>
                        </div>
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
                        <h4 class="modal-title">Editar Cliente</h4>
                        <button
                          type="button"
                          class="close"
                          data-dismiss="modal"
                          aria-hidden="true"
                        >&times;</button>
                      </div>
                      <div class="modal-body">
                        <div class="form-group">
                          <label>Cedula</label>
                          <input disabled type="text" class="form-control" v-model="editar.cedula" />
                          <div v-if="!$v.editar.cedula.required">Este campo es requerido</div>
                        </div>
                        <div class="form-group">
                          <label>Nombre</label>
                          <input type="text" class="form-control" v-model="editar.nombre" />
                          <div v-if="!$v.editar.nombre.required">Este campo es requerido</div>
                        </div>
                        <div class="form-group">
                          <label>Apellido</label>
                          <input class="form-control" v-model="editar.apellido" />
                          <div v-if="!$v.editar.apellido.required">Este campo es requerido</div>
                        </div>
                        <div class="form-group">
                          <label>Direccion</label>
                          <input type="text" class="form-control" v-model="editar.direccion" />
                          <div v-if="!$v.editar.direccion.required">Este campo es requerido</div>
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
// import $ from "jquery";
import axios from "axios";
import { required, minLength, maxLength } from "vuelidate/lib/validators";
export default {
  name: "Clientes",
  components: {},
  validations: {
    submitted: false,
    cliente: {
      nombre: {
        required,
      },
      apellido: {
        required,
      },
      direccion: {
        required,
      },
      cedula: {
        required,
        minLength: minLength(10),
        maxLength: maxLength(10),
      },
    },
    editar: {
      nombre: {
        required,
      },
      apellido: {
        required,
      },
      direccion: {
        required,
      },
      cedula: {
        required,
        minLength: minLength(10),
        maxLength: maxLength(10),
      },
    },
  },
  updated() {
    if (this.butt_actualizar) {
      this.actualizar_paginado();
      this.getCelulares();
      this.butt_actualizar = false;
    }
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
      rest: "http://localhost:3100/todos-clientes",
      // Paginacion
      pagenow: null,
      clientes: [],
      paginado: 0,
      total: 0,
      // Formulario
      submitted: false,
      cliente: {
        nombre: "",
        apellido: "",
        cedula: "",
        direccion: "",
      },
      // Editar
      editar: {
        nombre: "",
        apellido: "",
        cedula: "",
        direccion: "",
      },
      butt_actualizar: false,
    };
  },
  methods: {
    openModel() {
      this.myModel = true;
    },
    getCelulares() {
      axios
        .get(this.rest)
        .then((data) => {
          this.clientes = data.data.result;
          this.total = data.data.total;
          this.paginado = Math.ceil(this.total / 7);
          // this.paginado = 20
        })
        .catch((err) => {
          console.error(err);
        });
    },
    actualizar_paginado() {
      this.rest = "http://localhost:3100/todos-clientes";
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
      const modal = document.getElementById("addEmployeeModal");
      modal.classList.remove("show");
      modal.setAttribute("aria-hidden", "true");
      modal.setAttribute("style", "display: none");
      const modalBackdrops = document.getElementsByClassName("modal-backdrop");
      document.body.removeChild(modalBackdrops[0]);
      document.getElementById("addEmployeeModal").click();
      document.getElementById("wrapper").click();
      document.getElementById("boton1").blur();
      document.getElementById("wrapper").click();
      var body = document.body;
      body.classList.remove("modal-open");
      axios
        .post("http://localhost:3100/insertar-cliente", {
          nombre_cliente: this.cliente.nombre,
          apellido_cliente: this.cliente.apellido,
          cedula_cliente: this.cliente.cedula,
          direccion_cliente: this.cliente.direccion,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error.response);
        });
      this.actualizar_paginado();
      this.getCelulares();
      this.cliente.nombre = "";
      this.cliente.apellido = "";
      this.cliente.cedula = "";
      this.cliente.direccion = "";
    },
    mostrarCelular() {
      this.submitted = true;
      this.$v.cliente.$touch();
      if (this.$v.cliente.$invalid) {
        console.log(this.$v);
        console.log("error");
        return false;
      }
      this.save();
    },
    editar_celular(cedula, nombre, apellido, direccion) {
      this.editar.cedula = cedula;
      this.editar.nombre = nombre;
      this.editar.apellido = apellido;
      this.editar.direccion = direccion;
    },
    editar_celular_valores() {
      this.$v.editar.$touch();
      if (this.$v.editar.$invalid) {
        console.log("ERRROR", this.$v);
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
        .put("http://localhost:3100/editar-cliente", {
          nombre_cliente: this.editar.nombre,
          apellido_cliente: this.editar.apellido,
          cedula_cliente: this.editar.cedula,
          direccion_cliente: this.editar.direccion,
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
      return;
    },
  },
};
</script>
