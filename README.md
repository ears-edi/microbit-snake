# Micro:bit Snake game

This repository contains the code for our "Build your own Snake game with the BBC micro:bit!" workshop. The structure of the repository is as follows:

### snake.py

This file contains the completed workshop code. This can be flashed directly onto your micro:bit to play the game.

### \[number\]\[description\].py

These are files that contain flashable code that progresses from nothing through the features of the game. These are intended for people that didn't manage to code each stage of the workshop.

### intro\_programming

This directory contains an alternative progression of making the game for people with less experience programming. More of the code is written already, and not all steps are done by the tutee.

## Running the file on the micro:bit

You will need `python3` and `pip`.

Run the following in this directory with a micro:bit connected and mounted.

```
pip install uflash
uflash snake.py
```

Your micro:bit will then flash an orange LED for some time and reboot into the snake game code.

## Running this as a workshop

Slides from this workshop as we run it are available [here](https://docs.google.com/presentation/d/1d5NM7Sf5eOalQJ1Otfe1fJ4gtUMj3hgkXyFJPTEyZik/edit?usp=sharing).

Attribution would be nice if you decide to run this, but it's not necessary. You are free to use and change this workshop and the code contained within as you please.
