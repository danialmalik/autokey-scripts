user = clipboard.get_selection()
keyboard.send_keys("""
sudo -i su {app} -s /bin/bash
cd
source {app}_env
source venvs/{app}/bin/activate
""".format(app=user))
