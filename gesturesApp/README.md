# Gestures recognition app

## Installation
##### Before Installation

Before starting, make sure you have Python and that it's available from your command line. 
You can check this by simply running:

```bash
#!/bin/bash
$ python --version
```

You should get some output like ```3.7.6.```
 
##### Installation
If you do not have Python, please install the latest 3.x version from python.org or refer to the Installing Python section of this [guide](https://docs.python-guide.org/starting/installation/).


### Install Miniconda

To test your installation, in your terminal window or Anaconda Prompt, run the command conda list.
Open terminal, type "bash" and press ENTER
Then run conda list

### Create Miniconda environment

Execute:

	conda env create -f environment.yml
	
This will generate the gesturesapp environment with all the required tools installed.
Once created activate the environment by typing:

	conda activate gesturesapp
	
### Update from environment.yml
    
    conda env update --file environment.yml
