# Introduction to Rust

This repository contains the Beamer code and the demo PyO3 project for my "Introduction to Rust" talk at [nwHacks 2024](https://nwhacks.io/).

## Viewing the Slides

A PDF with the slides can be found [on the Releases page](https://github.com/ADSteele916/nwhacks2024-talk/releases).

## Compiling the Slides

If, for whatever reason, you want to compile the slides, you'll need a $\LaTeX$ installation that supports the XeTeX typesetting engine. I use MiKTeX on Windows.
For the syntax highlighting to work, you'll need Pygments. Make sure that you have a modern system Python installation and run
```
pip install pygments
```
I haven't tested this with a virtual environment; I don't particularly care about a small bit of clutter in my global packages to make command-line utilities easily available.

## Running the Examples

If you would like to run the starter project, run these commands:
```
cd demo-starter/chirper
python -m venv venv
venv/bin/activate
python spam-detection/main.py
```
In order the run the solution project, run these commands:
```
cd demo-solution/chirper
python -m venv venv
venv/bin/activate
pip install maturin
maturin develop --release
python spam-detection/main.py
```
These should be fairly cross-platform between PowerShell and Bash. Note that on Windows, you'll want to run `venv/Scripts/activate` instead of `venv/bin/activate`.
