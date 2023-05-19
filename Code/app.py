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

layout["right_Box2"].split_column(
    Layout(name = "RB2_1"),
    Layout(name = "RB2_2")
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


def workout_stats():
    stats = Panel("""  [b]_      __         __             __ 
 | | /| / /__  ____/ /_____  __ __/ /_     [b red]Last Workout : Arms[/]
 | |/ |/ / _ \/ __/  '_/ _ \/ // / __/     [b green]Duration : 2hrs 27 mins[/]
 |__/|__/\___/_/ /_/\_\\___/\_,_/\__/[/]      [b green] Calories burnt : 2500 cal[/]
                                           [b red]Workout Intensity : Hard[/]
                                           [b green]Workout no. of week : 5th[/]
                                           [b green]Exercises : 25[/]
                                      """, title = "Workout Stats", title_align = "left", border_style = "bold white", box = box.SQUARE)
    
    return stats

def Music_player():
    music_panel = Panel("""  [b]  ______                         ___                  __        
   /_  __/__  __ _________  ___   / _ \___ ____  ___   / /__      
    / / / _ \/ // / __/ _ \/ -_) / // / _ `/ _ \(_-<  / / -_) _ _ 
   /_/  \___/\_,_/_/ /_//_/\__/ /____/\_,_/_//_/___/ /_/\__/ (_|_)[/]
                                                                                    
                                                                                
    <----------------*----------------------------------------------->
    1:45                  Tourne Dans le Vide                     5:45""", title = "Music Player", title_align = "left", border_style = "bold white", box = box.SQUARE)
    
    return music_panel


def challenges():
    challenge_panel = Panel("[b red]New Challenge ⚠[/]\nWorkout 3x a day for a week for a bonus subscription\n\nShowcase your dedication and commmitment by working above your limits and uncover the beauty of your body and get a bonus subscription plan as a reward where you won't have to pay for any further meal plans for the next 2 months. So what are you waiting for ? Get to work and get astonished by the results", title = "New Challenge 📩", title_align = "left", border_style = "bold white", box = box.SQUARE)
    
    return challenge_panel

layout["Header"].size = 3
layout["Footer"].size = 3
layout["Header"].update(Header())
layout["Footer"].update(Footer())
layout["right_Box1"].update(Header_title())
layout["LB2_1"].update(workout_stats())
layout["LB2_2"].update(Music_player())
layout["RB2_1"].update(challenges())


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