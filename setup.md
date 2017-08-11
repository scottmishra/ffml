# So you want to use this setup.....
# Things to know:
- The setup of the data is still under construction and will be fully dockerized eventually, this is a short term solution to help get the ml team off the ground

# Before you start things you need installed:
- Python version 2.7.13 is required
- Docker is required and is helpful becuase the postgres setup sucksss
- Have bash or bash emulator install (git bash will work on windows)
- virtualenv are super helpful, and they are required for the setups

- run pip install virtualenv
- create a project directory 
- create a virtualenv
    - virtualenv <whatever you want>
- source /path/to/virtualenv/<Script/bin>/activate (Script for windows, bin for linux/mac)
- make sure the you set python 2.7.XX as the working versionss
- run the setupNFLDB.sh script (./setupNFLDB.sh)
- wait
- wait
- wait (the initial loading of the nfldb takes a long time since there is a like 2675 gamessss)
