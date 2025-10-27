#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: GutierrezJoshua_CSC500_CriticalThinking_Module1_Part1.py
Author: Joshua R. Gutierrez
Date: October 26, 2025
Version: 1.0
Description: A Python program that calculates the total cost of a meal including
an 18% tip and a 7% sales tax based on the user's input.
"""

# Ask the user to enter the charge for the food
food_charge = float(input("Enter the charge for the food: $"))

# Calculate tip and tax
tip = food_charge * 0.18
tax = food_charge * 0.07

# Calculate the total cost
total = food_charge + tip + tax

# Display the results
print("\n--- Meal Cost Breakdown ---")
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${tax:.2f}")
print(f"Total Amount: ${total:.2f}")
