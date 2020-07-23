<template>
    <div class="page-wrapper">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-12">
                    <div class="card">
                        <div class="card-body">
                            <h3 class="box-title m-t-40 tabla-titulo">Detalles de la Factura</h3>
                            <div class="table-responsive">
                                <table id="mainTable" class="table editable-table table-bordered table-striped m-b-0">
                                    <thead>
                                        <tr>
                                            <th>Celular</th>
                                            <th>Cantidad</th>
                                            <th>Total</th>  
                                        </tr> 
                                    </thead>
                                    <tbody>
                                        <tr>
                                        <td>Samsung S5</td>
                                        <td>2</td>
                                        <td>110.50</td>
                                    </tr>
                                    <tr>
                                        <td>Huawei Y5</td>
                                        <td>1</td>
                                        <td>120.50</td>
                                    </tr>
                                    <tfoot>
                                        <tr>
                                            <th><strong>Subtotal</strong></th>
                                            <th></th>
                                            <th>234.50</th>
                                        </tr>
                                        <tr>
                                            <th><strong>IVA</strong></th>
                                            <th></th>
                                            <th>10.50</th>
                                        </tr>
                                        <tr>
                                            <th><strong>Total</strong></th>
                                            <th></th>
                                            <th>245.00</th>
                                        </tr>
                                    </tfoot>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>