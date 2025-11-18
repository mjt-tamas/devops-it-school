#!/bin/bash

SLEEP_INTERVAL=5

monitor_system() {
    # --- Current Date and Time ---
    echo "=========================================================="
    echo "Monitoring Data: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "----------------------------------------------------------"

    # --- OS Information ---
    echo "OS/Kernel Info:"
    echo "$(uname -a)"
    echo ""

    # --- CPU Information ---
    echo "CPU Usage (Top 1):"
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    echo "    Current Usage: ${CPU_USAGE}%"
    echo ""

    # --- RAM Information ---
    echo "RAM Usage (Total/Used/Available):"
    free -h | awk '/Mem:/ {print "    Total: "$2, "Used: "$3, "Available: "$7}'
    echo ""

    # --- Disk Information ---
    echo "Disk Usage (Root Filesystem /):"
    df -h / | awk 'NR==2 {print "    Total: "$2, "Used: "$3, "Available: "$4, "Usage: "$5}'
    echo "=========================================================="
}

echo "Starting Bash System Monitor (Interval: ${SLEEP_INTERVAL}s)..."
while true; do
    monitor_system
    sleep $SLEEP_INTERVAL
done