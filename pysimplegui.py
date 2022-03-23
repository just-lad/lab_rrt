import PySimpleGUI as sg

import rrt_connect as rrt

"""
    Embedding the Matplotlib toolbar into your application

"""

# ------------------------------- This is to include a matplotlib figure in a Tkinter canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def get_env(combo):
    if combo == "Среда 1":
        return 0
    elif combo == "Среда 2":
        return 1
    elif combo == "Среда 3":
        return 2
    elif combo == "Среда 4":
        return 3


def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


# ------------------------------- PySimpleGUI CODE

layout = [
    [sg.T('Программа построения графиков')],
    [sg.B('Построить график'),
     sg.B('Выйти'),
     sg.Combo(values=('Среда 1', 'Среда 2', 'Среда 3', 'Среда 4'), default_value='Среда 1', readonly=True, k='-COMBO-'),
     sg.T('Выбрать шаг:'),
     sg.Slider(range=(1.0, 500.0), resolution=1, orientation='horizontal', k='-SLIDER-'),
     sg.T('Число итераций:'),
     sg.Text("", size=(0, 1), key='OUTPUT')],
    [sg.T('Настройки графика:')],
    [sg.Canvas(key='controls_cv')],
    [sg.T('График:')],
    [sg.Column(
        layout=[
            [sg.Canvas(key='fig_cv',
                       # it's important that you set this size
                       size=(500 * 2, 500)
                       )]
        ],
        background_color='#DAE0E6',
        pad=(0, 0)
    )]
]

window = sg.Window('Лабораторная работа RRT-Connect', layout)


while True:
    event, values = window.read()
    #print(event, values)
    if event in (sg.WIN_CLOSED, 'Выйти'):  # always,  always give a way out!
        break

    elif event is 'Построить график':
        # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE
        try:
            x_start = (20, 20)  # Starting node
            x_goal = (490, 240)  # Goal node

            env_index = get_env(values['-COMBO-'])
            rrt_step = values['-SLIDER-']
            rrt_conn = rrt.RrtConnect(x_start, x_goal, rrt_step, 15000, env_index)
            path, iterations = rrt_conn.planning()
            window['OUTPUT'].update(value=iterations)
            print(iterations)
            fig = rrt_conn.plotting.animation_connect(rrt_conn.V1, rrt_conn.V2, path, "Метод RRT-Connect")
        # ------------------------------- Instead of plt.show()
            draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)
        except:
            pass

window.close()
