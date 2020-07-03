var mysql = require('mysql');
var conexion = mysql.createConnection({
    host: 'localhost',
    database: 'bdd',
    user: 'root',
    password: '',
});

conexion.connect(function(err) {
    if (err) {
        console.error('Error de conexion: ' + err.stack);
        return;
    }
    console.log('Conectado con el identificador ' + conexion.threadId);
});

conexion.query('SELECT * FROM detalle_venta', function(error, results, fields) {
    if (error)
        throw error;

    results.forEach(result => {
        console.log(result);
    });
});
conexion.end();