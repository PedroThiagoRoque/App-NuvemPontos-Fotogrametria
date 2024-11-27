[app]

# (str) Title of your application
title = Aplicativo Fotogrametria 3D

# (str) Package name
package.name = fotogrametria3d

# (str) Package domain (unique, for example com.myname.app)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (list) Permissions required by the app (for accessing camera and storage)
android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (list) Application requirements
requirements = python3, kivy, kivymd, jnius

# (str) The entry point of your application (default is main.py)
entrypoint = main.py

# (str) Supported orientation
orientation = portrait

# (bool) Enable fullscreen mode (default is 1)
fullscreen = 1
