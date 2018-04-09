#!/bin/bash
: '
/*-------------------------------------
install.sh
nft

    by Daniel Richards (ddrichar@ucsc.edu)
       on 4-8-2018
--------------------------------------*/
'
NFT_PATH=`pwd`/new_from_template.py
ALIAS="alias nft='$NFT_PATH'"
echo $ALIAS >> ~/.bash_profile
. ~/.bash_profile
exit