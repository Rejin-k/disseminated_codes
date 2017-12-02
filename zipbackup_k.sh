#!/bin/bash

#!/bin/bash
read -p "Please enter the Folder path : "
if test -d $REPLY
then
    ls -l $REPLY
else
    echo "This is not a directory"
fi
zip -r backup$(date +"%Y-%m-%d-%s").zip $REPLY
exec bash
