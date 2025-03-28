#!/bin/bash 
rm -rf ./images/*
python motivation-throughput-cache.py
python motivation-distribution.py
python motivation-clocks.py
python design-throughput-cache.py
python evaluation-batchsize.py
python evaluation-workload.py
python evaluation-dist.py
python evaluation-multicore.py
python evaluation-alg.py
python evaluation-overhead.py