const electron = require('electron')
const { app, BrowserWindow } = electron

const path = require('path')
const url = require('url')

let win

function createWindow() {
    win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {

            nodeIntegration: true

        }
    })
    win.loadURL(url.format({
        pathname: path.join(__dirname, '/html/usuarios.html'),
        protocol: 'file',
        slashes: true
    }))

    //win.webContents.openDevTools() //Esta opción permite abrir las herramientas de desarrollador para revisar posibles errores en la aplicación a desarrollar
    win.setMenuBarVisibility(false) //Esta opción permite ocultar la barra de menú en la aplicación a desarrollar actualmente
}


app.on('ready', createWindow)