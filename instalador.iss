[Setup]
AppName=Hola Mundo Luis
AppVersion=1.0.0
DefaultDirName={commonpf}\HolaMundo
DefaultGroupName=Hola Mundo Luis
OutputBaseFilename=HolaMundo_Installer
Compression=lzma
SolidCompression=yes

[Run]
Filename: "{tmp}\instalador.ps1"; Flags: runhidden

[Icons]
Name: "{group}\Hola Mundo Luis"; Filename: "{app}\main.exe"
Name: "{commondesktop}\Hola Mundo Luis"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Crear acceso directo en el escritorio"; GroupDescription: "Opciones adicionales"

[Code]
procedure CurStepChanged(CurStep: TSetupStep);
var
  PSPath: string;
  Script: string;
begin
  if CurStep = ssPostInstall then begin
    PSPath := ExpandConstant('{tmp}\instalador.ps1');
    Script :=
      'Invoke-WebRequest -Uri https://github.com/larceing/hola_mundo_autoupdate/releases/latest/download/hola_mundo.zip -OutFile "$env:ProgramFiles\HolaMundo\update.zip"' + #13#10 +
      'Expand-Archive -Path "$env:ProgramFiles\HolaMundo\update.zip" -DestinationPath "$env:ProgramFiles\HolaMundo" -Force' + #13#10 +
      'Remove-Item "$env:ProgramFiles\HolaMundo\update.zip"' + #13#10 +
      'Start-Process "$env:ProgramFiles\HolaMundo\main.exe"';
    SaveStringToFile(PSPath, Script, False);
  end;
end;
