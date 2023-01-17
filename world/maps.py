from evennia.contrib.grid.xyzgrid import xymap_legend

class TransitionToDragonLair(xymap_legend.MapTransitionNode):
    target_map_xyz = (1, 1, "dragon_lair")

LEGEND = {
    'D': TransitionToDragonLair
}
MINE_PROTOTYPES = {
    ('*', '*'): {
        "prototype_parent": "xyz_room",
        "key": "A rock-strewn mining tunnel",
        "desc": "Chips of rock and piles of debris line the wall of this hastily-dug mine."
    },
    ('*', '*', '*'): {
        "prototype_parent": "xyz_exit",
        "desc": "The mine looms deep into the aerth."
    }
}
CASTLE_PROTOTYPES = {
    ('*', '*'): {
        "prototype_parent": "xyz_room",
        "key": "A stone hallway",
        "desc": "Stone bricks have been laid here to form a hallway which stretches away out of sight."
    },
    ('*', '*', '*'): {
        "prototype_parent": "xyz_exit",
        "desc": "The hallway stretches out in front of you."
    }
}
COLUMNS_PROTOTYPES = {
    ('*', '*'): {
        "prototype_parent": "xyz_room",
        "key": "A wide open space",
        "desc": "Stone bricks pave the floor and stone columns bear the massive weight of the structure, but no walls obstruct your view in any direction."
    },
    ('*', '*', '*'): {
        "prototype_parent": "xyz_exit",
        "desc": "The open space stretches out all around you."
    }
}
LAIR_PROTOTYPES = {
    ('*', '*'): {
        "prototype_parent": "xyz_room",
        "key": "A dragon's lair",
        "desc": "This pit has been dug out of the floor, clawed deep into the bedrock, the floor melted to slag by the breath of some fearsome creature."
    },
    ('*', '*', '*'): {
        "prototype_parent": "xyz_exit",
        "desc": "Uneven melted rock stretches before you."
    }
}
OPTIONS = {
    "map_display": True
}

MAP_1_STR = r"""

+ 0 1 2 3 4

4 #-#-# #-#
    |  \|/ 
3 # #-#-#-#
  |/  |   |
2 #-# #-#-#
  | | | | 
1 #-#-#-#-#
   x|\ x  |
0 #-# # # #

+ 0 1 2 3 4

"""

MAP_1 = { # mine level
    "zcoord": "level_one",
    "map": MAP_1_STR,
    "legend": LEGEND,
    "prototypes": MINE_PROTOTYPES,
    "options": OPTIONS
}

MAP_2_STR = r"""

+ 0 1 2 3 4

4 #-# #-# #
  |  x|  x
3 # # #-# #
   x /  |/|
2 # # # # #
  | | | | |
1 # #-# # #
   x   / /|
0 # #-# #-#

+ 0 1 2 3 4

"""

MAP_2 = { # storage level
    "zcoord": "level_two",
    "map": MAP_2_STR,
    "legend": LEGEND,
    "prototypes": MINE_PROTOTYPES,
    "options": OPTIONS
}

MAP_3_STR = r"""

+ 0 1 2 3 4

4 #-# # #-#
  |  x x /|
3 # # # # #
   \| |  /|
2 #-# #-# #
    | |  /|
1 #-# #-# #
    |  \ \|
0 #-#-# #-#

+ 0 1 2 3 4

"""

MAP_3 = { # castle level
    "zcoord": "level_three",
    "map": MAP_3_STR,
    "legend": LEGEND,
    "prototypes": CASTLE_PROTOTYPES,
    "options": OPTIONS
}

MAP_4_STR = r"""

+ 0 1 2 3 4

4 #-#-#-#-#
   \| |  /|
3 # # # # #
   x / \ /
2 # #-#-# #
  | | | |/|
1 #-# # #-#
  |\   x  | 
0 #-#-#-#-#

+ 0 1 2 3 4

"""

MAP_4 = { # castle level
    "zcoord": "level_four",
    "map": MAP_4_STR,
    "legend": LEGEND,
    "prototypes": CASTLE_PROTOTYPES,
    "options": OPTIONS
}

MAP_5_STR = r"""

+ 0 1 2 3 4

4 #-#-#-#-#
  |x|x|x|x|
3 #-#-#-#-#
  |x|/|\|x|
2 #-# D #-#
  |x|\ /|x|
1 #-#-#-#-#
  |x|x|x|x|
0 #-#-#-#-#

+ 0 1 2 3 4

"""

MAP_5 = { # columns level
    "zcoord": "level_five",
    "map": MAP_5_STR,
    "legend": LEGEND,
    "prototypes": COLUMNS_PROTOTYPES,
    "options": OPTIONS
}

MAP_DRAGON_STR = r"""

+ 0 1 2

2   #
   /|\
1 #-#-#
   \|/
0   #

+ 0 1 2

"""

MAP_DRAGON = {
    "zcoord": "dragon_lair",
    "map": MAP_DRAGON_STR,
    "legend": LEGEND,
    "prototypes": LAIR_PROTOTYPES,
    "options": OPTIONS
}

XYMAP_DATA_LIST = [
    MAP_1,
    MAP_2,
    MAP_3,
    MAP_4,
    MAP_5,
    MAP_DRAGON
]