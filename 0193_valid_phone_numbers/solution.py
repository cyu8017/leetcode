# LeetCode 0193 - Valid Phone Numbers
# https://leetcode.com/problems/valid-phone-numbers/

# Write a bash script to solve the problem
SCRIPT = r"""
#!/bin/bash
grep -E '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt
"""
