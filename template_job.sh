#!/bin/bash
#$ -cwd
#$ -j y
#$ -S /bin/bash
#
#$ -l virtual_free=30G
#
#$ -m e
#$ -M aefrainmp@protonmail.com
#
. /etc/profile.d/modules.sh

module load anaconda3/2021.05

source activate crossmap64

