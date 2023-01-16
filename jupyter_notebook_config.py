# SPDX-License-Identifier: Apache-2.0

c.NotebookApp.terminado_settings = {"shell_command": ["/bin/bash"]} #登入之後就是bash
c.ResourceUseDisplay.track_cpu_percent = True
c.Spawner.environment = {
    'JUPYTERHUB_SINGLEUSER_APP': "jupyter_server.serverapp.ServerApp"
}
c.FileContentsManager.delete_to_trash = True