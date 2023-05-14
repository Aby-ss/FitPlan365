from rich import print
from rich import box
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.layout import Layout 
from rich.table import Table

from rich.prompt import Prompt
from rich.progress import track
from rich.progress import Progress

from rich.traceback import install
install(show_locals=True)

def Bulk():
    bulk_panel = Panel("[b]Bulking Meals\n\nProtein Shake: A high protein and calorie-dense meal. Simply blend together protein powder, milk, fruits, and healthy fats like nuts or nut butter\nChicken,Rice and Vegetables: This classic bodybuilder meal is high in protein, complex carbs, and fiber. Simply cook some chicken breasts, brown rice, and vegetables and you have a well-rounded meal\nTuna + Brown Rice: Tuna is a great source of protein and healthy fats, while brown rice provides complex carbs and fiber\nOatmeal + Fruits: Oatmeal is a great source of complex carbs and fiber, while fruits add natural sweetness and vitamins\nSmoothie Bowl: Smoothie bowls are a great way to pack in a variety of nutrients in one meal. Blend together some fruits, protein powder, veggies, and healthy fats", title = "Target : Bulk", title_align = "left", border_style = "bold white", box = box.SQUARE)
    
    return bulk_panel