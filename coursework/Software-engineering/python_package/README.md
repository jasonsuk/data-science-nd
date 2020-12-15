# Create a Python package

To convert the modularized code into a Python package.

To install the Python package locally, set up a virtual environment first. Scroll down to `Virtual environment` for instructions.

## Instructions

Create

-   inside 'python_package' folder, a setup.py file, which is required in order to use pip install

-   a folder called 'distributions', which is the name of the Python package

-   inside the 'distributions' folder, the Gaussiandistribution.py file, Generaldistribution.py and an **init**.py file.

Once everything is set up, get back to `python_package` and type `pip install .`

If everything is set up correctly, pip will install the distributions package into the workspace.
Then start the python interpreter from the terminal typing: `python`

Then within the Python interpreter, try the distributions package:
from distributions import Gaussian
gaussian_one = Gaussian(25, 2)
gaussian_one.mean
gaussian_one + gaussian_one

In other words, to import and use the Gaussian class should work because the distributions package is now officially installed as part of Python installation.

## Virtual environment

To install the Python package locally, set up a virtual environment first. A virtual environment is a siloed Python installation apart from main Python installation. That way allows users to delete the virtual enviornment without affecting Python installation.

To try using virtual environment locally :

### Conda

Conda does two things: manages packages and manages environments.

As a package manager, conda makes it easy to install Python packages especially for data science. For instance, typing conda install numpy will install the numpy package.

As an environment manager, conda can create silo-ed Python installations. With an environment manager, packages can be locally installed on computer without affecting the main Python installation.

The command line code looks something like this:

    conda create --name environmentname
    source activate environmentname
    conda install numpy

**[IMPORTANT]** If you create a conda environment, activate the environment, and then pip install the distributions package, you'll find that the system installs your package globally rather than in your local conda environment. However, if you create the conda environment and install pip **simultaneously**, you'll find that pip behaves as expected installing packages into your local environment:

    conda create --name environmentname pip

### Pip and Venv

-   There may sometimes an issue with the operating system(especially Ubunta) and Python3 where the venv package isn't installed correctly. One way to fix this is by running this command in the workspace terminal: `conda update python` See: https://stackoverflow.com/questions/26215790/venv-doesnt-create-activate-script-python3 Then type `y` when prompted. It might take a couple of minutes for the workspace to update. If not using anaconda on a local computer, this first step can be skipped.

-   Next, type this command to create a virtual environment `python -m venv venv_name` where venv_name is the name that the user want to specify for a virtual environment. A new folder then will appear with the Python installation named venv_name

-   In the terminal, type `source venv_name/bin/activate`. Notice that the command line now shows (venv_name) at the beginning of the line to indicate the venv_name virtual environment is activated.

-   Now, type `pip install python_package/.` That should install `distributions` Python package.

-   Try using the package in a program to see if everything works!

#### Example :

    python3 -m venv environmentname
    source environmentname/bin/activate
    pip install numpy
