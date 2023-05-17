from datetime import datetime
import csv
import time
import numpy as np
import asciichartpy

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

layout = Layout()

layout.split_column(
    Layout(name = "Header"),
    Layout(name = "Body"),
    Layout(name = "Footer")
)

layout["Body"].split_row(
    Layout(name = "Box1"),
    Layout(name = "Box2")
)

layout["Box1"].split_column(
    Layout(name = "left_Box1"),
    Layout(name = "left_Box2")
)

layout["Box2"].split_column(
    Layout(name = "right_Box1"),
    Layout(name = "right_Box2", size=27)
)

layout["left_Box2"].split_column(
    Layout(name = "LB2_1"),
    Layout(name = "LB2_2")
)

class Header:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "📰", "[b]FitPlan365[/]", datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="bold white")
    
class Footer:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "💻", "[b]FitPlan[/]365", "🍞")
        return Panel(grid, style="green on black")
    
    
def Header_title():
    return """          ______ _ _     _____  _               ____    __ _____ 
         |  ____(_) |   |  __ \| |             |___ \  / /| ____|
         | |__   _| |_  | |__) | | __ _ _ __     __) |/ /_| |__  
         |  __| | | __| |  ___/| |/ _` | '_ \   |__ <| '_ \___ \ 
         | |    | | |_  | |    | | (_| | | | |  ___) | (_) |__) |
         |_|    |_|\__| |_|    |_|\__,_|_| |_| |____/ \___/____/ 
 
        A plan to bring out the beast inside every human and become\n              a better version of yourself"""

layout["Header"].size = 3
layout["Footer"].size = 3
layout["Header"].update(Header())
layout["Footer"].update(Footer())
layout["right_Box1"].update(Header_title())


weight_target = Prompt.ask("What's your weight Target [Bulk or Cut]")

if (weight_target == "Bulk"):
    # Bulk panel update
    from Bulk import Bulk
    layout["left_Box1"].update(Bulk())
elif (weight_target == "Cut"):
    # Cut panel update
    from Cut import Cut
    layout["left_Box1"].update(Cut())
    
    
print(layout)