import pystray
from PIL import Image
import subprocess
import os

icon = Image.open("kubectx-gui.png")


def switch_context(icon, item):
    subprocess.run(["kubectx", str(item)], stderr=subprocess.DEVNULL)
    current_context = subprocess.run(["kubectx", "-c"], stdout=subprocess.PIPE, text=True)
    message = str("The k8s context has been switched to:\n") + str(current_context.stdout)
    os.system('notify-send "Kubectx!" "'+message+'"')


contexts = subprocess.run(["kubectx"], stdout=subprocess.PIPE, text=True)

menu_items = []

for context in contexts.stdout.split("\n")[:-1]:
    menu_items.append(pystray.MenuItem(context, switch_context))

menu = pystray.Menu(*menu_items)

icon = pystray.Icon("Kubectx-gui", icon, menu=menu)
icon.run()
