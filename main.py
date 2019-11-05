import setup
import GUI_ALL.gui as ui
from database.database import DB

from services.user import UserService
from services.group import GroupService


# get mac address from pawin
mac_address = 'mac address'

db = DB()
db.destroy_table()
db.init_table()

UserService.initMe(mac_address, '', '', '', 1)

print(UserService.getAvailableUser())


# Set up UI
ui.initUI()
