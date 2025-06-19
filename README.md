# PPS2 Timing TB Analysis

This repository contains the scripts for analysing the data from the PPS2 Timing Test Beam campaigns.

## Setup

Either create the venv using the VS Code interface (if you are using VS Code), or do it by hand.

### Using VS Code Interface:

(Got the instructions from here: https://code.visualstudio.com/docs/python/tutorial-fastapi)

Open the VS Code command Pallette and run the **Python: Create Environment** command.

Select type **Venv** when asked.

Select the desired python version, typically the latest.

Select **requirements.txt** to install the dependencies.

You may need to follow up and run in the terminal the following command to update pip:
`python -m pip install --upgrade pip`


### By Hand:

Create a virtual evironment for working on things:

`python3 -m venv .venv`

Activate the venv:
`. .venv/bin/activate`

Inside the virtual environment, update things and install dependencies:
`python -m pip install --upgrade pip`
`python -m pip install -r requirements.txt`

Once you are done with the venv, remember to deactivate it with:
`deactivate`
