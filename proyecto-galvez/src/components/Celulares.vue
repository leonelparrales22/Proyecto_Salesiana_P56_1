<template>
  <div class="page-wrapper">
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
                          <td>{{celular.nombre_celular}}</td>
                          <td>{{celular.marca_celular}}</td>
                          <td>{{celular.stock_celular}}</td>
                          <td>{{celular.precio_celular | moneda}}</td>
                          <td class="centrar-horizontal">
                            <a href="#editEmployeeModal" class="edit" data-toggle="modal">
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
                        <b>{{celulares.length}}</b> de
                        <b>{{total}}</b> registros
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
                          active: n === pagenow
                        }"
                        >
                          <router-link
                            :to="{ name: 'celulares', params: { pagenow: n }}"
                            class="page-link"
                          >{{n}}</router-link>
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
                    <form>
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
                          <input type="text" class="form-control" required />
                        </div>
                        <div class="form-group">
                          <label>Marca</label>
                          <input type="email" class="form-control" required />
                        </div>
                        <div class="form-group">
                          <label>Stock</label>
                          <textarea class="form-control" required></textarea>
                        </div>
                        <div class="form-group">
                          <label>Precio</label>
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
                        <input type="submit" class="btn btn-success" value="Add" />
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
export default {
  name: "Celulares",
  components: {
    FooterComponent
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
      this.rest = "http://localhost:3100/todos-celulares";
      this.pagenow = this.$route.params.pagenow;
      if (this.pagenow != null) {
        if (this.pagenow > 1) {
          this.rest += `?desde=${(this.pagenow - 1) * 7 + 1}`;
        } else {
          this.rest += `?desde=0`;
        }
      }
      this.getCelulares();
    }
  },
  data() {
    return {
      rest: "http://localhost:3100/todos-celulares",
      pagenow: null,
      celulares: [],
      paginado: 0,
      total: 0
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
    }
  }
};
</script>
