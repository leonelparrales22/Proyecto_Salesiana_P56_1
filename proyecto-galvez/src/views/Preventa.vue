<template>
  <div class="page-wrapper">
    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <form>
                <div class="form-body">
                  <h3 class="box-title m-t-40 tabla-titulo">Ingreso de Datos Factura</h3>
                  <hr />
                  <!--/row-->
                  <div class="row">
                    <!--/span-->
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Clientes</label>
                        <select class="form-control custom-select" v-model="cliente_seleccionado">
                          <option
                            v-for="cliente in clientes"
                            :key="cliente.cedula_cliente"
                            v-bind:value="cliente.cedula_cliente"
                          >{{cliente.apellido_cliente}} {{cliente.nombre_cliente}}</option>
                        </select>

                        <br />
                        <!--/Muestra de que se está guardando el valor del select en v-model-->
                        <span>Seleccionado: {{ cliente_seleccionado }}</span>
                      </div>
                    </div>
                    <!-- <div v-if="!validaciones_ok" class="col-md-6">{{mensaje_error}}</div> -->

                    <div class="alert" style="height:40px; text-align:center; line-height: 5px;" v-if="!validaciones_ok">
                      <!-- <span
                        style="line-height: 5px"
                        class="closebtn"
                        onclick="this.parentElement.style.display='none';"
                      >&times;</span> -->
                      {{mensaje_error}}.
                    </div>




                    <!--/span-->
                  </div>
                  <div class="row">
                    <!--/span-->
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Celulares</label>
                        <select
                          class="form-control custom-select"
                          v-model="array_celulares[0].celular"
                        >
                          <option
                            v-for="celular in celulares"
                            :key="celular.id_celular"
                            v-bind:value="celular"
                          >{{ celular.nombre_celular }}</option>
                        </select>
                        <br />
                        <span>Precio: {{ array_celulares[0].celular.precio_celular | moneda}} Stock: {{ array_celulares[0].celular.stock_celular }}</span>
                        <!-- V-IF y V-FOR -->
                        <div v-for="n in cajas_de_celulares" :key="n">
                          <select
                            class="form-control custom-select"
                            v-model="array_celulares[n].celular"
                          >
                            <option>--Seleccione un celular--</option>
                            <option
                              v-for="celular in celulares"
                              :key="celular.id_celular"
                              v-bind:value="celular"
                            >{{ celular.nombre_celular }}</option>
                          </select>
                          <br />
                          <span>Precio: {{ array_celulares[n].celular.precio_celular | moneda}} Stock: {{ array_celulares[n].celular.stock_celular }}</span>
                          <!-- FIN V-IF y V-FOR -->
                        </div>
                      </div>
                    </div>
                    <!--/span-->
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Cantidad</label>
                        <input
                          type="text"
                          class="form-control"
                          v-model="array_celulares[0].cantidad"
                        />
                        <br />
                        <span>Cantidad escrita: {{ array_celulares[0].cantidad }}</span>
                        <div v-for="n in cajas_de_celulares" :key="n">
                          <input
                            type="number"
                            class="form-control"
                            v-model="array_celulares[n].cantidad"
                          />
                          <br />
                          <span>Cantidad escrita: {{ array_celulares[n].cantidad }}</span>
                        </div>
                      </div>

                      <button type="button" class="btn btn-inverse" v-on:click="masCelulares">
                        <i class="fa fa-check"></i> Añadir otro celular
                      </button>&nbsp;
                      <button
                        type="button"
                        v-if="cajas_de_celulares>=1"
                        class="btn btn-danger"
                        v-on:click="menosCelulares"
                      >
                        <i class="fa fa-times"></i> Quitar un celular
                      </button>
                    </div>
                  </div>
                  <br />
                  <br />
                  <center>
                    <button type="button" class="btn btn-success" v-on:click="aplastarBoton()">
                      <i class="fa fa-check"></i> Realizar venta
                    </button>
                  </center>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { Global } from "../Global";

export default {
  name: "Preventa",
  components: {},
  mounted() {
    this.getClientes();
    this.getCelulares();
  },
  updated() {},
  watch: {
    $route() {
      this.rest = Global.url + "clientes";
      this.rest1 = Global.url + "celulares";
      this.getClientes();
      this.getCelulares();
    },
  },
  data() {
    return {
      mensaje_error: "kk",
      validaciones_ok: true,
      array_celulares: [
        {
          celular: {},
          cantidad: "",
        },
      ],
      cajas_de_celulares: 0,
      rest: Global.url + "clientes",
      rest1: Global.url + "celulares",
      clientes: [],
      celulares: [],
      fecha: "",
      total: 0,
      cliente_seleccionado: "",
      selected2: "",
      cantidad: "",
      cliente: "",
      celu: [],

      venta: {
        cedula_cli: "",
        cedula_us: "",
      },

      detalle: {
        id_cel: "",
        cant: "",
      },

      factura: {
        subt: "",
        descu: "",
        iv: "",
        tot: "",
      },
    };
  },
  methods: {
    masCelulares() {
      this.cajas_de_celulares += 1;
      this.array_celulares.push({
        celular: "",
        cantidad: "",
      });
    },
    menosCelulares() {
      this.cajas_de_celulares -= 1;
      this.array_celulares.splice(-1, 1);
      this.validaciones_ok = true;
      if (!this.cliente_seleccionado) {
        this.validaciones_ok = false;
      } else {
        this.array_celulares.forEach((element) => {
          if (!element.celular || !element.cantidad) {
            this.validaciones_ok = false;
            return;
          }
        });
      }
    },
    getClientes() {
      axios
        .get(this.rest)
        .then((data) => {
          this.clientes = data.data.result;
          this.total = data.data.total;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    getCelulares() {
      axios
        .get(this.rest1)
        .then((data) => {
          this.celulares = data.data.result;
        })
        .catch((err) => {
          console.error(err);
        });
    },

    aplastarBoton() {
      console.log(this.array_celulares);
      this.validaciones_ok = true;
      if (!this.cliente_seleccionado) {
        this.mensaje_error = "Selecccione un cliente";
        this.validaciones_ok = false;
      } else {
        this.array_celulares.forEach((element) => {
          if (!element.celular || !element.cantidad) {
            this.mensaje_error = "Rellene todos los campos en celulares";
            this.validaciones_ok = false;
            return;
          }
          if (element.celular.stock_celular < element.cantidad) {
            this.mensaje_error =
              "No puede adquirir más que el stock disponible";
            this.validaciones_ok = false;
            return;
          }
        });
      }

      for (let index_1 = 0; index_1 < this.array_celulares.length; index_1++) {
        const element_1 = this.array_celulares[index_1];
        for (
          let index_2 = 0;
          index_2 < this.array_celulares.length;
          index_2++
        ) {
          const element_2 = this.array_celulares[index_2];
          if (index_1 === index_2) {
            break;
          }
          if (
            element_1.celular.nombre_celular ===
            element_2.celular.nombre_celular
          ) {
            this.mensaje_error =
              "No repita el mismo celular en los casilleros";
            this.validaciones_ok = false;
            break;
          }
        }
      }

      if (this.validaciones_ok) {
        axios
          .post(Global.url + "insertar-venta", {
            array_ventas: this.array_celulares,
            cedula_cliente: this.cliente_seleccionado,
            cedula_usuario: this.$parent.cedula,
          })
          .then((data) => {
            console.log("Este es el codigo: ", data.data.codigo_venta);
            this.$router.push({
              name: "factura",
              params: { id_factura: data.data.codigo_venta },
            });
          })
          .catch((err) => {
            console.error(err);
          });
      }
    },

    obtenerData() {
      this.fecha = new Date();
      this.cliente = this.selected1;
      this.celu = this.celu + this.selected2;
    },
  },
};
</script>
