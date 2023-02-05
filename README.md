## What is `kubectx-gui`?
**kubectx-gui** is a tool to switch between contexts (clusters) on kubectl faster. 
The tool is based on the original **kubectx** shell application and is a sys tray application for switching between contexts using a GUI.
## Dependecies
- installed python 3.X
- installed the kubectx tool from official repo - https://github.com/ahmetb/kubectx

## Installation
1. Clone the repo and install requirements:
```sh
$ cd /opt
$ git clone https://github.com/achelak/kubectx-gui.git
$ cd kubectx-gui
$ pip install -r requirements.txt --system
```
2. Execute the kubectx-gui
```sh
$ nohup python3 /opt/kubectx-gui/kubectx-gui.py &
```

