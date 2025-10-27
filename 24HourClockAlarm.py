#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: GutierrezJoshua_CSC500_CriticalThinking_Module1_Part2.py
Author: Joshua R. Gutierrez
Date: October 26, 2025
Version: 1.0
Description: A Python program that determines what time it will be on a 24-hour
clock after waiting a user-specified number of hours.
"""

# Ask the user for the current time and the number of hours to wait
current_time = int(input("Enter the current time (0-23): "))
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the alarm time using modulo to wrap around 24 hours
alarm_time = (current_time + hours_to_wait) % 24

# Display the result
print(f"\nWhen the alarm goes off, it will be {alarm_time}:00 on the 24-hour clock.")
