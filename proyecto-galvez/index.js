const { app, BrowserWindow, ipcMain } = require('electron')

function createWindow() {

    let win = new BrowserWindow({
        width: 1400,
        height: 1400,
        webPreferences: {
            nodeIntegration: true
        }
    })
    win.setMenuBarVisibility(false) //Esta opción permite ocultar la barra de menú en la aplicación a desarrollar actualmente
    win.loadURL("file://" + __dirname + "/dist/index.html")
}

app.on('ready', createWindow)