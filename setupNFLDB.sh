#!/bin/bash

## Simple setup script that will pull and create a
## postgres docker container and load it with data

# Step 1 start a postgres docker container, and mount a local directory 
# for holding the db files
# POSTGRES_VOL="postgres_vol/postgresql"
# if [ ! -d "$POSTGRES_VOL" ];
# then
#     mkdir -p $POSTGRES_VOL
# fi

CONTAINER_NAME="nfl_db"
mkdir -p ~/temp/postgres
vol=`echo ~/temp/postgres`

## create container and mount file system for storage
docker run --name nfldb2 -p 5433:5432 -e PGDATA=/data -e POSTGRES_PASSWORD=pass -d scottmishra/nfldb2

echo "Finished creating the docker container...you may need to run again if this takes a long time"

## Start python installation
pip install -r requirement.txt
## Sleep until db comes up
#sleep 30
SHARE_LOC=`which nfldb-update`
SHARE_LOC=${SHARE_LOC%$"nfldb-update"}
SHARE_LOC="${SHARE_LOC}../share/nfldb/"
echo $SHARE_LOC
## Copy the config.ini to the nfldb share folder
cp config.ini ${SHARE_LOC}
#update to the latest game data
nfldb-update



