#!/bin/bash
# run all on in a single job
# Yan Y. Liu <yanliu@illinois.edu>, 10/30/2016

sdir=/projects/nfie/nfie-floodmap/test/HUC6-catchmentmask-scripts
ldir=/projects/nfie/nfie-floodmap/test/HUC6-catchmentmask-logs
for s in `ls $sdir`
do
    n=`basename $s .sh`
    echo "/bin/bash $sdir/$s 1>$ldir/$n.stdout 2>$ldir/$n.stderr"
    /bin/bash $sdir/$s 1>$ldir/$n.stdout 2>$ldir/$n.stderr
done
