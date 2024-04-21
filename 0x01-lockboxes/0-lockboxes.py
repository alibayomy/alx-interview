#!/usr/bin/python3
"""Solution for lockboxes"""


def canUnlockAll(boxes):
    """Check if all the boxes can be oppend """

    boxes_map = [0] * len(boxes)
    boxes_map[0] = 1

    for key in boxes[0]:
        boxes_map[key] = 1

    for index,box  in enumerate(boxes[1:]):
        looping_index =  index  + 1 
        if boxes_map[looping_index] == 1 or looping_index in box:
            for key in box:
                boxes_map[key] = 1
    for items in boxes_map:
        if items == 0:
            return False
    return True
