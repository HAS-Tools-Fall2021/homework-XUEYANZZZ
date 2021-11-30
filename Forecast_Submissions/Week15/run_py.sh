#!/bin/bash
#SBATCH --job-name=test_py`
#SBATCH --ntasks=1
#SBATCH --nodes=1             
#SBATCH --mem=1gb                    
#SBATCH --time=00:01:00   
#SBATCH --partition=standard
#SBATCH --account=niug   
 
 
module load python/3.8
source ~/mypyenv/bin/activate

python Zhang_HW15.py
