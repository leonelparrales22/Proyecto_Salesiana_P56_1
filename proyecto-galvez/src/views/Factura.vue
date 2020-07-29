<template>
  <div class="page-wrapper">
    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <h3 class="box-title m-t-40 tabla-titulo">Detalles de la Factura</h3>
              <hr />
              <div class="table-responsive">
                <h2>Compra realizada con exito!</h2>

                <table
                  id="mainTable"
                  class="table editable-table table-bordered table-striped m-b-0"
                >
                  <thead>
                    <tr>
                      <th>Celular</th>
                      <th>Cantidad</th>
                      <th>Unidad</th>
                      <th>Total</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="detalle in detalle_venta" :key="detalle.cantidad">
                      <td>{{detalle.nombre_celular}}</td>
                      <td>{{detalle.cantidad}}</td>
                      <td>{{detalle.precio_celular | moneda}}</td>
                      <td>{{(detalle.precio_celular*detalle.cantidad) | moneda}}</td>
                    </tr>
                  </tbody>
                  <tfoot>
                    <tr>
                      <th></th>
                      <th></th>

                      <th>
                        <strong class="alinear-derecha">Subtotal</strong>
                      </th>
                      <th>{{factura.subtotal | moneda}}</th>
                    </tr>
                    <tr>
                      <th></th>
                      <th></th>
                      <th>
                        <strong class="alinear-derecha">IVA</strong>
                      </th>
                      <th>{{factura.iva | moneda}}</th>
                    </tr>
                    <tr>
                      <th class="quitar_borde"></th>
                      <th></th>

                      <th>
                        <strong class="alinear-derecha quitar_borde">Total</strong>
                      </th>
                      <th>{{factura.total | moneda}}</th>
                    </tr>
                  </tfoot>
                </table>
                <br />
                <center>
                  <router-link to="/contenedor/preventa">
                    <button type="button" class="btn btn-success" v-on:click="aplastarBoton()">
                      <i class="fa fa-chevron-circle-left"></i> Volver
                    </button>
                  </router-link>
                </center>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { Global } from "../Global";
import axios from "axios";
export default {
  name: "Factura",
  components: {},
  data() {
    return {
      id_factura: this.$route.params.id_factura,
      factura: "",
      detalle_venta: [],
    };
  },
  mounted() {
    this.getFactura();
  },
  methods: {
    getFactura() {
      axios
        .get(Global.url + `consultar-factura?id_factura=${this.id_factura}`)
        .then((data) => {
          this.factura = data.data.result.factura;
          this.detalle_venta = data.data.result.detalle_venta;
          console.log(this.factura);
          console.log(this.detalle_venta);
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>