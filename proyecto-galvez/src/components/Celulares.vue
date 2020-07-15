<template>
  <div class="page-wrapper">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <div class="card">
            <div class="card-body">
              <h4 class="card-title tabla-titulo">Registro Celulares</h4>
              <hr />
              <div class="table-responsive">
                <table id="mainTable" class="table">
                  <thead>
                    <tr>
                      <th>Cedula</th>
                      <th>Nombre</th>
                      <th>Apellido</th>
                      <th>Dirección</th>
                      <th>Editar</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>0923159099</td>
                      <td>Leonel</td>
                      <td>Parrales</td>
                      <td>La Concepción</td>
                      <td>
                        <img
                          src="../assets/img/lapiz.jpg"
                          width="25"
                          height="25"
                        />
                      </td>
                    </tr>
                    <tr>
                      <td>0923159099</td>
                      <td>Leonel</td>
                      <td>Parrales</td>
                      <td>La Concepción</td>
                      <td>
                        <img
                          src="../assets/img/lapiz.jpg"
                          width="25"
                          height="25"
                        />
                      </td>
                    </tr>
                    <tr>
                      <td>0923159099</td>
                      <td>Leonel</td>
                      <td>Parrales</td>
                      <td>La Concepción</td>
                      <td>
                        <img
                          src="../assets/img/lapiz.jpg"
                          width="25"
                          height="25"
                        />
                      </td>
                    </tr>
                    <tr>
                      <td>0923159099</td>
                      <td>Leonel</td>
                      <td>Parrales</td>
                      <td>La Concepción</td>
                      <td>
                        <img
                          src="../assets/img/lapiz.jpg"
                          width="25"
                          height="25"
                        />
                      </td>
                    </tr>
                    <tr>
                      <td>0923159099</td>
                      <td>Leonel</td>
                      <td>Parrales</td>
                      <td>La Concepción</td>
                      <td>
                        <img
                          src="../assets/img/lapiz.jpg"
                          width="25"
                          height="25"
                        />
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <FooterComponent />
  </div>
  <!-- Column -->
</template>

<script>
import FooterComponent from "./FooterComponent.vue";
export default {
  name: "Celulares",
  components: {
    FooterComponent,
  },
};
</script>
