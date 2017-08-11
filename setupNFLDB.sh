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

docker volume create nfl_db
## create container and mount file system for storage
docker run --name "$CONTAINER_NAME" -p 5432:5432 --volume nfl_db:/var/lib/postgresql -e POSTGRES_PASSWORD=pass -d postgres:9.6-alpine

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
## get a zip of a current db 
#curl -LOk http://burntsushi.net/stuff/nfldb/nfldb.sql.zip
#unzip nfldb.sql.zip
## Create NFLDB
python ./createDB.py

# run nfldb-update
nfldb-update

# fixing jax error
python ./updateJAX.py

# rerun nfldb-update
nfldb-update



