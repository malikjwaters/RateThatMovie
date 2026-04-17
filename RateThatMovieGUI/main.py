# import everything
from tlbx_imports import *

# import pages
from page_homepage import *
from page_login import *
from page_createacc import *
from page_search import *


# RUN WEBSITE
ui.run(reload=False, storage_secret="TEMP")