import os.path

from winotify import Notification, audio


ICON_PATH = os.path.join(
    os.path.dirname(__file__),
    "assets",
    "icon.jpeg"
)

notification = Notification(
    f"Notification Test {__name__}",
    "Windows notification",
    msg="Testing windows notification alert",
    icon=ICON_PATH,
)

notification.set_audio(audio.Default, loop=False)
notification.add_actions("Open Rocketseat", "https://rocketseat.com.br/")
notification.add_actions("Open App Icon", f"file:///{ICON_PATH}")
notification.show()
