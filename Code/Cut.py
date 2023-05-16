from rich import print
from rich import box
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.layout import Layout 
from rich.table import Table

from rich.live import Live
from rich.prompt import Prompt
from rich.progress import track
from rich.progress import Progress

from rich.traceback import install
install(show_locals=True)

def Cut():
    Cut_meals = Panel("", title = "Target : Cut", title_align = "left", border_style = "bold white", box = box.SQUARE)
    
    return Cut_meals