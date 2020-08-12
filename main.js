
const { app, BrowserWindow } = require("electron");
const path = require("path");
var python = require("python-shell");
var spawn = require("child_process").spawn;

function createWindow() {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
      nodeIntegration: true,
    },
  });
  let { PythonShell } = require("python-shell");
 
  PythonShell.run("engine.py",null, function (err, results) {
    if (err) console.log(err);
    console.log('fask connected ');
  });

  // and load the index.html of the app.
  mainWindow.loadFile("index.html");


}


app.whenReady().then(() => {
  createWindow();

  app.on("activate", function () {

    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on("window-all-closed", function () {
  if (process.platform !== "darwin") app.quit();
});

