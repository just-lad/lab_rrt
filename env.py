"""
Environment for rrt_2D
@author: huiming zhou
"""


class Env:
    def __init__(self, env_index):
        self.x_range = (0, 500)
        self.y_range = (0, 300)
        self.obs_boundary = obs_boundary()
        self.obs_circle = obs_circle(env_index)
        self.obs_rectangle = obs_rectangle(env_index)


def obs_boundary():
    obs_bound = [
        [0, 0, 10, 300],
        [0, 300, 500, 10],
        [10, 0, 500, 10],
        [500, 10, 10, 300]
    ]
    return obs_bound


def obs_rectangle(env_index):
    obs_rect = [
        [
        [0, 0, 0, 0]
        ],
        [
        [100, 10, 100, 250],
        [300, 50, 100, 250]
        ],
        [
        [260, 70, 0, 0]
        ],
        [
        [140, 120, 80, 20],
        [180, 220, 80, 30],
        [260, 70, 20, 120],
        [320, 140, 100, 20]
        ]
    ]
    return obs_rect[env_index]


def obs_circle(env_index):
    obs_cir = [
        [
        [0, 0, 0]
        ],
        [
        [0, 0, 0]
        ],
        [
        [250, 150, 120]
        ],
        [
        [70, 120, 30],
        [460, 200, 20],
        [150, 50, 20],
        [370, 70, 30],
        [370, 230, 30]
        ]
    ]

    return obs_cir[env_index]
