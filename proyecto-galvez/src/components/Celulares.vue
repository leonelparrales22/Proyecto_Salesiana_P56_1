<template>
  <div class="page-wrapper" id="wrapper">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <div class="card">
            <div class="card-body">
              <div class="row">
                <div class="col-sm-6">
                  <h4 class="card-title tabla-titulo">Registro Celulares</h4>
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
                    <table class="table table-striped table-hover" v-if="celulares">
                      <thead>
                        <tr>
                          <th>Modelo</th>
                          <th>Marca</th>
                          <th>Stock</th>
                          <th>Precio</th>
                          <th>Editar</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="celular in celulares" :key="celular.id_celular">
                          <td>{{ celular.nombre_celular }}</td>
                          <td>{{ celular.marca_celular }}</td>
                          <td>{{ celular.stock_celular }}</td>
                          <td>{{ celular.precio_celular | moneda }}</td>
                          <td class="centrar-horizontal">
                            <a
                              id="boton_lapiz"
                              href="#editEmployeeModal"
                              class="edit"
                              data-toggle="modal"
                              data-book-id="LEONELPAPIPARRALES"
                              @click="editar_celular(celular.id_celular, celular.nombre_celular, celular.marca_celular, celular.stock_celular, celular.precio_celular )"
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
                        <b>{{ celulares.length }}</b> de
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
                        <h4 class="modal-title">Añadir Celular</h4>
                        <button
                          type="button"
                          class="close"
                          data-dismiss="modal"
                          aria-hidden="true"
                        >&times;</button>
                      </div>
                      <div class="modal-body">
                        <div class="form-group">
                          <label>Modelo</label>
                          <input type="text" class="form-control" v-model="celular.modelo" />
                          <div
                            v-if="submitted && !$v.celular.modelo.required"
                          >Este campo es requerido</div>
                        </div>
                        <div class="form-group">
                          <label>Marca</label>
                          <input type="text" class="form-control" v-model="celular.marca" />
                          <div
                            v-if="submitted && !$v.celular.marca.required"
                          >Este campo es requerido</div>
                        </div>
                        <div class="form-group">
                          <label>Stock</label>
                          <input
                            type="number"
                            class="form-control"
                            v-model="celular.stock"
                            min="1"
                            max="100"
                          />
                          <div
                            v-if="submitted && !$v.celular.stock.required"
                          >Este campo es requerido</div>
                          <div
                            v-if="submitted && $v.celular.stock.required && !$v.celular.stock.between"
                          >Valores entre 1 y 100</div>
                        </div>
                        <div class="form-group">
                          <label>Precio</label>
                          <input
                            type="number"
                            class="form-control"
                            v-model="celular.precio"
                            min="1"
                            max="5000"
                          />
                          <div
                            v-if="submitted && !$v.celular.precio.required"
                          >Este campo es requerido</div>
                        </div>
                        <div
                          v-if="submitted && $v.celular.precio.required && !$v.celular.precio.between"
                        >Valores entre 1 y 5000</div>
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
                          <label>Modelo</label>
                          <input type="text" class="form-control" v-model="editar.modelo" />
                          <div v-if="!$v.editar.modelo.required">Este campo es requerido</div>
                        </div>
                        <div class="form-group">
                          <label>Marca</label>
                          <input type="text" class="form-control" v-model="editar.marca" />
                          <div v-if="!$v.editar.marca.required">Este campo es requerido</div>
                        </div>
                        <div class="form-group">
                          <label>Stock</label>
                          <input
                            type="number"
                            class="form-control"
                            v-model="editar.stock"
                            min="1"
                            max="100"
                          />
                          <div v-if="!$v.editar.stock.required">Este campo es requerido</div>
                          <div
                            v-if="$v.editar.stock.required && !$v.editar.stock.between"
                          >Valores entre 1 y 100</div>
                        </div>
                        <div class="form-group">
                          <label>Precio</label>
                          <input
                            type="number"
                            class="form-control"
                            v-model="editar.precio"
                            min="1"
                            max="5000"
                          />
                          <div v-if="!$v.editar.precio.required">Este campo es requerido</div>
                          <div
                            v-if="$v.editar.precio.required && !$v.editar.precio.between"
                          >Valores entre 1 y 5000</div>
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
    <FooterComponent />
  </div>
</template>
<style>
@import "./../assets/css/bootstrap.min.css";
</style>

<script>
// import $ from "jquery";
import axios from "axios";
import FooterComponent from "./FooterComponent.vue";
import { required, minLength, between } from "vuelidate/lib/validators";
export default {
  name: "Celulares",
  components: {
    FooterComponent
  },
  validations: {
    submitted: false,
    celular: {
      modelo: {
        required,
        minLenght: minLength(1)
      },
      marca: {
        required,
        minLenght: minLength(1)
      },
      stock: {
        required,
        minLenght: minLength(1),
        between: between(1, 100)
      },
      precio: {
        required,
        minLenght: minLength(1),
        between: between(1, 5000)
      }
    },
    editar: {
      modelo: {
        required,
        minLenght: minLength(1)
      },
      marca: {
        required,
        minLenght: minLength(1)
      },
      stock: {
        required,
        minLenght: minLength(1),
        between: between(1, 100)
      },
      precio: {
        required,
        minLenght: minLength(1),
        between: between(1, 5000)
      }
    }
  },
  updated() {
    console.log("CAMBIO");
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
    }
  },
  data() {
    return {
      rest: "http://localhost:3100/todos-celulares",
      // Paginacion
      pagenow: null,
      celulares: [],
      paginado: 0,
      total: 0,
      // Formulario
      submitted: false,
      celular: {
        modelo: "",
        marca: "",
        stock: "",
        precio: ""
      },
      // Editar
      editar: {
        id: "",
        modelo: "",
        marca: "",
        stock: "",
        precio: ""
      },
      butt_actualizar: false
    };
  },
  methods: {
    openModel() {
      this.myModel = true;
    },
    getCelulares() {
      axios
        .get(this.rest)
        .then(data => {
          this.celulares = data.data.result;
          this.total = data.data.total;
          this.paginado = Math.ceil(this.total / 7);
        })
        .catch(err => {
          console.error(err);
        });
    },
    actualizar_paginado() {
      this.rest = "http://localhost:3100/todos-celulares";
      this.pagenow = this.$route.params.pagenow;
      if (this.pagenow != null) {
        if (this.pagenow > 1) {
          this.rest += `?desde=${(this.pagenow - 1) * 7 + 1}`;
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
        .post("http://localhost:3100/insertar-celular", {
          nombre_celular: this.celular.modelo,
          marca_celular: this.celular.marca,
          stock_celular: this.celular.stock,
          precio_celular: this.celular.precio
        })
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error.response);
        });
      this.actualizar_paginado();
      this.getCelulares();
    },
    mostrarCelular() {
      this.submitted = true;
      this.$v.$touch();
      if (this.$v.$invalid) {
        return false;
      }
      this.save();
    },
    editar_celular(id, nombre, marca, stock, precio) {
      this.editar.id = id;
      this.editar.modelo = nombre;
      this.editar.marca = marca;
      this.editar.stock = stock;
      this.editar.precio = precio;
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
        .put("http://localhost:3100/editar-celular", {
          id_celular: this.editar.id,
          nombre_celular: this.editar.modelo,
          marca_celular: this.editar.marca,
          stock_celular: this.editar.stock,
          precio_celular: this.editar.precio
        })
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error.response);
        });
      this.actualizar_paginado();
      this.getCelulares();
      this.butt_actualizar = true;
      return;
    }
  }
};
</script>
