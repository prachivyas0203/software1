# Game Project

## Project Structer

# Project 4

This project is a simple game made with Python.

The project is divided into different files and a package.

## Project structure

- `main.py` - runs the game and contains the game menu.
- `classes/item.py` - contains the Item class.
- `classes/room.py` - contains the Room class.
- `classes/player.py` - contains the Player class.
- `classes/__init__.py` - makes the classes folder a Python package.

## Classes

### Item

The Item class has:
- name
- weight

### Room

The Room class has:
- name
- item

### Player

The Player class has:
- name
- items
- location

The player can:
- move to another room
- collect an item
- show collected items

## Game

When the program starts, it creates a player, rooms and items.

The player can use the menu to:
1. Show the current room
2. Move to another room
3. Collect an item
4. Show collected items
5. Quit the game

The project uses classes and objects to organize the game.
