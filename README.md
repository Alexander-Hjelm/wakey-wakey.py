Assuming wakey-wakey.pi is placed at the top of your user's ~-directory, Add the following cronjob:

@reboot sh ~/wakey-wakey.py/launcher.sh >~/wakey-wakey.py/logs/cronlog 2>&1

Now reboot and enjoy your new 300W alarm clock! >:)
