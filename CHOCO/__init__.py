from CHOCO.core.bot import CHOCOBot
from CHOCO.core.dir import dirr
from CHOCO.core.git import git
from CHOCO.core.userbot import Userbot
from CHOCO.misc import dbb, heroku

from .logging import LOGGER

git()


dirr()

dbb()

heroku()

# Clients
app = CHOCOBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
