var mysql = require('mysql');
//Recordar cambiar la clave de hipermedial a '' cuando trabaje en windows

var conexion = mysql.createConnection({
    host: 'localhost',
    database: 'bdd',
    user: 'root',
    password: 'hipermedial',
});

conexion.connect(function(err) {
    if (err) {
        console.error('Error de conexion: ' + err.stack);
        return;
    }
    console.log('Conectado con el identificador ' + conexion.threadId);
});

conexion.query('SELECT * FROM VENTAS', function(error, results, fields) {

    if (error)
        throw error;

    results.forEach(result => {
        console.log(result);
    });
});
conexion.end();