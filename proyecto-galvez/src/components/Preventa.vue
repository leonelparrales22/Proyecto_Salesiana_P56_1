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
                        <select class="form-control custom-select">
                          <option>--Seleccione un cliente--</option>
                          <option>Mario Suin</option>
                          <option>Esteban González</option>
                          <option>Marco Maila</option>
                        </select>
                      </div>
                    </div>
                    <!--/span-->
                  </div>
                  <div class="row">
                    <!--/span-->
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Celulares</label>
                        <select class="form-control custom-select">
                          <option>--Seleccione un celular--</option>
                          <option>Samsung A50</option>
                          <option>Iphone 5S</option>
                          <option>Samsung j6</option>
                        </select>
                      </div>
                    </div>
                    <!--/span-->
                    <div class="col-md-6">
                      <div class="form-group">
                        <label>Cantidad</label>
                        <input type="text" class="form-control" />
                      </div>
                      <button type="submit" class="btn btn-inverse">
                        <i class="fa fa-check"></i> Añadir otro celular
                      </button>
                    </div>
                  </div>
                  <br />
                  <br />
                  <center>
                    <button type="submit" class="btn btn-success">
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
    <FooterComponent />
  </div>
</template>

<script>
import FooterComponent from "./FooterComponent.vue";
export default {
  name: "Preventa",
  components: {
    FooterComponent,
  },
};
</script>
