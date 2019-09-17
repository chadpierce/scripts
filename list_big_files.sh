#!/bin/bash
# lists all files over specified size - run with sudo
find /home/ -type f -size +100M -exec ls -lh {} \;
