"""
A module that handles the functionality of rooms
"""
from rooms import Room
DICT_ROOMS = {}
DICT_DESCRIPTIONS = {}


def assembling_rooms(names, neighbors, doors, items):
    """
    Constructs room objects for all rooms in maze and stores all the rooms
    inside a dictionary.
    """
    scope = range(len(names))
    for i in scope:
        room = Room(names[i], neighbors[i], doors[i], items[i])
        DICT_ROOMS.update({room.name: room})


def assembling_descriptions(names, descriptions):
    """
    Adds the room descriptions for all rooms inside a dictionary.
    """
    scope = range(len(names))
    for i in scope:
        DICT_DESCRIPTIONS.update({names[i] : descriptions[i]})


def current_room(room_name):
    """
    The current room the player is in.
    """
    return DICT_ROOMS[room_name]


def room_description(room_name):
    """
    """
    return DICT_DESCRIPTIONS[room_name]


def items_in_room(room_name):
    """
    """
    return DICT_ROOMS[room_name].items

def is_item_in_room(room_name, item_name):
    """
    """
    return item_name in items_in_room(room_name)

def append_item(room_name, item_name):
    """
    """
    return DICT_ROOMS[room_name].add_item(item_name)


def delete_item(room_name, item_name):
    """
    """
    return DICT_ROOMS[room_name].delete_item(item_name)


def not_empty_room(room_name):
    """
    """
    return len(items_in_room(room_name)) != 0


def to_string_current_items(name):
    """
    Returns a string that lists the items in the selected room
    """
    item_list = 'You notice the following items--- '
    scope = range(len(DICT_ROOMS[name].items)-1)
    for i in scope:
        item_list += DICT_ROOMS[name].items[i] + ', '
    item_list += DICT_ROOMS[name].items[-1] + '.'
    return item_list


def move(cardinal, name):
    """
    Returns the current room of the player after the player moves
    a certain direction.
    """
    current_room_name = None
    if current_room(name).has_door_at(cardinal):
        print('Closed door')
    elif not current_room(name).has_neighbor(cardinal):
        print('No neighbor')
    else:
        current_room_name = current_room(name).neighbors[cardinal]
    return current_room_name
