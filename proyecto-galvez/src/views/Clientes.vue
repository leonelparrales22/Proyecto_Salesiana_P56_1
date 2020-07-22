<template>
  <div class="page-wrapper">
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
                    href="#addEmployeeModal"
                    class="btn btn-success alinear-derecha"
                    data-toggle="modal"
                  >
                    <i class="material-icons">&#xE147;</i>
                    <span>Añadir nuevo cliente</span>
                  </a>
                </div>
              </div>
              <hr />
              <!-- INICIO TABLA -->
              <div class="container-xl">
                <div class="table-responsive">
                  <div class="table-wrapper">
                    <table class="table table-striped table-hover">
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
                        <tr>
                          <td>Thomas Hardy</td>
                          <td>thomashardy@mail.com</td>
                          <td>89 Chiaroscuro Rd, Portland, USA</td>
                          <td>(171) 555-2222</td>
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
                        <tr>
                          <td>Dominique Perrier</td>
                          <td>dominiqueperrier@mail.com</td>
                          <td>Obere Str. 57, Berlin, Germany</td>
                          <td>(313) 555-5735</td>
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
                        <tr>
                          <td>Maria Anders</td>
                          <td>mariaanders@mail.com</td>
                          <td>25, rue Lauriston, Paris, France</td>
                          <td>(503) 555-9931</td>
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
                        <tr>
                          <td>Fran Wilson</td>
                          <td>franwilson@mail.com</td>
                          <td>C/ Araquil, 67, Madrid, Spain</td>
                          <td>(204) 619-5731</td>
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
                        <tr>
                          <td>Martin Blank</td>
                          <td>martinblank@mail.com</td>
                          <td>Via Monte Bianco 34, Turin, Italy</td>
                          <td>(480) 631-2097</td>
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
                        Showing
                        <b>5</b> out of
                        <b>25</b> entries
                      </div>
                      <ul class="pagination">
                        <li class="page-item disabled">
                          <a href="#">Previous</a>
                        </li>
                        <li class="page-item">
                          <a href="#" class="page-link">1</a>
                        </li>
                        <li class="page-item">
                          <a href="#" class="page-link">2</a>
                        </li>
                        <li class="page-item active">
                          <a href="#" class="page-link">3</a>
                        </li>
                        <li class="page-item">
                          <a href="#" class="page-link">4</a>
                        </li>
                        <li class="page-item">
                          <a href="#" class="page-link">5</a>
                        </li>
                        <li class="page-item">
                          <a href="#" class="page-link">Next</a>
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
                        <h4 class="modal-title">Add Employee</h4>
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
                        <h4 class="modal-title">Edit Employee</h4>
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
import FooterComponent from "../components/FooterComponent.vue";
export default {
  name: "Clientes",
  components: {
    FooterComponent,
  },
};
</script>
