#!/bin/bash

OUTFILE="temp.txt"

./thermal_weather.py > ${OUTFILE}
lp ${OUTFILE}
rm ${OUTFILE}

