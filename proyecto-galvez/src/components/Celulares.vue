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
                    <!-- <div class="table-title">
                      <div class="row">
                        <div class="col-sm-6">
                          <h2>
                            Manage
                            <b>Employees</b>
                          </h2>
                        </div>
                        <div class="col-sm-6">
                          <a href="#deleteEmployeeModal" class="btn btn-danger" data-toggle="modal">
                            <i class="material-icons">&#xE15C;</i>
                            <span>Delete</span>
                          </a>
                        </div>
                      </div>
                    </div>-->
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
                              href="#editEmployeeModal"
                              class="edit"
                              data-toggle="modal"
                              data-book-id="LEONELPAPIPARRALES"
                              @click="editar_celular(celular.id_celular)"
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
              <!-- :class="{ in: modalShown }" -->
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
                          <input
                            type="text"
                            class="form-control"
                            v-model="celular.modelo"
                            name="nombre_celular"
                          />
                          <div
                            v-if="submitted && !$v.celular.modelo.required"
                          >Este campo es requerido</div>
                        </div>
                        <div class="form-group">
                          <label>Marca</label>
                          <input
                            type="text"
                            class="form-control"
                            v-model="celular.marca"
                            name="marca_celular"
                          />
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
                            name="stock_celular"
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
                            name="precio_celular"
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
                    <form>
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
                          <label>Name</label>
                          <input type="text" class="form-control" required />
                        </div>
                        <div class="form-group">
                          <label>Email</label>
                          <input type="email" class="form-control" required />
                        </div>
                        <div class="form-group">
                          <label>Address</label>
                          <textarea class="form-control" required></textarea>
                        </div>
                        <div class="form-group">
                          <label>Phone</label>
                          <input type="text" class="form-control" required />
                        </div>
                      </div>
                      <div class="modal-footer">
                        <input
                          type="button"
                          class="btn btn-default"
                          data-dismiss="modal"
                          value="Cancel"
                        />
                        <input type="submit" class="btn btn-info" value="Save" />
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

<script>
import axios from "axios";
import FooterComponent from "./FooterComponent.vue";
import { required, minLength, between } from "vuelidate/lib/validators";
import $ from "jquery";
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
    console.log("kk");
    $("#editEmployeeModal").on("show.bs.modal", function(e) {
      //get data-id attribute of the clicked element
      var bookId = $(e.relatedTarget).data("book-id");
      console.log("OE", bookId);
      //populate the textbox
      $(e.currentTarget)
        .find('input[name="bookId"]')
        .val(bookId);
    });
    $(document).ready(function() {
      $("#editEmployeeModal").on("show.bs.modal", function() {
        alert("Hello World!");
      });
    });
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
      editar:{
        modelo: "",
        marca: "",
        stock: "",
        precio: ""
      },
      modalShown: false
    };
  },
  methods: {
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
    editar_celular(id) {
      console.log("dddjd", id);
    }
  }
};
</script>
