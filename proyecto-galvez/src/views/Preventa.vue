<template>
  <div class="page-wrapper">
    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <form action="#">
                <div class="form-body">
                  <h3 class="box-title m-t-40 tabla-titulo">Ingreso de Datos Factura</h3>
                  <hr />
                  <!--/row-->
                  <div class="row">
                    <!--/span-->
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Clientes</label>
                        <select class="form-control custom-select" v-model="selected1">
                          <option>--Seleccione un cliente--</option>
                          <option
                            v-for="cliente in clientes"
                            :key="cliente.cedula_cliente"
                          >{{cliente.nombre_cliente}} {{cliente.apellido_cliente}}</option>
                        </select>
                        <br>
                        <!--/Muestra de que se está guardando el valor del select en v-model-->
                        <span>Seleccionado: {{ selected1 }}</span>
                      </div>
                    </div>
                    <!--/span-->
                  </div>
                  <div class="row">
                    <!--/span-->
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Celulares</label>
                        <select class="form-control custom-select" v-model="selected2">
                          <option>--Seleccione un celular--</option>
                          <option v-for="celular in celulares" :key="celular.id_celular">
                            {{ celular.nombre_celular }}
                          </option>
                          
                          <!-- <option>Samsung A50</option>
                          <option>Iphone 5S</option>
                          <option>Samsung j6</option> -->
                        </select>
                        <br>
                        <!--/Muestra de que se está guardando el valor del select en v-model-->
                        <span>Seleccionado: {{ selected2 }}</span>
                      </div>
                    </div>
                    <!--/span-->
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Cantidad</label>
                        <input type="text" class="form-control" v-model="cantidad" />
                        <br>
                        <span>Cantidad escrita: {{ cantidad }}</span>
                      </div>
                      <button type="submit" class="btn btn-inverse">
                        <i class="fa fa-check"></i> Añadir otro celular
                      </button>
                    </div>
                  </div>
                  <br />
                  <br />
                  <center>
                    <button type="submit" class="btn btn-success" v-on:click="aplastarBoton()">
                       <!-- <router-link
                            :to="{ name: 'facturas', params: { nombre: selected1 } }"
                          ></router-link>  Revisar más a fondo esta sintaxis,  -->
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
export default {
  name: "Preventa",
  components: {
  },
  mounted() {
    this.getClientes();
    this.getCelulares();
  },
  watch: {
    $route() {
      this.rest = "http://localhost:3100/todos-clientes";
      this.rest1 = "http://localhost:3100/todos-celulares";
      this.getClientes();
      this.getCelulares();
    },
  },
  data() {
    return {
      rest: "http://localhost:3100/todos-clientes",
      rest1: "http://localhost:3100/todos-celulares",
      clientes: [],
      celulares: [],
      fecha: '',
      total: 0,
      selected1: '',
      selected2: '',
      cantidad: '',
      cliente: '',
      celu: [],

      venta :{
        cedula_cli: "",
        cedula_us: ""
      },

      detalle: {
        id_cel:  "",
        cant: ""
      },

      factura: {
        subt: "",
        descu: "",
        iv: "",
        tot: ""
      }

    };
  },
  methods: {
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

    aplastarBoton(){
      this.$router.push("/contenedor/factura")
    },

    // obtenerFecha(){
    //   this.fecha = new Date()
    //   console.log(this.fecha);
    // }

    obtenerData(){
      this.fecha = new Date()
      this.cliente = this.selected1
      this.celu = this.celu + this.selected2
    }
    
  }
};
</script>
