[Setup]
AppName=Hola Mundo Luis
AppVersion=1.0.0
DefaultDirName={commonpf}\HolaMundo
OutputBaseFilename=HolaMundo_Installer
SetupIconFile=resources\icono_spsil.ico
Compression=lzma
SolidCompression=yes

[Run]
Filename: "powershell.exe";
Parameters: "-ExecutionPolicy Bypass -Command ""Invoke-WebRequest -Uri https://github.com/larceing/hola_mundo_autoupdate/releases/latest/download/hola_mundo.zip -OutFile '{app}\update.zip'; Expand-Archive -Force '{app}\update.zip' '{app}'; Remove-Item '{app}\update.zip'; Start-Process '{app}\main.exe'"""
Flags: runhidden

[Icons]
Name: "{group}\Hola Mundo Luis"; Filename: "{app}\main.exe"
Name: "{commondesktop}\Hola Mundo Luis"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Crear acceso directo en el escritorio"; GroupDescription: "Opciones adicionales"
