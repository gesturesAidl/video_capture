# VIDEO GESTURES CAPTURE  

## HOW TO RUN THE PROGRAM - video_capture

### Create Miniconda environment

Execute:

	conda env create -f environment.yml
	
This will generate the gesturesapp environment with all the required tools installed.
Once created activate the environment by typing:

	conda activate gesturesapp
	
### Update from environment.yml
    
    conda env update --file environment.yml

### Create .env file
Create a folder with name 'env' inside the project gesturesApp folder and then, create a .env file inside it.
Copy the following code to your .env file and set the fields with your rabbitmq broker connection parameters: 

    RABBIT_USER="..."
    RABBIT_PW="..."
    RABBIT_HOST="..."
    RABBIT_PORT="..."


### RUN project
Place yourself in the repository root dir and type: 

    python3 gesturesApp/app/app.py

> Notice that to run this app, your laptop camera should not be being used by any other process. 