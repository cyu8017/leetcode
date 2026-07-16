#!/usr/bin/env python3
"""Write EXPLANATION.md for all solved problems."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPLANATIONS: dict[str, str] = {
    "0001_two_sum": """# How We Solve Two Sum

You have a list of numbers. Find **two numbers** that add up to a target.

## Steps

1. Look at each number one at a time.
2. For each number, ask: "What friend number do I need to reach the target?"
3. Keep a notebook (hash map) of numbers you already saw and where they are.
4. If the friend number is in the notebook, you found the answer.
5. If not, write this number in the notebook and keep going.
6. Return the two positions of the pair.
""",
    "0002_add_two_numbers": """# How We Solve Add Two Numbers

Two numbers are stored as linked lists (digits from right to left, like beads).

## Steps

1. Start at the first bead of both lists.
2. Add the two digits plus any carry (like 7+8=15, carry the 1).
3. Make a new bead with the ones digit of the sum.
4. Move to the next beads and repeat.
5. Keep going until both lists are done and carry is zero.
6. Return the new list.
""",
    "0003_longest_substring_without_repeating_characters": """# How We Solve Longest Substring Without Repeating Characters

Find the **longest part** of a word where no letter repeats.

## Steps

1. Use two fingers: left and right on the word.
2. Move the right finger and grow the window.
3. If a letter repeats, move the left finger until the repeat is gone.
4. After each move, check if this window is the longest so far.
5. Keep sliding until the right finger reaches the end.
6. Return the best length.
""",
    "0004_median_of_two_sorted_arrays": """# How We Solve Median of Two Sorted Arrays

Two sorted lists join into one big sorted list. Find the **middle value**.

## Steps

1. Binary search on the shorter list to pick a cut.
2. Cut the other list so left parts have the same total size.
3. Check: biggest on left <= smallest on right (for both lists).
4. If not, move the cut and try again.
5. When it fits, the median comes from the edge values of the cuts.
6. Return that number (average if even total length).
""",
    "0005_longest_palindromic_substring": """# How We Solve Longest Palindromic Substring

A palindrome reads the same forward and backward (like "aba").

## Steps

1. Try every letter as the middle of a palindrome.
2. Grow outward while both sides match.
3. Also try between two letters (even-length palindromes).
4. Remember the longest palindrome found.
5. Return that substring.
""",
    "0006_zigzag_conversion": """# How We Solve Zigzag Conversion

Write letters in a zigzag, then read row by row.

## Steps

1. Make one row bucket for each zigzag level.
2. Walk through each letter.
3. Put the letter in the current row.
4. Bounce down then up between rows.
5. Glue all rows together left to right.
6. Return the final string.
""",
    "0007_reverse_integer": """# How We Solve Reverse Integer

Flip the digits (123 becomes 321).

## Steps

1. Start with reversed = 0.
2. Peel off the last digit of the number.
3. Stick it on the end of reversed.
4. Remove that digit from the original number.
5. Stop if the answer gets too big (32-bit limit).
6. Return reversed, or 0 if overflow.
""",
    "0008_string_to_integer_atoi": """# How We Solve String to Integer (atoi)

Turn text like "   -42abc" into the number -42.

## Steps

1. Skip spaces at the start.
2. Read + or - if there is one.
3. Read digits while they are 0-9.
4. Stop at the first non-digit.
5. Clamp to 32-bit min/max if needed.
6. Return the integer.
""",
    "0009_palindrome_number": """# How We Solve Palindrome Number

Check if a number reads the same backward.

## Steps

1. Negative numbers are not palindromes.
2. Build half the digits in reverse.
3. Each step: take last digit, add to reversed pile, chop original.
4. Stop when original <= reversed.
5. Compare original and reversed (odd length allows middle digit).
6. Return true or false.
""",
    "0010_regular_expression_matching": """# How We Solve Regular Expression Matching

Match a word to a pattern with `.` (any letter) and `*` (repeat).

## Steps

1. Make a table: word length x pattern length.
2. Empty word + empty pattern = match.
3. Fill each cell using smaller sub-problems.
4. `*` can mean "skip this pair" or "use another letter."
5. Matching letters copy the diagonal yes from smaller parts.
6. Bottom-right cell is the final answer.
""",
    "0011_container_with_most_water": """# How We Solve Container With Most Water

Tall bars hold water between them. Find the **most water**.

## Steps

1. Put a left finger at the start and right finger at the end.
2. Water height = shorter bar times the width between fingers.
3. Keep the best (max) water seen.
4. Move the finger at the **shorter** bar inward.
5. Repeat until fingers meet.
6. Return the best water amount.
""",
    "0012_integer_to_roman": """# How We Solve Integer to Roman

Turn a number into Roman numerals (like 58 -> LVIII).

## Steps

1. Make a list of value + symbol pairs (biggest first).
2. Include subtractive pairs like 4 -> IV.
3. While number > 0, take the biggest symbol that fits.
4. Write that symbol and subtract its value.
5. Repeat until the number becomes zero.
6. Return the Roman string.
""",
    "0013_roman_to_integer": """# How We Solve Roman to Integer

Turn Roman numerals back into a number.

## Steps

1. Start total = 0.
2. Read symbols from right to left.
3. If a symbol is smaller than the one before it, subtract it.
4. Otherwise add it.
5. Move left and repeat.
6. Return the total.
""",
    "0014_longest_common_prefix": """# How We Solve Longest Common Prefix

Find the shared start of all words (like "flower", "flow", "flight" -> "fl").

## Steps

1. Use the first word as the prefix guess.
2. Compare letter by letter with every other word.
3. When letters differ, cut the prefix shorter.
4. If prefix becomes empty, stop early.
5. After all words, return the prefix left.
""",
    "0015_3sum": """# How We Solve 3Sum

Find three numbers in a list that add to zero.

## Steps

1. Sort the list so duplicates sit together.
2. Pick a first number (i).
3. Use two fingers (left, right) on the rest to hunt for two more numbers.
4. If sum is zero, save the triple and skip duplicate values.
5. If sum is too small, move left up; if too big, move right down.
6. Return all unique triples.
""",
    "0016_3sum_closest": """# How We Solve 3Sum Closest

Find three numbers whose sum is **closest** to a target.

## Steps

1. Sort the list.
2. Pick a first number (i).
3. Use left and right fingers on the rest.
4. Track the sum closest to target so far.
5. Move fingers like 3Sum based on whether sum is too small or too big.
6. Return the closest sum.
""",
    "0017_letter_combinations_of_a_phone_number": """# How We Solve Letter Combinations of a Phone Number

Phone keys map to letters (2->abc). Build all words from digits like "23".

## Steps

1. If digits are empty, return nothing.
2. Start with an empty word being built.
3. For each digit, try every letter on that key.
4. Add a letter, go to the next digit, then backtrack (remove letter).
5. When all digits are used, save the word.
6. Return all saved words.
""",
    "0018_4sum": """# How We Solve 4Sum

Find four numbers that add to a target (like 3Sum with one more loop).

## Steps

1. Sort the list.
2. Pick first number i, then second number j.
3. Use left and right fingers for the last two numbers.
4. Skip duplicate i and j values.
5. When sum matches target, save and skip duplicate left/right values.
6. Return all unique quadruples.
""",
    "0019_remove_nth_node_from_end_of_list": """# How We Solve Remove Nth Node From End of List

Remove the node n steps from the **end** of a linked list.

## Steps

1. Put a dummy head before the list (helps when removing the first node).
2. Move a fast finger n steps ahead.
3. Move fast and slow together until fast reaches the end.
4. Slow is now just before the node to remove.
5. Skip that node by linking around it.
6. Return the list after dummy.
""",
    "0020_valid_parentheses": """# How We Solve Valid Parentheses

Check if brackets match: (), [], {}.

## Steps

1. Use a stack (a pile you only touch on top).
2. For an open bracket, push it on the pile.
3. For a close bracket, pop and check it matches the opener.
4. If pile is empty when you need to pop, it is invalid.
5. At the end, pile must be empty.
6. Return true or false.
""",
    "0021_merge_two_sorted_lists": """# How We Solve Merge Two Sorted Lists

Merge two sorted linked lists into one sorted list.

## Steps

1. Make a dummy head for the answer list.
2. Compare the front nodes of both lists.
3. Attach the smaller node to the answer and move that list forward.
4. Repeat until one list is empty.
5. Attach the rest of the non-empty list.
6. Return the merged list after dummy.
""",
    "0022_generate_parentheses": """# How We Solve Generate Parentheses

Make all valid bracket strings with n pairs, like n=3 -> "((()))", etc.

## Steps

1. Start with an empty string and open=0, close=0.
2. If open < n, you may add "(".
3. If close < open, you may add ")".
4. When length is 2*n, save the string.
5. Backtrack: try choices, then undo and try others.
6. Return all saved strings.
""",
    "0023_merge_k_sorted_lists": """# How We Solve Merge k Sorted Lists

Merge many sorted linked lists into one sorted list.

## Steps

1. Put the head of every non-empty list into a min-heap (smallest first).
2. Pop the smallest node and attach it to the answer.
3. If that node has a next, push the next into the heap.
4. Repeat until the heap is empty.
5. Return the merged list.
""",
    "0024_swap_nodes_in_pairs": """# How We Solve Swap Nodes in Pairs

Swap every two nodes: 1->2->3->4 becomes 2->1->4->3.

## Steps

1. Use a dummy node before the head.
2. If two nodes exist, swap their links.
3. Move to the next unswapped pair.
4. Repeat until fewer than two nodes remain.
5. Return the list after dummy.
""",
    "0025_reverse_nodes_in_k_group": """# How We Solve Reverse Nodes in k-Group

Reverse every group of k nodes; leave a short tail unchanged.

## Steps

1. Walk k steps to find the end of the current group.
2. If fewer than k nodes remain, stop.
3. Reverse the k nodes inside the group.
4. Hook the reversed block back into the list.
5. Move to the next group and repeat.
6. Return the new head.
""",
    "0026_remove_duplicates_from_sorted_array": """# How We Solve Remove Duplicates from Sorted Array

Keep only unique numbers at the front of a sorted array.

## Steps

1. Use a write finger starting at 1 (index 0 stays).
2. Read each next number with a read finger.
3. If it is different from the last kept number, write it and move write forward.
4. Skip duplicates because the list is sorted.
5. Return how many unique numbers you kept.
""",
    "0027_remove_element": """# How We Solve Remove Element

Remove all copies of a value val from an array.

## Steps

1. Use a write finger at the start.
2. Read each number.
3. If it is not val, copy it to write and move write forward.
4. If it is val, skip it.
5. Return how many numbers remain.
""",
    "0028_find_the_index_of_the_first_occurrence_in_a_string": """# How We Solve Find the Index of the First Occurrence in a String

Find where a small word (needle) first appears inside a big word (haystack).

## Steps

1. If needle is empty, answer is 0.
2. Try every start position in haystack where needle could fit.
3. Compare needle letter by letter at that spot.
4. If all letters match, return that start index.
5. If none match, return -1.
""",
    "0029_divide_two_integers": """# How We Solve Divide Two Integers

Divide without using * or / (use bits instead).

## Steps

1. Handle overflow special case (MIN / -1).
2. Remember if the answer should be negative.
3. Work with positive absolute values.
4. For each bit position, if dividend is big enough, subtract (divisor << bit) and add (1 << bit) to quotient.
5. Return quotient with the correct sign.
""",
    "0030_substring_with_concatenation_of_all_words": """# How We Solve Substring with Concatenation of All Words

Find starts where s is made of all given words glued together (same length words).

## Steps

1. Count how many times each word is needed.
2. Try each possible alignment offset (0 .. wordLength-1).
3. Slide a window word-by-word across s.
4. Track word counts in the current window.
5. If a bad word appears, reset the window.
6. When window uses all words correctly, save the start index.
7. Return all start indexes (sorted).
""",
    "0031_next_permutation": """# How We Solve Next Permutation

Rearrange numbers into the **next bigger** order (like 123 -> 132).

## Steps

1. Find the rightmost place where a number is smaller than its neighbor to the right.
2. If none, reverse the whole list (wrap to smallest order).
3. Find the smallest number to the right that is bigger than that place.
4. Swap them.
5. Reverse everything after that place to get the smallest tail.
6. The array is now the next permutation.
""",
    "0032_longest_valid_parentheses": """# How We Solve Longest Valid Parentheses

Find the longest valid () substring.

## Steps

1. Use a stack of indexes; push -1 as a starter fence.
2. For "(", push its index.
3. For ")", pop a match; if stack empty, push current index as new fence.
4. Else length = i - stack top; keep the best length.
5. Return the best length.
""",
    "0033_search_in_rotated_sorted_array": """# How We Solve Search in Rotated Sorted Array

A sorted list was rotated. Find target index or -1.

## Steps

1. Use left and right binary search pointers.
2. Look at middle; if it is target, done.
3. Decide which half is sorted (left half or right half).
4. Check if target lives in the sorted half.
5. Move left/right to search that half, else search the other half.
6. Return index or -1.
""",
    "0034_find_first_and_last_position_of_element_in_sorted_array": """# How We Solve Find First and Last Position of Element in Sorted Array

Find first and last index of target in a sorted array.

## Steps

1. Binary search for the **first** position where nums[i] >= target.
2. If not found or not equal to target, return [-1, -1].
3. Binary search for the **first** position where nums[i] > target.
4. Last index is that position minus one.
5. Return [first, last].
""",
    "0035_search_insert_position": """# How We Solve Search Insert Position

Find where to insert target in a sorted array (or existing index).

## Steps

1. Binary search with left=0, right=n.
2. Look at middle.
3. If nums[mid] < target, search right half (left = mid+1).
4. Else search left half (right = mid).
5. When done, left is the insert position.
6. Return left.
""",
    "0036_valid_sudoku": """# How We Solve Valid Sudoku

Check if a 9x9 Sudoku board has no repeats in rows, columns, or 3x3 boxes.

## Steps

1. Make empty sets for each row, column, and box.
2. Walk every cell.
3. Skip "." empty cells.
4. If the digit is already in its row, column, or box, return false.
5. Otherwise add the digit to those three sets.
6. If you finish with no trouble, return true.
""",
    "0037_sudoku_solver": """# How We Solve Sudoku Solver

Fill a Sudoku board so every row, column, and box has 1-9 once.

## Steps

1. Record which digits are already used in each row, column, and box.
2. Make a list of empty cells.
3. Try digits 1-9 in the next empty cell.
4. If a digit is allowed, place it and go to the next empty cell.
5. If stuck, undo (backtrack) and try another digit.
6. When all cells filled, the puzzle is solved.
""",
    "0038_count_and_say": """# How We Solve Count and Say

Each term describes the previous term (run-length encoding). n=1 -> "1", n=2 -> "11", etc.

## Steps

1. Start with term = "1".
2. For each step until n, build the next term.
3. Walk the current term and count same digits in a row.
4. Write count + digit for each group.
5. That new string becomes the next term.
6. Return the final term.
""",
    "0039_combination_sum": """# How We Solve Combination Sum

Pick numbers (can reuse) that add to target.

## Steps

1. Sort candidates (optional but tidy).
2. Try building a path with backtracking.
3. If remaining target hits 0, save the path.
4. If remaining < 0, stop this branch.
5. For each candidate, add it and call again starting at same index (reuse allowed).
6. Backtrack by removing the last pick.
7. Return all combinations.
""",
    "0040_combination_sum_ii": """# How We Solve Combination Sum II

Pick numbers (each once) that add to target; no duplicate combos.

## Steps

1. Sort candidates so duplicates are together.
2. Backtrack like Combination Sum.
3. Skip using the same number twice at the same depth (duplicate skip rule).
4. Each number used at most once (next start is i+1).
5. Save paths that hit target exactly.
6. Return all unique combinations.
""",
    "0041_first_missing_positive": """# How We Solve First Missing Positive

Find the smallest missing **positive** integer (1, 2, 3, ...).

## Steps

1. Only numbers 1..n matter for an array of length n.
2. Try to put each value v into index v-1 by swapping.
3. Swap only when v is in range and not already in the right place.
4. Scan indexes: first place where nums[i] != i+1 gives the answer.
5. If all match, answer is n+1.
""",
    "0042_trapping_rain_water": """# How We Solve Trapping Rain Water

Bars trap rain between them. Count total water.

## Steps

1. Put left finger at start and right finger at end.
2. Track tallest bar seen on left and on right.
3. Move the finger at the **shorter** side inward.
4. If the bar is shorter than its side max, water += (side max - bar height).
5. Else update that side's max.
6. Repeat until fingers meet; return total water.
""",
    "0043_multiply_strings": """# How We Solve Multiply Strings

Multiply big numbers given as strings (no built-in big math).

## Steps

1. If either number is "0", answer is "0".
2. Make an array big enough to hold all digit results.
3. Multiply each digit pair like on paper.
4. Add into the right slot and carry to the left slot.
5. Turn the array into a string and remove leading zeros.
6. Return the final string.
""",
    "0044_wildcard_matching": """# How We Solve Wildcard Matching

Does a pattern match a word? `?` = one any letter, `*` = any letters (even none).

## Steps

1. Build a yes/no table for every prefix of word vs pattern.
2. Empty word matches empty pattern.
3. A leading `*` can match empty at the start.
4. Fill the table: `*` can skip itself or eat another letter.
5. `?` or same letter copies the diagonal smaller yes.
6. Bottom-right cell is the final answer.
""",
    "0045_jump_game_ii": """# How We Solve Jump Game II

Jump from index 0 to the end in the fewest jumps. Each step you can jump up to nums[i].

## Steps

1. Track the farthest index you can reach.
2. Track the end of the current jump window.
3. Walk index by index (stop before the last spot).
4. Update farthest with i + nums[i].
5. When you hit the window end, count one jump and open a new window at farthest.
6. Return the jump count.
""",
    "0046_permutations": """# How We Solve Permutations

Make every order of the numbers (all permutations).

## Steps

1. Keep a path list and a used[] checklist.
2. If path is full, save a copy in the answer list.
3. Try each number index from left to right.
4. Skip numbers already used.
5. Mark used, add to path, go deeper, then undo (backtrack).
6. Return all saved orders.
""",
    "0047_permutations_ii": """# How We Solve Permutations II

Make all unique orders when the list can have duplicate numbers.

## Steps

1. Sort the list so duplicates sit together.
2. Use path + used[] backtracking like Permutations.
3. Skip a duplicate if the same number right before it is unused (same-level dup rule).
4. When path is full, save it.
5. Backtrack and try other choices.
6. Return all unique permutations.
""",
    "0048_rotate_image": """# How We Solve Rotate Image

Turn a square grid 90 degrees clockwise **in place**.

## Steps

1. Transpose: swap matrix[i][j] with matrix[j][i] for i < j.
2. Reverse each row left to right.
3. The matrix is now rotated 90° clockwise.
""",
    "0049_group_anagrams": """# How We Solve Group Anagrams

Put words that use the same letters into the same group.

## Steps

1. For each word, sort its letters to make a key.
2. Words with the same key are anagrams — put them in one bucket.
3. Sort words inside each bucket alphabetically.
4. Order buckets by where their words first appear in the input.
5. Return the list of buckets.
""",
    "0050_powx_n": """# How We Solve Pow(x, n)

Compute x raised to the power n quickly.

## Steps

1. If n is 0, the answer is 1.
2. If n is negative, use 1/x and make n positive.
3. Keep a running power of x (square it each step).
4. Look at n in binary: if the last bit is 1, multiply the answer by the current power.
5. Shift n right and repeat until n is 0.
6. Return the answer.
""",
    "0051_n_queens": """# How We Solve N-Queens

Place n queens on an n×n board so no two attack each other.

## Steps

1. Place queens one row at a time.
2. For each row, try every column.
3. Skip a column if another queen shares the same column or diagonal.
4. When a row is filled, save the board and backtrack.
5. Remove the queen and try the next column.
6. Return all valid boards.
""",
    "0052_n_queens_ii": """# How We Solve N-Queens II

Count how many ways to place n queens on an n×n board safely.

## Steps

1. Place queens one row at a time.
2. For each row, try every column.
3. Skip a column if another queen shares the same column or diagonal.
4. When all rows are filled, add 1 to the count.
5. Backtrack and try other columns.
6. Return the total count.
""",
    "0053_maximum_subarray": """# How We Solve Maximum Subarray

Find the contiguous chunk of numbers with the biggest sum.

## Steps

1. Start with the first number as both the current sum and best sum.
2. Move to the next number.
3. Either extend the current chunk (add the number) or start fresh at this number.
4. Update the best sum if the current chunk is bigger.
5. Repeat until the end of the list.
6. Return the best sum.
""",
    "0054_spiral_matrix": """# How We Solve Spiral Matrix

Walk through a grid in a clockwise spiral and collect the numbers.

## Steps

1. Track the top, bottom, left, and right edges of the remaining grid.
2. Go left to right along the top row, then move the top edge down.
3. Go top to bottom along the right column, then move the right edge left.
4. If rows remain, go right to left along the bottom row, then move the bottom edge up.
5. If columns remain, go bottom to top along the left column, then move the left edge right.
6. Repeat until all cells are visited, then return the collected numbers.
""",
    "0055_jump_game": """# How We Solve Jump Game

Check if you can reach the last index by jumping from each spot.

## Steps

1. Keep track of the farthest index you can reach so far.
2. Walk through each index in order.
3. If the current index is beyond the farthest reach, return false.
4. Update the farthest reach using the current jump length.
5. If you can visit every index, return true.
""",
    "0056_merge_intervals": """# How We Solve Merge Intervals

Combine overlapping time ranges into bigger ranges.

## Steps

1. Sort intervals by their start time.
2. Start with the first interval in a merged list.
3. For each next interval, check if it overlaps the last merged one.
4. If it overlaps, stretch the last interval's end to the bigger end time.
5. If it does not overlap, add it as a new interval.
6. Return the merged list.
""",
    "0057_insert_interval": """# How We Solve Insert Interval

Add a new time range into a sorted list and merge overlaps.

## Steps

1. Copy all intervals that end before the new one starts.
2. Merge every interval that overlaps the new one.
3. Add the merged new interval once.
4. Copy all remaining intervals that start after it.
5. Return the updated list.
""",
    "0058_length_of_last_word": """# How We Solve Length of Last Word

Find how many letters are in the last word of a sentence.

## Steps

1. Start at the end of the string.
2. Skip trailing spaces.
3. Count characters while they are not spaces.
4. Stop when you hit a space or the start.
5. Return the count.
""",
    "0059_spiral_matrix_ii": """# How We Solve Spiral Matrix II

Fill an n×n grid with numbers 1 to n² in clockwise spiral order.

## Steps

1. Track top, bottom, left, and right edges of the empty area.
2. Fill the top row left to right, then move the top edge down.
3. Fill the right column top to bottom, then move the right edge left.
4. Fill the bottom row right to left, then move the bottom edge up.
5. Fill the left column bottom to top, then move the left edge right.
6. Repeat with the next number until the grid is full.
""",
    "0060_permutation_sequence": """# How We Solve Permutation Sequence

Find the k-th permutation of numbers 1 through n in sorted order.

## Steps

1. List the numbers 1 to n and precompute factorials.
2. Convert k to zero-based (subtract 1).
3. From the highest place value down, pick the index = k ÷ factorial.
4. Append that number and remove it from the list.
5. Update k to k mod factorial and continue.
6. Join the chosen digits into the answer string.
""",
    "0061_rotate_list": """# How We Solve Rotate List

Move the last k nodes of a linked list to the front.

## Steps

1. If the list is empty or has one node, return it.
2. Find the tail and count the list length.
3. Connect the tail to the head to form a circle.
4. Reduce k using k mod length.
5. Walk length − k steps to find the new tail.
6. Break the circle after the new tail and return the new head.
""",
    "0062_unique_paths": """# How We Solve Unique Paths

Count paths from top-left to bottom-right moving only right or down.

## Steps

1. Use one row of counts, all starting at 1.
2. For each row below the first, update each cell.
3. Each cell adds the count from the cell above and the cell to the left.
4. The first row and column stay 1.
5. Return the bottom-right count in the row.
""",
    "0063_unique_paths_ii": """# How We Solve Unique Paths II

Count paths on a grid with blocked cells.

## Steps

1. If the start cell is blocked, return 0.
2. Keep one row of path counts, starting with 1 at the top-left.
3. For each row, zero out blocked cells.
4. For open cells, add the count from the left (same row update).
5. Also zero the first column when that row's start is blocked.
6. Return the bottom-right count.
""",
    "0064_minimum_path_sum": """# How We Solve Minimum Path Sum

Find the cheapest path from top-left to bottom-right (only right or down).

## Steps

1. Use the grid itself to store the best cost so far.
2. Start at the top-left cell (cost stays the same).
3. Fill the first row by adding the cell to the left.
4. Fill the first column by adding the cell above.
5. For other cells, add the smaller of the costs from above or the left.
6. Return the bottom-right cell.
""",
    "0065_valid_number": """# How We Solve Valid Number

Check if a string is a valid decimal number (with optional exponent).

## Steps

1. Scan the string one character at a time.
2. Track whether we have seen a digit, a dot, and an exponent.
3. Digits are always allowed; signs only after start or after e/E.
4. Only one dot, and no dot after an exponent.
5. Only one exponent, and it must come after at least one digit.
6. The string is valid only if it ends with at least one digit seen.
""",
    "0066_plus_one": """# How We Solve Plus One

Add 1 to a number stored as an array of digits.

## Steps

1. Start from the last digit.
2. If it is less than 9, add 1 and return.
3. If it is 9, set it to 0 and carry to the left.
4. If every digit was 9, put a 1 at the front.
5. Return the updated digit array.
""",
    "0067_add_binary": """# How We Solve Add Binary

Add two binary strings and return the sum as binary.

## Steps

1. Start from the rightmost bits of both strings.
2. Add the bits plus any carry.
3. Write the remainder (0 or 1) and update the carry.
4. Move left until both strings and carry are done.
5. Reverse the collected bits to get the answer.
""",
    "0068_text_justification": """# How We Solve Text Justification

Format words into lines of exact width with justified spacing.

## Steps

1. Greedily pack as many words as fit on each line.
2. If it is the last line or only one word, left-justify with spaces at the end.
3. Otherwise compute extra spaces to spread between words.
4. Give leftover spaces to the leftmost gaps first.
5. Build each line and repeat until all words are used.
""",
    "0069_sqrtx": """# How We Solve Sqrt(x)

Find the integer square root (floor of √x).

## Steps

1. Handle small x (0 or 1) directly.
2. Binary search between 2 and x/2.
3. Compare mid×mid with x.
4. Move the search left or right.
5. Return the largest mid whose square is ≤ x.
""",
    "0070_climbing_stairs": """# How We Solve Climbing Stairs

Count ways to climb n stairs taking 1 or 2 steps at a time.

## Steps

1. One stair has 1 way; two stairs have 2 ways.
2. Keep the count for the previous two stair totals.
3. Each new total is the sum of the last two.
4. Step forward until you reach n.
5. Return that total.
""",
    "0071_simplify_path": """# How We Solve Simplify Path

Turn a Unix-style path into its shortest absolute form.

## Steps

1. Split the path by `/`.
2. Skip empty parts and `.`.
3. On `..`, pop the last folder if the stack is not empty.
4. Otherwise push the folder name.
5. Join with `/` and put a `/` at the front.
""",
    "0072_edit_distance": """# How We Solve Edit Distance

Find the fewest edits to turn one word into another.

## Steps

1. Build a table of costs for empty prefixes.
2. For each pair of characters, if they match, copy the diagonal cost.
3. If they differ, take 1 plus the minimum of delete, insert, or replace.
4. Use one row at a time to save space.
5. Return the bottom-right cost.
""",
    "0073_set_matrix_zeroes": """# How We Solve Set Matrix Zeroes

If a cell is 0, set its whole row and column to 0.

## Steps

1. Remember if the first row or column should become all zeros.
2. Use the first row and column as markers for other zeros.
3. Scan the rest of the grid and mark rows/columns that contain a zero.
4. Zero out marked rows and columns using the markers.
5. Fix the first row and column last if needed.
""",
    "0074_search_a_2d_matrix": """# How We Solve Search a 2D Matrix

Search a sorted matrix where each row and column is ordered.

## Steps

1. Start at the top-right corner.
2. If the cell equals the target, return true.
3. If the cell is bigger, move left.
4. If the cell is smaller, move down.
5. Stop when you leave the grid; return false.
""",
    "0075_sort_colors": """# How We Solve Sort Colors

Sort an array of 0s, 1s, and 2s in one pass.

## Steps

1. Keep three pointers: low, mid, and high.
2. If mid sees 0, swap with low and move both forward.
3. If mid sees 1, just move mid forward.
4. If mid sees 2, swap with high and move high back.
5. Repeat until mid passes high.
""",
    "0076_minimum_window_substring": """# How We Solve Minimum Window Substring

Find the smallest substring of s that contains all letters of t.

## Steps

1. Count how many of each letter t needs.
2. Expand the window right, updating counts.
3. When all needed letters are satisfied, try shrinking from the left.
4. Save the smallest valid window seen.
5. Return that substring, or empty if none exists.
""",
    "0077_combinations": """# How We Solve Combinations

List all k-number groups from 1 to n.

## Steps

1. Build combinations with backtracking.
2. Add numbers in increasing order.
3. Stop when the path has k numbers.
4. Skip choices that cannot still fill k slots.
5. Return all combinations found.
""",
    "0078_subsets": """# How We Solve Subsets

List every subset of the given numbers.

## Steps

1. Start with the empty subset.
2. For each number, copy every existing subset and add the number.
3. Append those new subsets to the list.
4. Repeat for all numbers.
5. Return the full power set.
""",
    "0079_word_search": """# How We Solve Word Search

Check if a word exists in a letter grid by adjacent moves.

## Steps

1. Try starting a search from every cell.
2. Use DFS to match the next letter in each direction.
3. Mark visited cells temporarily so they are not reused.
4. Backtrack and unmark if the path fails.
5. Return true if any start works.
""",
    "0080_remove_duplicates_from_sorted_array_ii": """# How We Solve Remove Duplicates from Sorted Array II

Keep at most two copies of each value in a sorted array.

## Steps

1. If length is 2 or less, return the length.
2. The first two spots are always kept.
3. For each later value, compare with the value two spots back.
4. If different, write it to the next open spot.
5. Return how many spots were used.
""",
    "0081_search_in_rotated_sorted_array_ii": """# How We Solve Search in Rotated Sorted Array II

Find a target in a rotated sorted array that may have duplicates.

## Steps

1. Binary search with left and right pointers.
2. If the middle matches the target, return true.
3. If left, middle, and right are equal, shrink both ends.
4. Otherwise pick the sorted half that could contain the target.
5. Return false if the search range is empty.
""",
    "0082_remove_duplicates_from_sorted_list_ii": """# How We Solve Remove Duplicates from Sorted List II

Remove every value that appears more than once in a sorted list.

## Steps

1. Use a dummy node before the head.
2. Walk with previous and current pointers.
3. When current equals the next value, skip the whole duplicate group.
4. Otherwise advance previous.
5. Return the list after the dummy.
""",
    "0083_remove_duplicates_from_sorted_list": """# How We Solve Remove Duplicates from Sorted List

Keep only one copy of each value in a sorted list.

## Steps

1. Start at the head.
2. If current equals next, skip the next node.
3. Otherwise move forward one step.
4. Repeat until the end.
5. Return the head.
""",
    "0084_largest_rectangle_in_histogram": """# How We Solve Largest Rectangle in Histogram

Find the largest rectangle area under a histogram.

## Steps

1. Use a monotonic stack of rising bar indexes.
2. Add a zero-height bar at the end as a stopper.
3. When the current bar is shorter, pop taller bars.
4. For each pop, width is the span to the new stack top.
5. Track the maximum height × width.
""",
    "0085_maximal_rectangle": """# How We Solve Maximal Rectangle

Find the largest rectangle of ones in a binary matrix.

## Steps

1. Treat each row as the base of a histogram.
2. Grow heights for consecutive ones; reset on zeros.
3. For every row, run the histogram largest-rectangle algorithm.
4. Keep the best area seen across all rows.
5. Return that area.
""",
    "0086_partition_list": """# How We Solve Partition List

Reorder a list so values below x come before values x or larger.

## Steps

1. Make two lists: before and after.
2. Put each node into before if its value is less than x.
3. Otherwise put it into after.
4. Cut the after list and attach it after before.
5. Return the head of the before list.
""",
    "0087_scramble_string": """# How We Solve Scramble String

Check if one string can be a scramble of another.

## Steps

1. Equal strings are scrambles; different letter counts are not.
2. Try every split of the string.
3. Check the no-swap case for both parts recursively.
4. Check the swap case for both parts recursively.
5. Memoize results so repeated pairs are not recomputed.
""",
    "0088_merge_sorted_array": """# How We Solve Merge Sorted Array

Merge two sorted arrays into nums1 in place.

## Steps

1. Start from the end of both filled ranges.
2. Compare the larger of nums1[i] and nums2[j].
3. Write the larger value into the last open slot of nums1.
4. Keep going until nums2 is empty.
5. nums1 then holds the full sorted merge.
""",
    "0089_gray_code": """# How We Solve Gray Code

Build an n-bit Gray code sequence.

## Steps

1. There are 2^n codes for bit length n.
2. For each index i from 0 to 2^n − 1, compute i XOR (i shifted right by 1).
3. Collect those values in order.
4. Neighboring codes differ by exactly one bit.
5. Return the list.
""",
    "0090_subsets_ii": """# How We Solve Subsets II

List unique subsets when the input may have duplicates.

## Steps

1. Sort the numbers so duplicates sit together.
2. Backtrack and always save the current path.
3. Skip a number if it equals the previous one at the same depth.
4. Choose a number, recurse, then undo the choice.
5. Return all unique subsets.
""",
    "0091_decode_ways": """# How We Solve Decode Ways

Count how many ways a digit string can map to letters A–Z.

## Steps

1. A leading zero cannot be decoded, so return 0.
2. Keep counts for the previous one and two positions.
3. A single non-zero digit can extend the previous count.
4. A valid two-digit number (10–26) can also extend the count before that.
5. Walk the string and return the final count.
""",
    "0092_reverse_linked_list_ii": """# How We Solve Reverse Linked List II

Reverse only the part of a list between two positions.

## Steps

1. Put a dummy node before the head.
2. Walk to the node just before the left position.
3. Reverse the next (right − left) links by inserting at the front of that section.
4. Leave the rest of the list alone.
5. Return the list after the dummy.
""",
    "0093_restore_ip_addresses": """# How We Solve Restore IP Addresses

Split a digit string into all valid IP addresses.

## Steps

1. Build an IP with exactly four parts.
2. Each part is 1–3 digits and its value is at most 255.
3. Skip parts with leading zeros unless the part is just 0.
4. Backtrack through all valid splits.
5. Join successful parts with dots.
""",
    "0094_binary_tree_inorder_traversal": """# How We Solve Binary Tree Inorder Traversal

Visit nodes in left → root → right order.

## Steps

1. Use a stack and start at the root.
2. Keep going left, pushing nodes onto the stack.
3. Pop a node, record its value, then go right.
4. Repeat until the stack and current node are both empty.
5. Return the recorded values.
""",
    "0095_unique_binary_search_trees_ii": """# How We Solve Unique Binary Search Trees II

Build every unique BST that stores values 1 through n.

## Steps

1. For a number range, try each value as the root.
2. Build all left subtrees from smaller values.
3. Build all right subtrees from larger values.
4. Pair every left tree with every right tree.
5. Collect all roots formed that way.
""",
    "0096_unique_binary_search_trees": """# How We Solve Unique Binary Search Trees

Count unique BSTs that store values 1 through n.

## Steps

1. Let dp[i] be the number of unique trees with i nodes.
2. An empty tree counts as 1.
3. For each size, try each possible root.
4. Multiply left-side counts by right-side counts.
5. Sum those products to get dp[n].
""",
    "0097_interleaving_string": """# How We Solve Interleaving String

Check if s3 is made by merging s1 and s2 in order.

## Steps

1. Lengths must add up; otherwise return false.
2. Use a one-row DP over s2 prefixes.
3. Mark whether the current prefixes of s1 and s2 form the matching prefix of s3.
4. A cell is true if the next letter comes from s1 or from s2 legally.
5. Return the final DP value.
""",
    "0098_validate_binary_search_tree": """# How We Solve Validate Binary Search Tree

Check whether a tree follows BST ordering rules.

## Steps

1. Walk the tree with a low and high bound for each node.
2. The node value must sit strictly between those bounds.
3. The left child inherits a tighter high bound.
4. The right child inherits a tighter low bound.
5. Empty nodes are valid.
""",
    "0099_recover_binary_search_tree": """# How We Solve Recover Binary Search Tree

Fix a BST where exactly two node values were swapped.

## Steps

1. Walk the tree in order using a stack.
2. Watch for places where the previous value is bigger than the current one.
3. The first such previous node is one swapped value.
4. The later current node is the other swapped value.
5. Swap those two values to restore the BST.
""",
    "0100_same_tree": """# How We Solve Same Tree

Check if two binary trees have the same structure and values.

## Steps

1. Two empty trees are the same.
2. If only one is empty, they differ.
3. If root values differ, they differ.
4. Compare left subtrees and right subtrees recursively.
5. Both sides must match.
""",
    "0101_symmetric_tree": """# How We Solve Symmetric Tree

Check if a tree is a mirror of itself.

## Steps

1. Compare the left and right children of the root.
2. Two empty nodes match.
3. Values must be equal.
4. Compare outer children with outer children.
5. Compare inner children with inner children.
""",
    "0102_binary_tree_level_order_traversal": """# How We Solve Binary Tree Level Order Traversal

List node values level by level from top to bottom.

## Steps

1. Start a queue with the root.
2. For each level, process exactly the nodes currently in the queue.
3. Record their values left to right.
4. Enqueue their children for the next level.
5. Collect every level into the answer.
""",
    "0103_binary_tree_zigzag_level_order_traversal": """# How We Solve Binary Tree Zigzag Level Order Traversal

List levels left-to-right, then right-to-left, alternating.

## Steps

1. Do a normal BFS level order.
2. Keep a direction flag.
3. Reverse every other level before saving it.
4. Flip the flag after each level.
5. Return the zigzag list of levels.
""",
    "0104_maximum_depth_of_binary_tree": """# How We Solve Maximum Depth of Binary Tree

Find how many levels the tree has.

## Steps

1. An empty tree has depth 0.
2. Recurse on the left and right children.
3. Take the larger of those two depths.
4. Add 1 for the current node.
5. Return that total.
""",
    "0105_construct_binary_tree_from_preorder_and_inorder_traversal": """# How We Solve Construct Binary Tree from Preorder and Inorder Traversal

Rebuild a tree from preorder and inorder lists.

## Steps

1. The next preorder value is the current root.
2. Find that value in the inorder list to split left and right ranges.
3. Build the left subtree from the left range.
4. Build the right subtree from the right range.
5. Return the connected root.
""",
    "0106_construct_binary_tree_from_inorder_and_postorder_traversal": """# How We Solve Construct Binary Tree from Inorder and Postorder Traversal

Rebuild a tree from inorder and postorder lists.

## Steps

1. The last unused postorder value is the current root.
2. Find that value in the inorder list to split ranges.
3. Build the right subtree first.
4. Then build the left subtree.
5. Return the connected root.
""",
    "0107_binary_tree_level_order_traversal_ii": """# How We Solve Binary Tree Level Order Traversal II

List levels from bottom to top.

## Steps

1. Run a normal BFS level order.
2. Collect each level top to bottom.
3. Reverse the list of levels.
4. Return the reversed list.
""",
    "0108_convert_sorted_array_to_binary_search_tree": """# How We Solve Convert Sorted Array to Binary Search Tree

Turn a sorted array into a height-balanced BST.

## Steps

1. Pick the middle value as the root (use the upper middle).
2. Recursively build the left half as the left subtree.
3. Recursively build the right half as the right subtree.
4. Connect them to the root.
5. Repeat until the range is empty.
""",
    "0109_convert_sorted_list_to_binary_search_tree": """# How We Solve Convert Sorted List to Binary Search Tree

Turn a sorted linked list into a height-balanced BST.

## Steps

1. Copy the list values into an array.
2. Pick the upper middle as the root.
3. Build left and right halves recursively.
4. Attach those subtrees to the root.
5. Return the balanced tree.
""",
    "0110_balanced_binary_tree": """# How We Solve Balanced Binary Tree

Check that every node's left and right heights differ by at most one.

## Steps

1. Compute height bottom-up.
2. If a subtree is already unbalanced, return a sentinel.
3. If left and right heights differ by more than 1, mark unbalanced.
4. Otherwise return 1 plus the larger child height.
5. The tree is balanced if the root height is not the sentinel.
""",
    "0111_minimum_depth_of_binary_tree": """# How We Solve Minimum Depth of Binary Tree

Find the shortest root-to-leaf path. A missing child does not count as a leaf.

## Steps

1. Empty tree has depth 0.
2. If only the right child exists, recurse on the right.
3. If only the left child exists, recurse on the left.
4. Otherwise take 1 plus the smaller of the two child depths.
5. Return that depth.
""",
    "0112_path_sum": """# How We Solve Path Sum

Ask whether any root-to-leaf path sums to the target.

## Steps

1. Empty tree has no path.
2. At a leaf, check whether the remaining sum equals the leaf value.
3. Otherwise subtract the current value and try left and right.
4. Succeed if either subtree finds a path.
5. Return that boolean answer.
""",
    "0113_path_sum_ii": """# How We Solve Path Sum II

Collect every root-to-leaf path that sums to the target.

## Steps

1. DFS with the remaining sum and the path so far.
2. Push the current node value onto the path.
3. At a leaf whose value matches the remaining sum, copy the path.
4. Otherwise recurse into both children with a reduced remaining sum.
5. Pop after exploring so sibling branches share the same buffer.
""",
    "0114_flatten_binary_tree_to_linked_list": """# How We Solve Flatten Binary Tree to Linked List

Rewrite the tree in place into a preorder right spine.

## Steps

1. Recursively flatten the left and right subtrees.
2. If there is a left subtree, find its rightmost node.
3. Attach the original right subtree after that rightmost node.
4. Move the left subtree to the right and clear left.
5. Repeat until every node only has a right child.
""",
    "0115_distinct_subsequences": """# How We Solve Distinct Subsequences

Count how many subsequences of `s` equal `t` with one-dimensional DP.

## Steps

1. Let `dp[j]` be ways to form the first `j` characters of `t`.
2. Seed `dp[0] = 1` for the empty prefix.
3. Scan each character of `s`.
4. Walk `t` backwards; when characters match, add `dp[j]` into `dp[j+1]`.
5. Return `dp[len(t)]`.
""",
    "0116_populating_next_right_pointers_in_each_node": """# How We Solve Populating Next Right Pointers in Each Node

Link every node to its right neighbor on the same level in a perfect tree.

## Steps

1. Start a level list with the root.
2. Walk the level left to right and set each node's `next`.
3. Build the next level from left and right children.
4. Repeat until there are no more children.
5. Return the original root.
""",
    "0117_populating_next_right_pointers_in_each_node_ii": """# How We Solve Populating Next Right Pointers in Each Node II

Same level linking as the perfect-tree version, but children may be missing.

## Steps

1. Process the tree level by level.
2. On each level, connect consecutive nodes with `next`.
3. Collect existing left and right children for the next level.
4. Continue until a level is empty.
5. Return the root with all `next` pointers filled.
""",
    "0118_pascals_triangle": """# How We Solve Pascal's Triangle

Build `numRows` rows where each entry is the sum of the two above it.

## Steps

1. Start with an empty list of rows.
2. For row `i`, place `1` at both ends.
3. Fill interior cells from the previous row's adjacent pair.
4. Append the finished row.
5. Return all rows.
""",
    "0119_pascals_triangle_ii": """# How We Solve Pascal's Triangle II

Return only the 0-indexed row, updating one array in place.

## Steps

1. Start with `[1]`.
2. For each next row index, append a trailing `1`.
3. Update interior cells right-to-left so older values stay available.
4. Each update adds the previous cell into the current cell.
5. Return the finished row.
""",
    "0120_triangle": """# How We Solve Triangle

Find the minimum path sum from top to bottom with bottom-up DP.

## Steps

1. Copy the bottom row as the working DP array.
2. Move upward one row at a time.
3. For each cell, add the smaller of the two children below it.
4. Continue until only the top cell remains.
5. Return that value as the minimum total.
""",
    "0121_best_time_to_buy_and_sell_stock": """# How We Solve Best Time to Buy and Sell Stock

One buy and one sell: track the lowest price so far and the best profit.

## Steps

1. Keep the minimum price seen so far.
2. For each later price, compute price minus that minimum.
3. Update the best profit when the gap is larger.
4. Update the minimum when a cheaper day appears.
5. Return the best profit (or 0 if none).
""",
    "0122_best_time_to_buy_and_sell_stock_ii": """# How We Solve Best Time to Buy and Sell Stock II

Unlimited trades: take every upward day-to-day gain.

## Steps

1. Walk consecutive price pairs.
2. Whenever today is higher than yesterday, add the difference.
3. Skip flat or down moves.
4. Summing all rises equals the optimal multi-trade profit.
5. Return that sum.
""",
    "0123_best_time_to_buy_and_sell_stock_iii": """# How We Solve Best Time to Buy and Sell Stock III

At most two transactions with four running states.

## Steps

1. Track the cheapest buy for the first trade.
2. Track the best profit after selling the first trade.
3. Treat the second buy as price minus first-trade profit.
4. Track the best profit after the second sell.
5. Return the second-sell profit.
""",
    "0124_binary_tree_maximum_path_sum": """# How We Solve Binary Tree Maximum Path Sum

Any node-to-node path can bend at a root; DFS returns one-sided gain.

## Steps

1. Recurse into left and right, clamping negative gains to 0.
2. Candidate path through the node is value plus both gains.
3. Update a global best with that candidate.
4. Return value plus the better single child gain to the parent.
5. Answer is the global best after the DFS.
""",
    "0125_valid_palindrome": """# How We Solve Valid Palindrome

Ignore non-alphanumeric characters and compare case-insensitively.

## Steps

1. Place two pointers at the ends of the string.
2. Skip characters that are not letters or digits.
3. Compare the lowercased pair.
4. Move inward while they match.
5. Return true if the pointers meet without a mismatch.
""",
    "0126_word_ladder_ii": """# How We Solve Word Ladder II

BFS builds parent links for every shortest step, then DFS rebuilds paths.

## Steps

1. BFS from the begin word, generating one-letter neighbors.
2. Record parents only on the first level a word is reached.
3. Stop once the end word appears in a level.
4. DFS from the end word back through parents to the begin word.
5. Reverse each path and return all shortest ladders.
""",
    "0127_word_ladder": """# How We Solve Word Ladder

BFS finds the shortest transformation length.

## Steps

1. Put the word list into a set for O(1) lookups.
2. Queue the begin word with length 1.
3. Expand every one-letter neighbor still in the set.
4. Mark words visited as they are enqueued.
5. Return the length when the end word is reached, else 0.
""",
    "0128_longest_consecutive_sequence": """# How We Solve Longest Consecutive Sequence

Use a set and only start counting at the beginning of a streak.

## Steps

1. Insert every number into a set.
2. For each number, skip it if `num - 1` is also present.
3. Otherwise walk `num + 1`, `num + 2`, ... while they exist.
4. Track the longest streak length.
5. Return that length.
""",
    "0129_sum_root_to_leaf_numbers": """# How We Solve Sum Root to Leaf Numbers

Each root-to-leaf path forms a decimal number; sum them all.

## Steps

1. DFS with the number built so far.
2. Append the current digit by multiplying by 10 and adding `val`.
3. At a leaf, return that number.
4. Otherwise return the sum of left and right recursive results.
5. Start the DFS from the root with 0.
""",
    "0130_surrounded_regions": """# How We Solve Surrounded Regions

Only `O` regions touching the border survive; everything else becomes `X`.

## Steps

1. DFS/BFS from every border `O` and mark the connected region as safe.
2. Scan the whole board afterward.
3. Turn remaining `O` cells into `X` (they were surrounded).
4. Restore safe markers back to `O`.
5. The board is updated in place.
""",
    "0131_palindrome_partitioning": """# How We Solve Palindrome Partitioning

Backtrack every cut that leaves a palindrome prefix of the remaining string.

## Steps

1. Start DFS at index 0 with an empty path.
2. Try every end index and keep the slice only if it is a palindrome.
3. Recurse from the next index with that slice appended.
4. When the start reaches the end, record a complete partition.
5. Backtrack by popping after each recursive call.
""",
    "0132_palindrome_partitioning_ii": """# How We Solve Palindrome Partitioning II

Precompute palindrome spans, then DP the minimum cuts to reach each index.

## Steps

1. Build a boolean table of every palindromic substring.
2. Let `cuts[i]` be the fewest cuts needed for `s[0..i]`.
3. If `s[0..i]` itself is a palindrome, `cuts[i] = 0`.
4. Otherwise try every split `j` where `s[j+1..i]` is a palindrome.
5. Return `cuts[n-1]`.
""",
    "0133_clone_graph": """# How We Solve Clone Graph

DFS/BFS clone each node once and wire neighbor pointers to the clones.

## Steps

1. Return null for an empty graph.
2. Keep a map from original node value (or identity) to its clone.
3. Create the clone before recursing so cycles terminate.
4. Clone every neighbor and attach the cloned neighbor list.
5. Return the clone of the start node.
""",
    "0134_gas_station": """# How We Solve Gas Station

If total gas covers total cost, the unique start is after the worst prefix tank.

## Steps

1. Track overall surplus and the current tank from a candidate start.
2. Add `gas[i] - cost[i]` at each station.
3. When the tank goes negative, reset start to `i + 1` and tank to 0.
4. After one pass, succeed only if total surplus is non-negative.
5. Return that start index, or -1.
""",
    "0135_candy": """# How We Solve Candy

Two passes enforce the left and right neighbor rating constraints.

## Steps

1. Give every child one candy.
2. Left-to-right: if ratings rise, give one more than the left neighbor.
3. Right-to-left: if ratings rise going left, raise to beat the right neighbor.
4. Take the max of both constraints at each child.
5. Sum the candies.
""",
    "0136_single_number": """# How We Solve Single Number

XOR cancels every duplicated value and leaves the unique one.

## Steps

1. Start with 0.
2. XOR every number into the accumulator.
3. Pairs cancel to 0.
4. The leftover bits are the single number.
5. Return that value.
""",
    "0137_single_number_ii": """# How We Solve Single Number II

Track bits seen once and twice so triples clear out.

## Steps

1. Maintain `ones` and `twos` bit masks.
2. For each number, update ones with bits not already in twos.
3. Update twos with bits not already in ones.
4. After three appearances, both masks clear that bit.
5. `ones` holds the unique number.
""",
    "0138_copy_list_with_random_pointer": """# How We Solve Copy List with Random Pointer

Clone each node once, then copy both `next` and `random` through the map.

## Steps

1. Return null for an empty list.
2. Map each original node identity to its clone.
3. Create the clone before following pointers to handle cycles/shared refs.
4. Recursively (or iteratively) set `next` and `random` on the clone.
5. Return the clone of the head.
""",
    "0139_word_break": """# How We Solve Word Break

DP marks whether every prefix can be segmented with dictionary words.

## Steps

1. Put the dictionary into a set.
2. Let `dp[0]` mean the empty prefix is valid.
3. For each end index, try every earlier start where `dp[start]` is true.
4. If `s[start:end]` is a word, set `dp[end]`.
5. Return `dp[n]`.
""",
    "0140_word_break_ii": """# How We Solve Word Break II

Memoized DFS builds every sentence that segments the suffix.

## Steps

1. Put dictionary words in a set.
2. From each start index, try every dictionary word that matches a prefix.
3. Recurse on the remaining suffix and prepend the word to each continuation.
4. Memoize the list of sentences for each start index.
5. Return the sentences for index 0.
""",
    "0141_linked_list_cycle": """# How We Solve Linked List Cycle

Floyd's tortoise and hare detects whether a cycle exists.

## Steps

1. Start slow and fast at the head.
2. Move slow one step and fast two steps.
3. If they ever meet, a cycle exists.
4. If fast reaches null, there is no cycle.
5. Return that boolean result.
""",
    "0142_linked_list_cycle_ii": """# How We Solve Linked List Cycle II

After Floyd's meet point, restart one pointer at the head to find the entry.

## Steps

1. Run tortoise and hare until they meet, or prove there is no cycle.
2. Reset one pointer to the head.
3. Advance both one step at a time.
4. Their next meeting point is the cycle entrance.
5. Return that node, or null if none.
""",
    "0143_reorder_list": """# How We Solve Reorder List

Split, reverse the second half, then weave the two halves together.

## Steps

1. Find the midpoint with slow/fast pointers.
2. Cut the list into first and second halves.
3. Reverse the second half in place.
4. Alternate nodes from the first half and the reversed second half.
5. The list is updated in place.
""",
    "0144_binary_tree_preorder_traversal": """# How We Solve Binary Tree Preorder Traversal

Visit root, then left, then right.

## Steps

1. If the node is null, stop.
2. Record the node value.
3. Recurse into the left subtree.
4. Recurse into the right subtree.
5. Return the collected values.
""",
    "0145_binary_tree_postorder_traversal": """# How We Solve Binary Tree Postorder Traversal

Visit left, then right, then root.

## Steps

1. If the node is null, stop.
2. Recurse into the left subtree.
3. Recurse into the right subtree.
4. Record the node value.
5. Return the collected values.
""",
    "0146_lru_cache": """# How We Solve LRU Cache

Hash map plus doubly linked list give O(1) get and put with eviction.

## Steps

1. Store key-to-node lookups in a map.
2. Keep most-recent nodes near the head of a doubly linked list.
3. On get, move the node to the front and return its value.
4. On put, update or insert at the front.
5. If capacity is exceeded, evict the node before the tail.
""",
    "0147_insertion_sort_list": """# How We Solve Insertion Sort List

Insert each node into a growing sorted dummy-headed list.

## Steps

1. Create a dummy head for the sorted result.
2. Take nodes one by one from the input list.
3. Walk the sorted list until the insertion spot.
4. Splice the current node into place.
5. Return dummy.next when finished.
""",
    "0148_sort_list": """# How We Solve Sort List

Merge-sort the linked list in O(n log n) time and O(1) extra pointer space.

## Steps

1. Base case: empty or single-node lists are already sorted.
2. Split at the midpoint with slow/fast pointers.
3. Recursively sort both halves.
4. Merge the two sorted halves by value.
5. Return the merged head.
""",
    "0149_max_points_on_a_line": """# How We Solve Max Points on a Line

For each origin point, group other points by reduced slope.

## Steps

1. If there are at most two points, return that count.
2. Fix each point as an origin.
3. Normalize slopes with gcd and a consistent sign.
4. Count how many points share each slope with the origin.
5. Track the global maximum over all origins.
""",
    "0150_evaluate_reverse_polish_notation": """# How We Solve Evaluate Reverse Polish Notation

Use a stack: push numbers, pop two operands for each operator.

## Steps

1. Scan tokens left to right.
2. Push integers onto the stack.
3. For an operator, pop right then left.
4. Apply the operator (division truncates toward zero) and push the result.
5. The final stack value is the answer.
""",
    "0151_reverse_words_in_a_string": """# How We Solve Reverse Words in a String

Split on whitespace, reverse the word list, and join with single spaces.

## Steps

1. Split the string on any run of whitespace.
2. Drop empty tokens created by leading or trailing spaces.
3. Reverse the remaining words.
4. Join them with a single space.
5. Return the rebuilt string.
""",
    "0152_maximum_product_subarray": """# How We Solve Maximum Product Subarray

Track both the running max and min products because negatives can flip them.

## Steps

1. Seed best, max, and min with the first value.
2. For each next number, consider itself and products with the old max/min.
3. Update the running max and min from those candidates.
4. Keep the global best product seen so far.
5. Return that best value.
""",
    "0153_find_minimum_in_rotated_sorted_array": """# How We Solve Find Minimum in Rotated Sorted Array

Binary search on the rotated boundary using comparison with the right end.

## Steps

1. Keep a left/right window over the array.
2. Compare the middle value with the rightmost value.
3. If mid is greater than right, the minimum is to the right of mid.
4. Otherwise shrink the right side to mid.
5. When left meets right, that index holds the minimum.
""",
    "0154_find_minimum_in_rotated_sorted_array_ii": """# How We Solve Find Minimum in Rotated Sorted Array II

Same binary search as the unique case, but shrink carefully when duplicates tie.

## Steps

1. Binary search with left and right pointers.
2. If mid is greater than right, move left past mid.
3. If mid is less than right, move right to mid.
4. If they are equal, decrement right to skip the duplicate.
5. Return the value at the final left index.
""",
    "0155_min_stack": """# How We Solve Min Stack

Keep a parallel mins stack so getMin stays O(1).

## Steps

1. On push, append the value and the new running minimum.
2. On pop, remove from both stacks together.
3. Top returns the last value on the main stack.
4. getMin returns the last value on the mins stack.
5. Every operation stays amortized constant time.
""",
    "0156_binary_tree_upside_down": """# How We Solve Binary Tree Upside Down

Iteratively rotate each left child into the new root while rewiring siblings.

## Steps

1. Walk down the left spine.
2. Save the next left child before rewriting links.
3. Make the previous right child the new left.
4. Make the previous node the new right.
5. Continue until the old leftmost node becomes the new root.
""",
    "0157_read_n_characters_given_read4": """# How We Solve Read N Characters Given Read4

Call read4 in a loop and copy characters into the destination until n are filled.

## Steps

1. Simulate read4 over the file string four characters at a time.
2. Copy as many as still needed into the destination buffer.
3. Stop early when read4 returns fewer than four characters.
4. Also stop once n characters have been copied.
5. Return the actual count written.
""",
    "0158_read_n_characters_given_read4_ii_call_multiple_times": """# How We Solve Read N Characters Given read4 II

Persist leftover characters between calls so multiple reads share one file pointer.

## Steps

1. Keep an internal 4-char buffer with size and index.
2. For each query, drain leftovers before calling read4 again.
3. Refill the buffer only when it is empty.
4. Copy until the query count is met or the file ends.
5. Return the count for every query in order.
""",
    "0159_longest_substring_with_at_most_two_distinct_characters": """# How We Solve Longest Substring with At Most Two Distinct Characters

Sliding window with a frequency map limited to two distinct characters.

## Steps

1. Expand the right pointer and count characters.
2. While more than two distinct characters remain, shrink from the left.
3. Delete a character from the map when its count hits zero.
4. Track the maximum valid window length.
5. Return that length.
""",
    "0160_intersection_of_two_linked_lists": """# How We Solve Intersection of Two Linked Lists

Two pointers switch heads so both travel the same total distance.

## Steps

1. Start one pointer on each list.
2. Advance both one step at a time.
3. When a pointer reaches the end, redirect it to the other list's head.
4. They meet at the intersection, or both become null.
5. Return that meeting node.
""",
    "0161_one_edit_distance": """# How We Solve One Edit Distance

Check whether one insert, delete, or replace turns `s` into `t`.

## Steps

1. Reject equal strings and length gaps larger than one.
2. Make `s` the shorter string when lengths differ.
3. Walk until the first mismatch.
4. For equal lengths, the suffixes after that index must match.
5. For insert/delete, `s` from the mismatch must equal `t` from the next char.
""",
    "0162_find_peak_element": """# How We Solve Find Peak Element

Binary search follows the rising slope to any peak.

## Steps

1. Keep a left/right window over the array.
2. Compare the middle value with its right neighbor.
3. If mid is greater, a peak lies on the left side including mid.
4. Otherwise climb right by setting left to mid + 1.
5. When left meets right, that index is a peak.
""",
    "0163_missing_ranges": """# How We Solve Missing Ranges

Scan the sorted numbers and emit every gap inside `[lower, upper]`.

## Steps

1. Start with a sentinel just before `lower`.
2. Walk each number plus a sentinel just after `upper`.
3. Whenever the gap is at least two, record `[prev+1, num-1]`.
4. Update `prev` to the current number.
5. Return the collected inclusive ranges.
""",
    "0164_maximum_gap": """# How We Solve Maximum Gap

Bucket sort guarantees the maximum adjacent gap after sorting.

## Steps

1. Return 0 for fewer than two numbers.
2. Place values into buckets sized by the pigeonhole principle.
3. Track each bucket's minimum and maximum.
4. The answer is the largest gap between consecutive non-empty buckets.
5. Return that gap.
""",
    "0165_compare_version_numbers": """# How We Solve Compare Version Numbers

Compare dotted revisions as integers, padding missing parts with zeros.

## Steps

1. Split both versions on `.`.
2. Convert each revision to an integer.
3. Pad the shorter list with zeros.
4. Compare corresponding revisions left to right.
5. Return -1, 1, or 0.
""",
    "0166_fraction_to_recurring_decimal": """# How We Solve Fraction to Recurring Decimal

Long division with a remainder map detects the repeating cycle.

## Steps

1. Handle zero and the overall sign first.
2. Emit the integer quotient.
3. While a remainder remains, record its position in the decimal.
4. Multiply by 10, append the next digit, and update the remainder.
5. When a remainder repeats, wrap that span in parentheses.
""",
    "0167_two_sum_ii_input_array_is_sorted": """# How We Solve Two Sum II

Two pointers on the sorted array find the unique pair.

## Steps

1. Start left at the beginning and right at the end.
2. Compare their sum with the target.
3. Move left up when the sum is too small.
4. Move right down when the sum is too large.
5. Return the 1-indexed positions when they match.
""",
    "0168_excel_sheet_column_title": """# How We Solve Excel Sheet Column Title

Convert the 1-indexed number to base-26 letters A-Z.

## Steps

1. Subtract one so the mapping is 0-based.
2. Take modulo 26 to get the next letter from the right.
3. Divide by 26 and repeat while the number remains.
4. Reverse the collected letters.
5. Return the title string.
""",
    "0169_majority_element": """# How We Solve Majority Element

Boyer-Moore voting finds the element that appears more than n/2 times.

## Steps

1. Keep a candidate and a count.
2. When the count is zero, adopt the current value as candidate.
3. Increment for matches and decrement for mismatches.
4. The majority element survives as the final candidate.
5. Return that candidate.
""",
    "0170_two_sum_iii_data_structure_design": """# How We Solve Two Sum III

Store frequencies so add is cheap and find checks complements.

## Steps

1. Keep a count map of inserted numbers.
2. On add, increment that number's count.
3. On find, scan each number for `value - number`.
4. If the complement equals the number, require count at least 2.
5. Otherwise succeed when the complement exists in the map.
""",
    "0171_excel_sheet_column_number": """# How We Solve Excel Sheet Column Number

Treat the title as a base-26 number with digits A-Z.

## Steps

1. Start the result at 0.
2. For each character left to right, multiply by 26.
3. Add the letter's 1-based value (`A` = 1).
4. Continue through the whole title.
5. Return the accumulated number.
""",
    "0172_factorial_trailing_zeroes": """# How We Solve Factorial Trailing Zeroes

Count factors of 5 in `n!`; each contributes a trailing zero.

## Steps

1. Initialize a counter to 0.
2. Divide `n` by 5 and add the quotient.
3. Repeat with the new quotient.
4. Stop when the quotient becomes 0.
5. Return the total count of fives.
""",
    "0173_binary_search_tree_iterator": """# How We Solve Binary Search Tree Iterator

Controlled inorder traversal with a stack of left spines.

## Steps

1. On construction, push the root and all left children.
2. `hasNext` is true while the stack is non-empty.
3. `next` pops the top node as the next inorder value.
4. Then push that node's right child and its left spine.
5. Each visit costs amortized O(1) time.
""",
    "0174_dungeon_game": """# How We Solve Dungeon Game

DP backward from the princess: each cell stores the min HP needed there.

## Steps

1. Work from the bottom-right corner toward the start.
2. Need enough HP so that after the room's effect you can still reach the exit.
3. Take the cheaper of the right and down options.
4. Clamp any non-positive need up to 1.
5. The top-left DP value is the answer.
""",
    "0175_combine_two_tables": """# How We Solve Combine Two Tables

Left join `Address` onto `Person` so every person appears once.

## Steps

1. Select first name, last name, city, and state.
2. Start from the `Person` table.
3. Left join `Address` on matching `personId`.
4. Missing addresses become null city/state.
5. Return the joined rows.
""",
    "0176_second_highest_salary": """# How We Solve Second Highest Salary

Pick the second distinct salary with an ordered offset query.

## Steps

1. Select distinct salaries from `Employee`.
2. Order them descending.
3. Skip the first row with `OFFSET 1`.
4. Take one row as `SecondHighestSalary`.
5. If none remains, the scalar subquery returns null.
""",
    "0177_nth_highest_salary": """# How We Solve Nth Highest Salary

A function returns the Nth distinct salary via `LIMIT`/`OFFSET`.

## Steps

1. Accept `N` as the function argument.
2. Convert it to a 0-based offset `N - 1`.
3. Select distinct salaries ordered descending.
4. Skip `N - 1` rows and take one.
5. Return null when fewer than `N` distinct salaries exist.
""",
    "0178_rank_scores": """# How We Solve Rank Scores

Use dense ranking so ties share a rank and the next rank is consecutive.

## Steps

1. Select each score from `Scores`.
2. Apply `DENSE_RANK()` ordered by score descending.
3. Alias the rank column as `rank`.
4. Order the output by score descending.
5. Return score and rank pairs.
""",
    "0179_largest_number": """# How We Solve Largest Number

Sort number strings by which concatenation is larger.

## Steps

1. Convert every integer to a string.
2. Sort so that `a` comes before `b` when `a+b` is greater than `b+a`.
3. Join the sorted strings.
4. If the result would start with zeros, return `"0"`.
5. Otherwise return the joined string.
""",
    "0180_consecutive_numbers": """# How We Solve Consecutive Numbers

Self-join three consecutive log rows that share the same number.

## Steps

1. Alias `Logs` three times as `l1`, `l2`, and `l3`.
2. Require consecutive ids: `l1.id + 1 = l2.id` and `l2.id + 1 = l3.id`.
3. Require equal `num` across all three.
4. Select the distinct matching numbers.
5. Return them as `ConsecutiveNums`.
""",
    "0181_employees_earning_more_than_their_managers": """# How We Solve Employees Earning More Than Their Managers

Self-join employees to their managers and compare salaries.

## Steps

1. Alias `Employee` as the worker and again as the manager.
2. Join on `worker.managerId = manager.id`.
3. Keep rows where the worker salary is greater.
4. Select the worker name as `Employee`.
5. Return those names.
""",
    "0182_duplicate_emails": """# How We Solve Duplicate Emails

Group by email and keep only addresses that appear more than once.

## Steps

1. Select email from `Person`.
2. Group rows by email.
3. Keep groups with `COUNT(*) > 1`.
4. Alias the column as `Email`.
5. Return the duplicate addresses.
""",
    "0183_customers_who_never_order": """# How We Solve Customers Who Never Order

Find customers whose ids never appear in `Orders`.

## Steps

1. Select customer names from `Customers`.
2. Exclude ids present in `Orders.customerId`.
3. Use `NOT IN` or an anti-join.
4. Alias the name column as `Customers`.
5. Return the remaining customers.
""",
    "0184_department_highest_salary": """# How We Solve Department Highest Salary

Join employees to departments and keep only each department's max salary.

## Steps

1. Join `Employee` to `Department` on department id.
2. For each employee, compare salary to the department maximum.
3. Keep rows equal to that maximum.
4. Select department name, employee name, and salary.
5. Return all top earners, including ties.
""",
    "0185_department_top_three_salaries": """# How We Solve Department Top Three Salaries

Dense-rank salaries within each department and keep ranks 1-3.

## Steps

1. Partition employees by department and rank salaries descending.
2. Use `DENSE_RANK` so ties share a rank.
3. Join the ranked rows to `Department`.
4. Keep rows with rank at most 3.
5. Return department, employee, and salary.
""",
    "0186_reverse_words_in_a_string_ii": """# How We Solve Reverse Words in a String II

Reverse the whole character array, then reverse each word in place.

## Steps

1. Reverse every character from start to end.
2. Scan for word boundaries separated by spaces.
3. Reverse each word segment individually.
4. Leave the single spaces between words alone.
5. The array is updated in place.
""",
    "0187_repeated_dna_sequences": """# How We Solve Repeated DNA Sequences

Slide a 10-letter window and record sequences seen more than once.

## Steps

1. Walk every substring of length 10.
2. Track sequences already seen in a set.
3. When a sequence appears again, add it to the result set.
4. Deduplicate automatically with the result set.
5. Return the collected sequences.
""",
    "0188_best_time_to_buy_and_sell_stock_iv": """# How We Solve Best Time to Buy and Sell Stock IV

DP over at most `k` transactions, with an unlimited-trade shortcut.

## Steps

1. If `k` is large, sum every upward day-to-day gain.
2. Otherwise keep buy/sell states for each transaction count.
3. Update buy as the cheapest effective purchase after prior profit.
4. Update sell as the best profit after selling that purchase.
5. Return the profit after `k` sells.
""",
    "0189_rotate_array": """# How We Solve Rotate Array

Three reverses rotate the array right by `k` in place.

## Steps

1. Reduce `k` modulo the array length.
2. Reverse the entire array.
3. Reverse the first `k` elements.
4. Reverse the remaining suffix.
5. The array is now rotated right by `k`.
""",
    "0190_reverse_bits": """# How We Solve Reverse Bits

Build a 32-bit result by shifting in bits from the low end of `n`.

## Steps

1. Start the result at 0.
2. For each of 32 bits, shift result left.
3. Append the least significant bit of `n`.
4. Shift `n` right by one.
5. Return the reversed 32-bit integer.
""",
    "0191_number_of_1_bits": """# How We Solve Number of 1 Bits

Clear the lowest set bit repeatedly and count how many times that happens.

## Steps

1. Start a counter at 0.
2. While `n` is nonzero, replace it with `n & (n - 1)`.
3. Increment the counter after each clear.
4. Stop when every set bit is gone.
5. Return the counter as the Hamming weight.
""",
    "0192_word_frequency": """# How We Solve Word Frequency

Use a Unix pipeline to split, count, and sort word frequencies.

## Steps

1. Read `words.txt` and squeeze spaces into newlines.
2. Sort the resulting words.
3. Count unique lines with `uniq -c`.
4. Sort those counts descending.
5. Print `word count` for each line.
""",
    "0193_valid_phone_numbers": """# How We Solve Valid Phone Numbers

Filter `file.txt` with a regex for the two allowed phone formats.

## Steps

1. Match `xxx-xxx-xxxx`.
2. Or match `(xxx) xxx-xxxx`.
3. Anchor the pattern to the whole line.
4. Use `grep -E` against `file.txt`.
5. Print only the valid numbers.
""",
    "0194_transpose_file": """# How We Solve Transpose File

Use `awk` to collect each column into a row while reading the file.

## Steps

1. For every field index, append the current token to that column buffer.
2. Separate later tokens with spaces.
3. After the file ends, print each column buffer as a line.
4. Preserve the original left-to-right field order.
5. Return the transposed text.
""",
    "0195_tenth_line": """# How We Solve Tenth Line

Print only the tenth line of `file.txt`.

## Steps

1. Use `sed -n '10p'`.
2. Read `file.txt`.
3. Suppress all other lines.
4. Emit line 10 when it exists.
5. Produce empty output if the file is shorter.
""",
    "0196_delete_duplicate_emails": """# How We Solve Delete Duplicate Emails

Delete higher-id rows that share an email with a lower-id row.

## Steps

1. Self-join `Person` on matching email.
2. Keep pairs where the left id is greater.
3. Delete those left-side duplicates.
4. The smallest id for each email remains.
5. The table now has unique emails.
""",
    "0197_rising_temperature": """# How We Solve Rising Temperature

Compare each day's temperature with the previous calendar day.

## Steps

1. Self-join `Weather` so dates differ by one day.
2. Use `DATEDIFF` to enforce consecutive dates.
3. Keep rows warmer than the previous day.
4. Select those ids.
5. Return the rising-temperature days.
""",
    "0198_house_robber": """# How We Solve House Robber

Track the best totals with and without robbing the previous house.

## Steps

1. Keep `prev2` and `prev1` as the best results for the last two houses.
2. For each house, choose max(skip it, rob it + prev2).
3. Shift the window forward.
4. Continue through the whole street.
5. Return the final best total.
""",
    "0199_binary_tree_right_side_view": """# How We Solve Binary Tree Right Side View

Level-order BFS and record the last node on each level.

## Steps

1. Queue the root if it exists.
2. Process one level at a time.
3. Enqueue left then right children.
4. Append the last node's value for that level.
5. Return the collected right-side values.
""",
    "0200_number_of_islands": """# How We Solve Number of Islands

DFS/BFS flood-fill every land cell and count how many components you start.

## Steps

1. Scan the grid for an unvisited `'1'`.
2. Increment the island count.
3. Flood-fill that component, marking land as water.
4. Continue scanning for the next unvisited land cell.
5. Return the total number of islands.
""",
    "0201_bitwise_and_of_numbers_range": """# How We Solve Bitwise AND of Numbers Range

Shift away differing low bits until left and right share a common prefix.

## Steps

1. While left is less than right, right-shift both.
2. Count how many shifts were needed.
3. The remaining value is the shared high-bit prefix.
4. Shift that prefix back left by the same count.
5. Return the reconstructed AND of the whole range.
""",
    "0202_happy_number": """# How We Solve Happy Number

Replace a number by the sum of squared digits and watch for 1 or a cycle.

## Steps

1. Compute the next value as the sum of each digit squared.
2. Record every value seen so far.
3. Stop with true when the value becomes 1.
4. Stop with false when a previously seen value reappears.
5. Return that boolean result.
""",
    "0203_remove_linked_list_elements": """# How We Solve Remove Linked List Elements

Walk a dummy-headed list and skip every node whose value matches the target.

## Steps

1. Attach a dummy node before the head.
2. Advance while looking at the next node.
3. If the next value equals the target, bypass that node.
4. Otherwise move forward one step.
5. Return dummy.next as the cleaned list.
""",
    "0204_count_primes": """# How We Solve Count Primes

Use the Sieve of Eratosthenes to mark composites below `n`.

## Steps

1. Return 0 when `n` is at most 2.
2. Create a boolean array marking every index as potentially prime.
3. For each prime `p`, mark multiples starting at `p*p`.
4. Continue while `p*p < n`.
5. Count the remaining true entries.
""",
    "0205_isomorphic_strings": """# How We Solve Isomorphic Strings

Maintain two maps so the character mapping is a bijection.

## Steps

1. Pair characters from `s` and `t` in order.
2. Map each `s` character to its `t` partner.
3. Map each `t` character back to its `s` partner.
4. Reject any conflict with an earlier mapping.
5. Return true if every pair is consistent.
""",
    "0206_reverse_linked_list": """# How We Solve Reverse Linked List

Iteratively reverse next pointers while walking the list.

## Steps

1. Keep a `prev` pointer starting at null.
2. Store the next node before rewriting links.
3. Point the current node back to `prev`.
4. Advance `prev` and `current`.
5. Return `prev` as the new head.
""",
    "0207_course_schedule": """# How We Solve Course Schedule

Kahn's algorithm detects whether the prerequisite graph is a DAG.

## Steps

1. Build an adjacency list and indegree array.
2. Queue every course with indegree 0.
3. Take courses one by one and reduce neighbors' indegrees.
4. Enqueue neighbors that reach indegree 0.
5. Succeed only if every course was taken.
""",
    "0208_implement_trie_prefix_tree": """# How We Solve Implement Trie (Prefix Tree)

Store words in a character tree with an end-of-word flag on terminal nodes.

## Steps

1. Start each operation at the root.
2. On insert, create missing child nodes for each character.
3. Mark the final node as a complete word.
4. Search requires reaching a node marked as a word.
5. startsWith only requires that the prefix path exists.
""",
    "0209_minimum_size_subarray_sum": """# How We Solve Minimum Size Subarray Sum

Expand a sliding window until the sum meets the target, then shrink it.

## Steps

1. Move the right pointer and add each value to the running sum.
2. While the sum is at least the target, record the window length.
3. Subtract the left value and advance left.
4. Keep the shortest valid length seen.
5. Return 0 if no window ever reached the target.
""",
    "0210_course_schedule_ii": """# How We Solve Course Schedule II

Kahn's BFS produces a valid topological order of courses.

## Steps

1. Build the graph and indegree counts from prerequisites.
2. Queue all courses with indegree 0.
3. Append each dequeued course to the order.
4. Reduce indegrees of dependents and enqueue newly ready courses.
5. Return the order if it contains every course, otherwise an empty list.
""",
    "0211_design_add_and_search_words_data_structure": """# How We Solve Design Add and Search Words Data Structure

Store words in a trie and search with DFS when a dot wildcard appears.

## Steps

1. Each trie node maps characters to child nodes and marks word endings.
2. `addWord` walks the trie and sets the final node as a word.
3. `search` walks character by character for literal letters.
4. On `.`, try every child recursively.
5. A match succeeds only if the path ends on a word node.
""",
    "0212_word_search_ii": """# How We Solve Word Search II

Build a trie from the dictionary, then DFS the board while pruning dead trie branches.

## Steps

1. Insert every word into a trie and store the word at its terminal node.
2. DFS from each board cell following trie edges.
3. When a terminal node is reached, record that word and clear it to avoid duplicates.
4. Mark visited cells, explore four directions, then restore the cell.
5. Prune trie branches that have no remaining children.
""",
    "0213_house_robber_ii": """# How We Solve House Robber II

The circle breaks into two linear house-robber problems.

## Steps

1. If there is one house, return its value.
2. Rob houses `0..n-2` with the classic linear DP.
3. Rob houses `1..n-1` with the same DP.
4. Track `prev2` and `prev1` while scanning each range.
5. Return the maximum of the two linear results.
""",
    "0214_shortest_palindrome": """# How We Solve Shortest Palindrome

Find the longest palindromic prefix, then prepend the reverse of the remaining suffix.

## Steps

1. Build `s + "#" + reverse(s)`.
2. Compute the KMP prefix function on that string.
3. The last LPS value is the longest palindromic prefix length.
4. Reverse the suffix after that prefix.
5. Prepend that reversed suffix to `s`.
""",
    "0215_kth_largest_element_in_an_array": """# How We Solve Kth Largest Element in an Array

Quickselect partitions around a pivot until the kth largest lands in place.

## Steps

1. Convert k to the target index `len(nums) - k`.
2. Pick a random pivot and partition the array.
3. If the pivot index equals the target, return that value.
4. Recurse on the left or right side depending on the pivot index.
5. Repeat until the target index is found.
""",
    "0216_combination_sum_iii": """# How We Solve Combination Sum III

Backtrack over digits 1–9 to build k numbers that sum to n.

## Steps

1. Start with an empty path and search from digit 1.
2. Add each candidate digit if it does not exceed the remaining sum.
3. When the path length is k and the sum is 0, save a copy.
4. Always move to the next digit to avoid reuse.
5. Backtrack by removing the last chosen digit.
""",
    "0217_contains_duplicate": """# How We Solve Contains Duplicate

A duplicate exists exactly when some value appears more than once.

## Steps

1. Insert all numbers into a set.
2. Compare the set size with the array length.
3. If the set is smaller, at least one duplicate exists.
4. Otherwise every value is unique.
5. Return the comparison result.
""",
    "0218_the_skyline_problem": """# How We Solve The Skyline Problem

Sweep building events left to right while tracking active heights in a heap.

## Steps

1. Create start events `(left, -height, right)` and end events `(right, 0, 0)`.
2. Sort events by x, with starts before ends at the same x.
3. Remove heap entries whose buildings ended before the current x.
4. Push a new active height when a building starts.
5. Append `[x, currentMax]` whenever the max height changes.
""",
    "0219_contains_duplicate_ii": """# How We Solve Contains Duplicate II

Track the most recent index of each value while scanning the array.

## Steps

1. Walk through the array left to right.
2. Store each value's latest index in a hash map.
3. If the value was seen before, check the index gap.
4. Return true when the gap is at most k.
5. Otherwise update the stored index and continue.
""",
    "0220_contains_duplicate_iii": """# How We Solve Contains Duplicate III

Bucket numbers into width-sized groups inside a sliding window.

## Steps

1. Reject impossible inputs where the window or value tolerance is invalid.
2. Map each number to a bucket id using width `valueDiff + 1`.
3. If the same bucket already exists, the pair is close enough.
4. Also check the previous and next buckets for a valid neighbor.
5. Remove the bucket for the value leaving the window when it grows too large.
""",
    "0221_maximal_square": """# How We Solve Maximal Square

Use 1D DP where each cell stores the side length of the largest square ending there.

## Steps

1. Scan the matrix row by row with a rolling DP array.
2. When a cell is `1`, set `dp = min(left, top, top-left) + 1`.
3. Reset the cell to 0 when it is not part of a square.
4. Track the maximum side length seen.
5. Return its square area.
""",
    "0222_count_complete_tree_nodes": """# How We Solve Count Complete Tree Nodes

Exploit the complete-tree shape to count in O(log² n) time.

## Steps

1. Measure the leftmost depth and rightmost depth.
2. If they match, the tree is perfect with `2^h - 1` nodes.
3. Otherwise count the root plus both subtrees recursively.
4. Repeat the depth check on each recursive call.
5. Sum the results.
""",
    "0223_rectangle_area": """# How We Solve Rectangle Area

Add both rectangle areas and subtract their overlap.

## Steps

1. Compute the area of rectangle A.
2. Compute the area of rectangle B.
3. Find overlap width as the horizontal intersection length.
4. Find overlap height as the vertical intersection length.
5. Return `areaA + areaB - overlapWidth * overlapHeight`.
""",
    "0224_basic_calculator": """# How We Solve Basic Calculator

Evaluate expressions with `+`, `-`, and parentheses using a stack.

## Steps

1. Walk the string while tracking the current number and sign.
2. On `+` or `-`, apply the current sign to the running result.
3. On `(`, push the current result and sign onto a stack.
4. On `)`, finish the inner result and combine it with the stack.
5. Add the final number after the loop ends.
""",
    "0225_implement_stack_using_queues": """# How We Solve Implement Stack using Queues

Rotate the queue after each push so the newest element sits at the front.

## Steps

1. Store all elements in one queue.
2. On push, append the value.
3. Rotate by moving every earlier element to the back.
4. Pop and top both read from the queue front.
5. Empty checks whether the queue has no elements.
""",
    "0226_invert_binary_tree": """# How We Solve Invert Binary Tree

Recursively swap each node's left and right children.

## Steps

1. Return null for an empty tree.
2. Recursively invert the right subtree.
3. Recursively invert the left subtree.
4. Assign the inverted right subtree to `left`.
5. Assign the inverted left subtree to `right`.
""",
    "0227_basic_calculator_ii": """# How We Solve Basic Calculator II

Use a stack to defer addition and subtraction while handling `*` and `/` immediately.

## Steps

1. Parse numbers and operators left to right.
2. Push signed values for `+` and `-`.
3. Multiply or divide with the top stack value for `*` and `/`.
4. Reset the current number after each operator.
5. Return the sum of the stack.
""",
    "0228_summary_ranges": """# How We Solve Summary Ranges

Group consecutive sorted numbers into ranges.

## Steps

1. Scan the sorted array from left to right.
2. Mark the start of each range.
3. Extend the range while the next number is exactly one greater.
4. Format a single value or a `start->end` range.
5. Append each formatted range to the answer.
""",
    "0229_majority_element_ii": """# How We Solve Majority Element II

Boyer-Moore voting with two candidates finds elements appearing more than n/3 times.

## Steps

1. First pass tracks two candidate values with counters.
2. Replace empty counters with new values.
3. Decrement both counters when neither candidate matches.
4. Second pass counts actual frequencies of the candidates.
5. Keep values whose counts exceed `n // 3`.
""",
    "0230_kth_smallest_element_in_a_bst": """# How We Solve Kth Smallest Element in a BST

Iterative inorder traversal visits values in sorted order.

## Steps

1. Push all left children onto a stack.
2. Pop the next smallest node.
3. Decrease k each time a node is visited.
4. Return the value when k reaches 0.
5. Move to the right child and repeat.
""",
    "0231_power_of_two": """# How We Solve Power of Two

A positive power of two has exactly one set bit.

## Steps

1. Reject non-positive numbers.
2. Compute `n & (n - 1)`.
3. Subtracting 1 clears the lowest set bit.
4. Powers of two become 0 after that operation.
5. Return whether the result is 0.
""",
    "0232_implement_queue_using_stacks": """# How We Solve Implement Queue using Stacks

Use an input stack and an output stack to reverse order on demand.

## Steps

1. Push new items onto the input stack.
2. When popping or peeking, move items to the output stack if it is empty.
3. Each move reverses order once, giving FIFO behavior.
4. Pop and peek from the output stack top.
5. Empty means both stacks are empty.
""",
    "0233_number_of_digit_one": """# How We Solve Number of Digit One

Count ones digit by digit using higher, current, and lower parts of n.

## Steps

1. Process each decimal place with a growing factor.
2. Split n into higher, current digit, and lower segments.
3. Add the count contributed by that digit position.
4. Handle the special case when the current digit is 1.
5. Sum contributions across all digit positions.
""",
    "0234_palindrome_linked_list": """# How We Solve Palindrome Linked List

Find the middle, reverse the second half, then compare both halves.

## Steps

1. Use slow and fast pointers to reach the middle.
2. Reverse the second half of the list.
3. Walk the first half and reversed second half together.
4. Compare values at each step.
5. Return false on the first mismatch, otherwise true.
""",
    "0235_lowest_common_ancestor_of_a_binary_search_tree": """# How We Solve Lowest Common Ancestor of a BST

Use BST ordering to walk toward the split point.

## Steps

1. Start at the root.
2. If both target values are smaller, go left.
3. If both are larger, go right.
4. Otherwise the current node is the LCA.
5. Return that node.
""",
    "0236_lowest_common_ancestor_of_a_binary_tree": """# How We Solve Lowest Common Ancestor of a Binary Tree

Recursive post-order search finds where the paths to p and q diverge.

## Steps

1. Return null for an empty node.
2. Return the node itself if it equals p or q.
3. Recurse on left and right subtrees.
4. If both sides return non-null, the current node is the LCA.
5. Otherwise return whichever side found a target.
""",
    "0237_delete_node_in_a_linked_list": """# How We Solve Delete Node in a Linked List

Copy the next node's value into the current node, then skip the next node.

## Steps

1. Read the value from the node after the target.
2. Copy that value into the target node.
3. Point the target node to the node after next.
4. This removes the next node instead of the target reference.
5. The list reflects the deletion without needing the head.
""",
    "0238_product_of_array_except_self": """# How We Solve Product of Array Except Self

Build prefix products forward and suffix products backward.

## Steps

1. Initialize the answer array with prefix products from left to right.
2. Track a running prefix multiplier.
3. Multiply by suffix products while scanning right to left.
4. Track a running suffix multiplier.
5. Return the final product array without using division.
""",
    "0239_sliding_window_maximum": """# How We Solve Sliding Window Maximum

Maintain a deque of indices with decreasing values.

## Steps

1. Append each index to the deque after removing smaller tail values.
2. Remove indices that fall outside the current window.
3. Once the window is full, the deque front is the maximum index.
4. Append that maximum to the answer.
5. Continue until the end of the array.
""",
    "0240_search_a_2d_matrix_ii": """# How We Solve Search a 2D Matrix II

Start at the top-right corner and eliminate a row or column each step.

## Steps

1. Begin at row 0 and the last column.
2. If the current value equals the target, return true.
3. If it is larger than the target, move left.
4. If it is smaller, move down.
5. Return false if the search walks off the matrix.
""",
    "0241_different_ways_to_add_parentheses": """# How We Solve Different Ways to Add Parentheses

Split the expression at each operator and combine left and right results.

## Steps

1. If the expression is a single number, return it.
2. Scan for operators `+`, `-`, and `*`.
3. Recursively compute all values for the left and right subexpressions.
4. Combine each pair with the operator at the split point.
5. Return every possible result.
""",
    "0242_valid_anagram": """# How We Solve Valid Anagram

Two strings are anagrams when every letter count matches.

## Steps

1. Reject different-length strings immediately.
2. Count letter frequencies for both strings in one pass.
3. Increment for characters in `s`.
4. Decrement for characters in `t`.
5. Return true only if all counts are zero.
""",
    "0243_shortest_word_distance": """# How We Solve Shortest Word Distance

Track the latest positions of both words while scanning the list once.

## Steps

1. Initialize the last seen index of each word to -1.
2. Walk through the word list in order.
3. Update the index when word1 or word2 appears.
4. If the other word was seen already, update the minimum distance.
5. Return the smallest gap found.
""",
    "0244_shortest_word_distance_ii": """# How We Solve Shortest Word Distance II

Given a list of words, quickly find the smallest gap between two given words.

## Steps

1. When built, save every index where each word appears.
2. To query word1 and word2, walk their two index lists with two fingers.
3. Compute distance between current pair of indexes.
4. Keep the smallest distance seen.
5. Move the finger pointing to the smaller index forward.
6. Return the smallest distance.
""",
    "0245_shortest_word_distance_iii": """# How We Solve Shortest Word Distance III

When both words are the same, find the minimum gap between two occurrences.

## Steps

1. If word1 equals word2, track the previous occurrence index only.
2. Update the minimum distance whenever the same word appears again.
3. Otherwise use the standard two-index scan from problem 243.
4. Keep the smallest valid distance during one pass.
5. Return that distance.
""",
    "0246_strobogrammatic_number": """# How We Solve Strobogrammatic Number

Compare digits from both ends using rotational symmetry pairs.

## Steps

1. Map each valid digit to its upside-down partner.
2. Use two pointers at the start and end.
3. Fail if the mapped start digit does not match the end digit.
4. Move both pointers inward.
5. Return true if every pair matches.
""",
    "0247_strobogrammatic_number_ii": """# How We Solve Strobogrammatic Number II

Recursively build every strobogrammatic number of length n.

## Steps

1. Base case: empty middle for even splits, or `0`, `1`, `8` for the center digit.
2. Try each valid outer digit pair.
3. Skip leading zero except when n is 1.
4. Recursively fill the inner substring.
5. Return all complete strings of length n.
""",
    "0248_strobogrammatic_number_iii": """# How We Solve Strobogrammatic Number III

Generate strobogrammatic numbers by length and count those in the numeric range.

## Steps

1. Loop over every length between `low` and `high`.
2. Generate all strobogrammatic strings of that length.
3. Convert bounds and candidates to integers for comparison.
4. Count values inside the inclusive range.
5. Return the total count.
""",
    "0249_group_shifted_strings": """# How We Solve Group Shifted Strings

Strings in the same shift group share the same relative letter offsets.

## Steps

1. For each string, compute offsets from its first character mod 26.
2. Use that offset tuple as the group key.
3. Append the string to the bucket for its key.
4. Collect all buckets as groups.
5. Return the grouped lists.
""",
    "0250_count_univalue_subtrees": """# How We Solve Count Univalue Subtrees

Post-order DFS checks whether each subtree has a single value.

## Steps

1. Return true for null nodes.
2. Recursively verify the left and right subtrees.
3. Ensure child values match the current node when children exist.
4. If the whole subtree is unival, increment the counter.
5. Return whether the current subtree is unival.
""",
    "0251_flatten_2d_vector": """# How We Solve Flatten 2D Vector

Track the current row and column while skipping empty inner lists.

## Steps

1. Store the 2D vector and initialize row and column to 0.
2. Advance until the current position points to a valid element.
3. Return the current value and move the column forward.
4. Advance again after each read.
5. Report whether any elements remain.
""",
    "0252_meeting_rooms": """# How We Solve Meeting Rooms

Sort meetings by start time and check for overlap.

## Steps

1. Sort intervals by their start times.
2. Walk through consecutive meetings.
3. If the next meeting starts before the previous one ends, return false.
4. Otherwise continue scanning.
5. Return true when no overlap exists.
""",
    "0253_meeting_rooms_ii": """# How We Solve Meeting Rooms II

Sweep sorted start and end times to track concurrent meetings.

## Steps

1. Sort all start times and all end times separately.
2. Compare the earliest remaining start with the earliest end.
3. If a meeting starts before one ends, increase the room count.
4. Otherwise free a room by moving the end pointer.
5. Return the maximum rooms needed at once.
""",
    "0254_factor_combinations": """# How We Solve Factor Combinations

Backtrack over factor splits and append the remaining value when valid.

## Steps

1. Try each factor starting from 2 up to the square root.
2. When a factor divides the remainder, push it and recurse.
3. After exploring smaller factors, append the remaining value if the path is non-empty.
4. Save combinations with at least two factors.
5. Backtrack and continue searching.
""",
    "0255_verify_preorder_sequence_in_binary_search_tree": """# How We Solve Verify Preorder Sequence in Binary Search Tree

Simulate BST construction with a stack and a lower bound.

## Steps

1. Track the smallest value allowed for the current position.
2. If the next value is below that bound, the sequence is invalid.
3. Pop smaller stack values while updating the lower bound.
4. Push the current value onto the stack.
5. Return true if the entire preorder is valid.
""",
    "0256_paint_house": """# How We Solve Paint House

Dynamic programming keeps the minimum cost for each color at every house.

## Steps

1. Initialize the first row costs for red, green, and blue.
2. For each next house, compute the cheapest way to paint each color.
3. Each color cost adds the current paint cost plus the best previous non-matching color.
4. Slide the DP row forward house by house.
5. Return the minimum of the final three costs.
""",
    "0257_binary_tree_paths": """# How We Solve Binary Tree Paths

DFS builds root-to-leaf path strings.

## Steps

1. Append the current node value to the path.
2. If the node is a leaf, join the path with arrows and save it.
3. Otherwise recurse on the left and right children.
4. Backtrack by removing the current node from the path.
5. Return all collected path strings.
""",
    "0258_add_digits": """# How We Solve Add Digits

Repeated digit sums equal the digital root formula.

## Steps

1. Return 0 immediately for input 0.
2. Otherwise compute `1 + (num - 1) % 9`.
3. This equals repeatedly summing digits until one digit remains.
4. Return that single-digit result.
""",
    "0259_3sum_smaller": """# How We Solve 3Sum Smaller

Sort the array and count triplets with a fixed left value and moving pointers.

## Steps

1. Sort the numbers.
2. Fix the leftmost value of each triplet.
3. Use two pointers on the remaining range.
4. If the sum is too small, all pairs up to the right pointer work.
5. Otherwise move the right pointer left and continue.
""",
    "0260_single_number_iii": """# How We Solve Single Number III

XOR finds the combined difference bit, then partitions numbers into two groups.

## Steps

1. XOR all numbers to get the xor of the two unique values.
2. Isolate any set bit that differs between them.
3. XOR numbers with that bit set into one accumulator.
4. XOR the rest into the other accumulator.
5. Return both unique numbers.
""",
    "0261_graph_valid_tree": """# How We Solve Graph Valid Tree

A valid tree on n nodes has exactly n-1 edges and no cycles.

## Steps

1. Reject immediately if the edge count is not n-1.
2. Initialize union-find parent pointers for each node.
3. For each edge, find the roots of both endpoints.
4. If the roots match, a cycle exists.
5. Otherwise merge the components and return true at the end.
""",
    "0262_trips_and_users": """# How We Solve Trips and Users

Compute daily cancellation rates for unbanned clients over a date range.

## Steps

1. Join trips with users on client id where the user role is client.
2. Keep only unbanned clients and dates in the target range.
3. Group by request date.
4. Divide non-completed trips by total trips and round to two decimals.
5. Order the results by day.
""",
    "0263_ugly_number": """# How We Solve Ugly Number

Repeatedly remove factors of 2, 3, and 5 until none remain.

## Steps

1. Reject non-positive numbers.
2. While divisible by 2, divide by 2.
3. Repeat for 3 and then 5.
4. If the remaining value is 1, the number is ugly.
5. Otherwise return false.
""",
    "0264_ugly_number_ii": """# How We Solve Ugly Number II

Generate ugly numbers in order using three moving pointers.

## Steps

1. Start the sequence with 1.
2. Track the next candidate from multiples of 2, 3, and 5.
3. Append the smallest candidate.
4. Advance every pointer that produced that candidate.
5. Return the nth generated ugly number.
""",
    "0265_paint_house_ii": """# How We Solve Paint House II

For each house, track the cheapest and second-cheapest previous colors.

## Steps

1. Initialize costs for the first house.
2. For each later house, find the minimum and second minimum previous costs.
3. Paint each color with the best non-conflicting previous cost.
4. Slide the DP row forward.
5. Return the minimum cost in the final row.
""",
    "0266_palindrome_permutation": """# How We Solve Palindrome Permutation

A string can permute into a palindrome when at most one character count is odd.

## Steps

1. Count each letter frequency.
2. Count how many letters have odd frequency.
3. Return true if that count is 0 or 1.
4. Otherwise return false.
""",
    "0267_palindrome_permutation_ii": """# How We Solve Palindrome Permutation II

Build unique permutations of half the string and mirror them around a middle character.

## Steps

1. Count characters and reject more than one odd count.
2. Put any odd-count character in the middle.
3. Build the sorted half with half of each character count.
4. Backtrack unique permutations of the half.
5. Mirror each prefix to form full palindromes.
""",
    "0268_missing_number": """# How We Solve Missing Number

The missing value is the difference between the expected and actual sums.

## Steps

1. Let n be the array length.
2. Compute the expected sum of 0 through n.
3. Subtract the actual array sum.
4. Return the difference as the missing number.
""",
    "0269_alien_dictionary": """# How We Solve Alien Dictionary

Derive letter order from adjacent word comparisons and topologically sort.

## Steps

1. Build a graph of characters appearing in the words.
2. Compare each adjacent word to find the first differing letter.
3. Detect invalid prefix cases that imply no valid order.
4. Topologically sort characters with indegree zero.
5. Return the order or an empty string if a cycle exists.
""",
    "0270_closest_binary_search_tree_value": """# How We Solve Closest Binary Search Tree Value

Walk the BST while tracking the closest value seen so far.

## Steps

1. Start with the root value as the closest candidate.
2. Compare distance to the current node and update if closer.
3. Return immediately on an exact match.
4. Go left if the target is smaller, otherwise go right.
5. Return the closest value after the walk ends.
""",
    "0271_encode_and_decode_strings": """# How We Solve Encode and Decode Strings

Prefix each string with its length and a delimiter before concatenation.

## Steps

1. For each string, write its length, a `#`, then the string bytes.
2. Join all encoded pieces into one string.
3. While decoding, read digits until `#` to get the length.
4. Slice the next length characters as one original string.
5. Repeat until the encoded string is exhausted.
""",
    "0272_closest_binary_search_tree_value_ii": """# How We Solve Closest Binary Search Tree Value II

Collect sorted values, then expand outward from the insertion point.

## Steps

1. Inorder traverse the BST into a sorted list.
2. Find the first value not less than the target.
3. Repeatedly pick the closer side between left and right neighbors.
4. Append that value and move the pointer inward.
5. Stop after collecting k values.
""",
    "0273_integer_to_english_words": """# How We Solve Integer to English Words

Convert three-digit chunks and append scale words.

## Steps

1. Return `Zero` for input 0.
2. Split the number into chunks of up to three digits.
3. Convert each chunk with ones, tens, and hundreds rules.
4. Attach Thousand, Million, or Billion labels as needed.
5. Join the chunk phrases in order.
""",
    "0274_h_index": """# How We Solve H-Index

Bucket counts by citation frequency to find the largest valid h.

## Steps

1. Place each citation into a bucket capped at n.
2. Walk buckets from high to low while accumulating paper counts.
3. When the accumulated count reaches the bucket index, that h works.
4. Return the largest such h.
""",
    "0275_h_index_ii": """# How We Solve H-Index II

Binary search the smallest index whose citation count satisfies h.

## Steps

1. Binary search over the sorted citation array.
2. For a mid index, compute how many papers remain at or after it.
3. If citations[mid] is at least that count, search left.
4. Otherwise search right.
5. Return n minus the final left boundary.
""",
    "0276_paint_fence": """# How We Solve Paint Fence

Dynamic programming counts valid colorings with at most two adjacent same colors.

## Steps

1. Handle n equals 1 or 2 directly with k and k squared.
2. Track totals for the previous two fence lengths.
3. Each new length multiplies the sum of the prior two by k minus 1.
4. Slide the DP window forward for n steps.
5. Return the total for length n.
""",
    "0277_find_the_celebrity": """# How We Solve Find the Celebrity

Eliminate non-celebrities with one pass, then verify the survivor.

## Steps

1. Start with person 0 as the candidate.
2. If the candidate knows someone, that person becomes the new candidate.
3. After elimination, verify everyone knows the candidate.
4. Verify the candidate knows nobody.
5. Return the candidate or -1 if verification fails.
""",
    "0278_first_bad_version": """# How We Solve First Bad Version

Binary search the first version that fails the bad check.

## Steps

1. Set the search range from 1 to n.
2. Test the middle version with `isBadVersion`.
3. If it is bad, search the left half including mid.
4. Otherwise search the right half after mid.
5. Return the left boundary when the range collapses.
""",
    "0279_perfect_squares": """# How We Solve Perfect Squares

Breadth-first search finds the minimum number of square summands.

## Steps

1. Precompute all squares not greater than n.
2. BFS from n with steps equal to squares used so far.
3. Subtract each square and enqueue the remainder.
4. Return the step count when remainder reaches 0.
5. Skip already visited remainders.
""",
    "0280_wiggle_sort": """# How We Solve Wiggle Sort

Swap adjacent elements when the current parity violates the wiggle rule.

## Steps

1. Walk from index 1 to the end.
2. On odd indices, ensure the value is greater than its left neighbor.
3. On even indices, ensure the value is less than its left neighbor.
4. Swap with the left neighbor when a rule is broken.
5. Continue until the array satisfies the wiggle pattern.
""",
    "0281_zigzag_iterator": """# How We Solve Zigzag Iterator

Alternate between two vectors, skipping exhausted lists.

## Steps

1. Track an index and turn for each vector.
2. On `next`, advance the current vector and flip the turn.
3. Skip vectors that are already exhausted.
4. `hasNext` is true while any vector has remaining elements.
""",
    "0282_expression_add_operators": """# How We Solve Expression Add Operators

Backtrack over split points while tracking running value and last term for multiplication.

## Steps

1. Try every substring starting at each index (respect leading-zero rules).
2. On the first number, seed path, value, and previous term.
3. Recurse with plus, minus, or multiply branches.
4. For multiply, undo the previous term before applying the product.
5. Record paths whose final value equals the target.
""",
    "0283_move_zeroes": """# How We Solve Move Zeroes

Compact non-zero values to the front, then fill the rest with zeros.

## Steps

1. Walk the array with a write pointer.
2. Copy each non-zero value to the write position and advance it.
3. Fill remaining slots from the write pointer to the end with zero.
""",
    "0284_peeking_iterator": """# How We Solve Peeking Iterator

Cache one lookahead value so peek does not consume the stream.

## Steps

1. On first peek, read from the underlying iterator into a buffer.
2. Return the buffer on subsequent peeks.
3. On next, return the buffer if present; otherwise read from the iterator.
4. hasNext is true if buffered or the underlying iterator has more.
""",
    "0285_inorder_successor_in_bst": """# How We Solve Inorder Successor in BST

Use the right subtree minimum or the lowest ancestor on the left path.

## Steps

1. If the node has a right child, return the leftmost node in that subtree.
2. Otherwise walk from the root tracking the last node whose value is greater than p.
3. Return that successor or null if none exists.
""",
    "0286_walls_and_gates": """# How We Solve Walls and Gates

Multi-source BFS from every gate fills empty rooms with distance.

## Steps

1. Enqueue all cells with distance zero (gates).
2. BFS to neighbors that are still empty (INF).
3. Set each reached room to parent distance plus one.
4. Stop when the queue is empty.
""",
    "0287_find_the_duplicate_number": """# How We Solve Find the Duplicate Number

Floyd cycle detection on the index-as-pointer graph finds the duplicate.

## Steps

1. Move slow one step and fast two steps until they meet.
2. Reset slow to the start and advance both one step at a time.
3. The meeting point is the duplicate value.
""",
    "0288_unique_word_abbreviation": """# How We Solve Unique Word Abbreviation

Group dictionary words by abbreviation and check uniqueness per key.

## Steps

1. Abbreviate each word as first char, middle length, last char (unchanged if length <= 2).
2. Map abbreviation keys to the set of full words.
3. A query word is unique if its key is unused or maps only to itself.
""",
    "0289_game_of_life": """# How We Solve Game of Life

Encode next state in the second bit while scanning in one pass.

## Steps

1. Count live neighbors using the least significant bit of each cell.
2. Mark cells that should live next by setting bit 1 (value |= 2).
3. Shift every cell right by one bit to finalize the next generation.
""",
    "0290_word_pattern": """# How We Solve Word Pattern

Enforce a bijection between pattern characters and words.

## Steps

1. Split the string into words; reject length mismatches.
2. Map each character to a word and each word to a character.
3. Return false on any conflicting mapping.
4. Return true if every pair is consistent.
""",
    "0291_word_pattern_ii": """# How We Solve Word Pattern II

Backtrack over pattern characters and string splits with bijective mapping.

## Steps

1. If the pattern is exhausted, succeed only when the string is too.
2. If the current character already maps to a word, verify the prefix match.
3. Otherwise try every non-empty substring and assign a new word when unused.
4. Undo assignments on failure and continue searching.
""",
    "0292_nim_game": """# How We Solve Nim Game

You lose when four stones remain on your turn.

## Steps

1. Observe that multiples of four are losing positions.
2. Return true when n is not divisible by four.
""",
    "0293_flip_game": """# How We Solve Flip Game

Scan for every adjacent `++` and build the flipped result.

## Steps

1. Walk the string left to right.
2. When two plus signs appear, replace them with minus signs.
3. Collect each resulting state in any order.
""",
    "0294_flip_game_ii": """# How We Solve Flip Game II

Memoized game theory: a position wins if any move leaves the opponent losing.

## Steps

1. Try every valid flip from the current state.
2. If a move leads to a state the opponent cannot win, return true.
3. Memoize each state to avoid recomputation.
4. Return false when no winning move exists.
""",
    "0295_find_median_from_data_stream": """# How We Solve Find Median from Data Stream

Two heaps keep the lower and upper halves balanced.

## Steps

1. Push each new number into the max-heap for the lower half.
2. Balance by moving the largest lower value to the min-heap upper half.
3. Rebalance sizes so lower has at least as many elements.
4. Return the top of lower or the average of both tops for the median.
""",
    "0296_best_meeting_point": """# How We Solve Best Meeting Point

The optimal meeting point is the median row and median column.

## Steps

1. Collect all friend row and column coordinates.
2. Sort columns and pick medians for rows and columns.
3. Sum Manhattan distances to those medians.
""",
    "0297_serialize_and_deserialize_binary_tree": """# How We Solve Serialize and Deserialize Binary Tree

Level-order BFS with empty markers preserves tree structure.

## Steps

1. Serialize with BFS, writing values and empty placeholders.
2. Trim trailing empties and join with commas.
3. Deserialize by reading the root, then filling children level by level.
""",
    "0298_binary_tree_longest_consecutive_sequence": """# How We Solve Binary Tree Longest Consecutive Sequence

DFS extends the path when a child value is exactly parent plus one.

## Steps

1. At each node, start length 1 or extend from the parent when consecutive.
2. Recurse to both children with the updated length.
3. Return the maximum length seen in the subtree.
""",
    "0299_bulls_and_cows": """# How We Solve Bulls and Cows

Count exact matches separately from digit frequency overlaps.

## Steps

1. Count bulls where secret and guess digits match at the same index.
2. Track unmatched digit frequencies in both strings.
3. Sum min counts per digit for cows.
4. Format the result as bulls A cows B.
""",
    "0300_longest_increasing_subsequence": """# How We Solve Longest Increasing Subsequence

Patience sorting with binary search finds the LIS length.

## Steps

1. Maintain an array of pile tops in increasing order.
2. Binary search for the leftmost pile that can accept each number.
3. Append when the number is larger than all piles.
4. Return the number of piles as the LIS length.
""",
    "0301_remove_invalid_parentheses": """# How We Solve Remove Invalid Parentheses

Breadth-first search removes parentheses level by level until valid strings appear.

## Steps

1. BFS over strings with one parenthesis removed per step.
2. Check validity with a running balance count.
3. Stop expanding deeper once any valid string is found at the current level.
4. Collect all valid strings from that level.
""",
    "0302_smallest_rectangle_enclosing_black_pixels": """# How We Solve Smallest Rectangle Enclosing Black Pixels

Binary search each boundary using the known black pixel as a guide.

## Steps

1. Search left and right column bounds where black pixels exist.
2. Search top and bottom row bounds similarly.
3. Multiply width by height for the enclosing area.
""",
    "0303_range_sum_query_immutable": """# How We Solve Range Sum Query Immutable

Prefix sums answer range queries in constant time.

## Steps

1. Build a prefix array during construction.
2. Return prefix[right+1] minus prefix[left] for each query.
""",
    "0304_range_sum_query_2d_immutable": """# How We Solve Range Sum Query 2D Immutable

Two-dimensional prefix sums support rectangle queries.

## Steps

1. Build a cumulative sum table with inclusion-exclusion.
2. Query any sub-rectangle using four prefix lookups.
""",
    "0305_number_of_islands_ii": """# How We Solve Number of Islands II

Union-find tracks connected land components as cells are added.

## Steps

1. For each new land cell, create a new component.
2. Union with existing land neighbors and decrement count on merges.
3. Append the current island count after each add.
""",
    "0306_additive_number": """# How We Solve Additive Number

Try every split for the first two numbers, then verify the additive chain.

## Steps

1. Enumerate first and second substrings with leading-zero checks.
2. While digits remain, require the next chunk to equal their sum.
3. Return true if the entire string is consumed.
""",
    "0307_range_sum_query_mutable": """# How We Solve Range Sum Query Mutable

A Fenwick tree supports point updates and prefix range sums.

## Steps

1. Initialize the BIT from the input array.
2. Apply updates as deltas to a single index.
3. Answer range sums with two prefix queries.
""",
    "0308_range_sum_query_2d_mutable": """# How We Solve Range Sum Query 2D Mutable

A 2D Fenwick tree handles cell updates and rectangle sums.

## Steps

1. Build the 2D BIT from the matrix.
2. Update one cell by adding its delta through nested loops.
3. Query a rectangle with four 2D prefix sums.
""",
    "0309_best_time_to_buy_and_sell_stock_with_cooldown": """# How We Solve Best Time to Buy and Sell Stock with Cooldown

Track three states: free, holding, and cooldown after selling.

## Steps

1. Iterate prices while updating free, hold, and cooldown profits.
2. Buying moves from free to hold; selling moves from hold to cooldown.
3. Return the best profit among free and cooldown at the end.
""",
    "0310_minimum_height_trees": """# How We Solve Minimum Height Trees

Repeatedly peel leaves to find the tree center(s).

## Steps

1. Build adjacency lists and leaf degrees.
2. Remove all leaves layer by layer until at most two nodes remain.
3. Return the remaining nodes as the minimum-height roots.
""",
    "0311_sparse_matrix_multiplication": """# How We Solve Sparse Matrix Multiplication

Skip zero entries when accumulating dot products.

## Steps

1. For each row of mat1, iterate only nonzero inner indices.
2. Multiply by nonzero entries in the matching row of mat2.
3. Accumulate into the result matrix.
""",
    "0312_burst_balloons": """# How We Solve Burst Balloons

Interval DP treats the last balloon burst in each range as the split point.

## Steps

1. Pad nums with 1 on both ends.
2. Fill DP for increasing interval lengths.
3. Try every last balloon in the range and maximize coins gained.
""",
    "0313_super_ugly_number": """# How We Solve Super Ugly Number

Multiple pointers generate the next super ugly number from given primes.

## Steps

1. Start with ugly list [1] and one pointer per prime.
2. Take the minimum candidate product each step.
3. Advance every pointer that produced that minimum.
""",
    "0314_binary_tree_vertical_order_traversal": """# How We Solve Binary Tree Vertical Order Traversal

BFS groups nodes by column while preserving left-to-right order.

## Steps

1. Queue nodes with their column index starting at root column 0.
2. Append values to each column list in BFS order.
3. Return columns from min to max index.
""",
    "0315_count_of_smaller_numbers_after_self": """# How We Solve Count of Smaller Numbers After Self

Scan right to left and insert into a sorted list to count smaller elements.

## Steps

1. Process nums from end to start.
2. Binary search for insertion position in sorted list.
3. That position is the count of smaller numbers to the right.
""",
    "0316_remove_duplicate_letters": """# How We Solve Remove Duplicate Letters

Monotonic stack builds the lexicographically smallest unique subsequence.

## Steps

1. Track last index of each character.
2. Pop larger stack tops while they appear later.
3. Append current char if not already used.
""",
    "0317_shortest_distance_from_all_buildings": """# How We Solve Shortest Distance from All Buildings

BFS from each building accumulates distance and reach counts on empty cells.

## Steps

1. For every building, BFS across empty land cells.
2. Add distance and increment reach count per cell.
3. Return the minimum distance among cells reached by all buildings.
""",
    "0318_maximum_product_of_word_lengths": """# How We Solve Maximum Product of Word Lengths

Bitmask each word and maximize product when masks do not overlap.

## Steps

1. Build a bitmask for each word without duplicate letters.
2. Compare pairs with no shared bits.
3. Track the maximum length product.
""",
    "0319_bulb_switcher": """# How We Solve Bulb Switcher

Only perfect-square positions remain on after n toggles.

## Steps

1. Observe each bulb toggles once per divisor.
2. Bulbs end on when toggled an odd number of times.
3. Return floor(sqrt(n)).
""",
    "0320_generalized_abbreviation": """# How We Solve Generalized Abbreviation

Backtrack each position to either abbreviate or keep the character.

## Steps

1. At each index, extend the current run length count.
2. Or flush the count and append the literal character.
3. Collect all completed abbreviation strings.
""",
    "0321_create_maximum_number": """# How We Solve Create Maximum Number

Pick the best subsequence from each array, then merge lexicographically.

## Steps

1. Try every split of k digits between the two arrays.
2. Use a monotone stack to pick the largest subsequence of each length.
3. Merge pairs with suffix-aware comparison and keep the maximum.
""",
    "0322_coin_change": """# How We Solve Coin Change

Bottom-up DP finds the minimum coins for each amount.

## Steps

1. Initialize dp[0] = 0 and others to infinity.
2. Relax each coin across all reachable amounts.
3. Return dp[amount] or -1 if unreachable.
""",
    "0323_number_of_connected_components_in_an_undirected_graph": """# How We Solve Number of Connected Components in an Undirected Graph

Union-find merges connected nodes and counts components.

## Steps

1. Start with n components.
2. Union each edge's endpoints when they differ.
3. Decrement the count on successful unions.
""",
    "0324_wiggle_sort_ii": """# How We Solve Wiggle Sort II

Place smaller half at even indices and larger half at odd indices.

## Steps

1. Sort a copy of the array.
2. Fill even indices from the lower median backward.
3. Fill odd indices from the largest values backward.
""",
    "0325_maximum_size_subarray_sum_equals_k": """# How We Solve Maximum Size Subarray Sum Equals k

Prefix sums with earliest index map maximize subarray length.

## Steps

1. Track the first index for each prefix sum.
2. If prefix minus k was seen, update the best length.
3. Return the maximum length found.
""",
    "0326_power_of_three": """# How We Solve Power of Three

Repeated division by three should leave 1 for powers of three.

## Steps

1. Reject non-positive numbers.
2. While divisible by 3, divide n by 3.
3. Return true if the remainder is 1.
""",
    "0327_count_of_range_sum": """# How We Solve Count of Range Sum

Merge sort on prefix sums counts valid range sums in each merge step.

## Steps

1. Build prefix sums starting at zero.
2. During merge sort, count pairs in range [lower, upper].
3. Merge sorted prefix subarrays recursively.
""",
    "0328_odd_even_linked_list": """# How We Solve Odd Even Linked List

Split odd and even index nodes into two lists, then reconnect.

## Steps

1. Walk odd and even pointers in parallel.
2. Link odd nodes to odd nodes and even nodes to even nodes.
3. Attach the even list after the odd list.
""",
    "0329_longest_increasing_path_in_a_matrix": """# How We Solve Longest Increasing Path in a Matrix

DFS with memoization finds the longest strictly increasing path.

## Steps

1. From each cell, explore four directions to higher neighbors.
2. Memoize the best path length starting at each cell.
3. Return the maximum over all starts.
""",
    "0330_patching_array": """# How We Solve Patching Array

Greedy patching extends the reachable range [1, miss).

## Steps

1. While miss is at most n, use the next sorted number if it fits.
2. Otherwise add a patch equal to miss and increment patch count.
3. Extend miss by the added value each step.
""",
    "0331_verify_preorder_serialization_of_a_binary_tree": """# How We Solve Verify Preorder Serialization of a Binary Tree

Slot counting tracks whether the preorder stream can close a valid tree.

## Steps

1. Start with one open slot for the root.
2. Each node consumes one slot; internal nodes add two child slots.
3. Null markers only consume slots. Valid iff slots reach zero at the end.
""",
    "0332_reconstruct_itinerary": """# How We Solve Reconstruct Itinerary

Hierholzer DFS builds the Eulerian path in reverse lexicographic order.

## Steps

1. Push destinations in reverse-sorted order so pop yields lexicographically smallest.
2. DFS from JFK, appending airports after exhausting outgoing edges.
3. Reverse the postorder route to get the itinerary.
""",
    "0333_largest_bst_subtree": """# How We Solve Largest BST Subtree

Post-order DFS returns BST validity, min, max, and subtree size.

## Steps

1. Empty nodes are valid BSTs with neutral bounds.
2. Merge left and right info when values satisfy BST ordering.
3. Track the maximum valid subtree size seen.
""",
    "0334_increasing_triplet_subsequence": """# How We Solve Increasing Triplet Subsequence

Track the smallest first and second values seen so far.

## Steps

1. Update first when the current number is smaller.
2. Else update second when it fits between first and second.
3. Any number greater than second completes a triplet.
""",
    "0335_self_crossing": """# How We Solve Self Crossing

Compare the current segment against earlier segments for intersection patterns.

## Steps

1. Check the classic fourth-line-crosses-first case.
2. Handle equal-width spiral overlap when length is at least five.
3. Handle tight spiral overlap when length is at least six.
""",
    "0336_palindrome_pairs": """# How We Solve Palindrome Pairs

Split each word and pair with reverse halves found in a hash map.

## Steps

1. For every split, test whether the left or right part is a palindrome.
2. Look up the reverse of the other part in the word index.
3. Store pairs in a set to avoid duplicates.
""",
    "0337_house_robber_iii": """# How We Solve House Robber III

Tree DP tracks best sums with and without robbing the current node.

## Steps

1. Post-order traverse left and right children.
2. With-rob adds node value plus both without-rob child sums.
3. Without-rob takes the max side choice from each child.
""",
    "0338_counting_bits": """# How We Solve Counting Bits

Each number inherits one fewer set bit than its cleared-lowest-bit parent.

## Steps

1. Initialize result[0] = 0.
2. For i from 1 to n, copy result[i & (i - 1)].
3. Add one for the bit removed by i & (i - 1).
""",
    "0339_nested_list_weight_sum": """# How We Solve Nested List Weight Sum

DFS accumulates integer values multiplied by current depth.

## Steps

1. Walk each nested list at depth starting at 1.
2. Add integer values times depth.
3. Recurse into nested lists at depth + 1.
""",
    "0340_longest_substring_with_at_most_k_distinct_characters": """# How We Solve Longest Substring with At Most K Distinct Characters

Sliding window shrinks when distinct character count exceeds k.

## Steps

1. Expand right and count characters in the window.
2. While distinct count is greater than k, shrink from the left.
3. Track the maximum valid window length.
""",
    "0341_flatten_nested_list_iterator": """# How We Solve Flatten Nested List Iterator

A stack lazily expands nested lists when the next integer is requested.

## Steps

1. Push top-level items onto a stack in reverse order.
2. Before next/hasNext, peel list nodes until the top is an integer.
3. Pop and return integers; advance through nested children incrementally.
""",
    "0342_power_of_four": """# How We Solve Power of Four

A power of four is a power of two whose single bit sits at an odd index.

## Steps

1. Reject non-positive values.
2. Check exactly one set bit with n & (n - 1) == 0.
3. Confirm n % 3 == 1, which holds for powers of four.
""",
    "0343_integer_break": """# How We Solve Integer Break

Greedy decomposition into threes maximizes the product.

## Steps

1. Handle n <= 3 directly.
2. While n > 4, multiply by 3 and subtract 3.
3. Multiply the remaining n into the result.
""",
    "0344_reverse_string": """# How We Solve Reverse String

Two pointers swap characters in place from both ends.

## Steps

1. Start left at 0 and right at the last index.
2. Swap s[left] and s[right].
3. Move inward until the pointers meet.
""",
    "0345_reverse_vowels_of_a_string": """# How We Solve Reverse Vowels of a String

Two pointers swap only vowel positions.

## Steps

1. Scan from both ends toward the center.
2. Skip non-vowels on each side.
3. Swap vowels and continue inward.
""",
    "0346_moving_average_from_data_stream": """# How We Solve Moving Average from Data Stream

A fixed-size queue maintains the running sum for O(1) averages.

## Steps

1. Append each new value and update total.
2. Drop the oldest value once size exceeds the window.
3. Return total divided by current window length.
""",
    "0347_top_k_frequent_elements": """# How We Solve Top K Frequent Elements

Bucket sort groups values by frequency for linear-time extraction.

## Steps

1. Count frequencies with a hash map.
2. Place values into buckets indexed by count.
3. Scan buckets from highest count until k elements are collected.
""",
    "0348_design_tic_tac_toe": """# How We Solve Design Tic-Tac-Toe

Track row, column, and diagonal scores instead of the full board.

## Steps

1. Add +1 for player 1 and -1 for player 2 on each move.
2. Update row, column, and diagonal counters for the cell.
3. Return the player when any line reaches n in absolute value.
""",
    "0349_intersection_of_two_arrays": """# How We Solve Intersection of Two Arrays

Set intersection returns each distinct shared value once.

## Steps

1. Build sets from both input arrays.
2. Keep values present in both sets.
3. Return the intersection list.
""",
    "0350_intersection_of_two_arrays_ii": """# How We Solve Intersection of Two Arrays II

Frequency counts preserve duplicate intersections.

## Steps

1. Count occurrences in the first array.
2. Walk the second array and emit values with remaining count.
3. Decrement counts as matches are consumed.
""",
    "0351_android_unlock_patterns": """# How We Solve Android Unlock Patterns

Bitmask DFS counts valid patterns with jump constraints on the 3x3 grid.

## Steps

1. Precompute jump middles for knight-like moves.
2. Allow a jump only when the middle cell is still empty.
3. Count corner, edge, and center starts with symmetry multipliers.
""",
    "0352_data_stream_as_disjoint_intervals": """# How We Solve Data Stream as Disjoint Intervals

Maintain merged intervals while inserting each new value.

## Steps

1. Start a singleton interval for the incoming number.
2. Merge overlapping or adjacent intervals during insertion.
3. Return the current interval list on request.
""",
    "0353_design_snake_game": """# How We Solve Design Snake Game

Track snake body in a set and grow only when food is eaten.

## Steps

1. Move the head and reject wall or self collisions.
2. Remove the tail unless the head lands on food.
3. Increment score and advance the food index after eating.
""",
    "0354_russian_doll_envelopes": """# How We Solve Russian Doll Envelopes

Sort by width ascending and height descending, then LIS on heights.

## Steps

1. Sort envelopes to prevent equal-width nesting.
2. Build the longest increasing height subsequence.
3. Return the LIS length as the answer.
""",
    "0355_design_twitter": """# How We Solve Design Twitter

Store tweets by time and merge recent posts from followed users.

## Steps

1. Append each tweet with an increasing timestamp.
2. Collect the latest tweets from self and followees.
3. Return the ten most recent tweet ids.
""",
    "0356_line_reflection": """# How We Solve Line Reflection

Points must pair across the vertical line x = minX + maxX.

## Steps

1. Put all points in a hash set.
2. Compute the reflection target sum of min and max x.
3. Verify every point has its mirrored partner.
""",
    "0357_count_numbers_with_unique_digits": """# How We Solve Count Numbers with Unique Digits

Count valid numbers by length using permutations of available digits.

## Steps

1. Handle n = 0 as the single number zero.
2. Start with ten one-digit numbers including 0.
3. For each extra digit, multiply by remaining digit choices and add.
""",
    "0358_rearrange_string_k_distance_apart": """# How We Solve Rearrange String k Distance Apart

Greedy max-heap placement with a k-step cooldown queue.

## Steps

1. Reject impossible cases using the frequency bound.
2. Always place the most frequent available character next.
3. Requeue used characters after k positions have passed.
""",
    "0359_logger_rate_limiter": """# How We Solve Logger Rate Limiter

Remember the last printed timestamp for each message.

## Steps

1. On a new message, allow printing and store the timestamp.
2. On repeats within ten seconds, reject printing.
3. Allow printing again once ten seconds have elapsed.
""",
    "0360_sort_transformed_array": """# How We Solve Sort Transformed Array

Two pointers merge transformed values from both ends of sorted nums.

## Steps

1. Evaluate the quadratic at the left and right indices.
2. If a > 0, fill the result from the largest values inward.
3. If a < 0, fill from the smallest values outward.
""",
    "0361_bomb_enemy": """# How We Solve Bomb Enemy

Prefix counts of enemies along each row and column avoid repeated scans.

## Steps

1. Sweep each row left/right, counting enemies until a wall.
2. Sweep each column up/down the same way.
3. Place a bomb on empty cells and take the maximum hit total.
""",
    "0362_design_hit_counter": """# How We Solve Design Hit Counter

A queue stores hit timestamps and drops entries older than 300 seconds.

## Steps

1. Append each hit timestamp.
2. On getHits, pop timestamps at or before current time minus 300.
3. Return the remaining queue length.
""",
    "0363_max_sum_of_rectangle_no_larger_than_k": """# How We Solve Max Sum of Rectangle No Larger Than K

Compress rows and use sorted prefix sums to cap subarray sums at k.

## Steps

1. Fix top and bottom rows, accumulating column sums.
2. Track running prefix sums in sorted order.
3. Use lower_bound to find the best prior prefix within the k limit.
""",
    "0364_nested_list_weight_sum_ii": """# How We Solve Nested List Weight Sum II

Weight integers by depth measured from the deepest leaf upward.

## Steps

1. DFS collect each integer with its top-down depth.
2. Find the maximum depth in the structure.
3. Sum value times (maxDepth - depth + 1).
""",
    "0365_water_and_jug_problem": """# How We Solve Water and Jug Problem

Any reachable amount is a multiple of gcd(x, y) up to x + y.

## Steps

1. Reject targets above the combined capacity.
2. Accept target zero immediately.
3. Check target divisibility by gcd(x, y).
""",
    "0366_find_leaves_of_binary_tree": """# How We Solve Find Leaves of Binary Tree

Node height from leaves upward groups nodes removed together.

## Steps

1. DFS compute height where leaves have height 0.
2. Append node values into the bucket for their height.
3. Return buckets from leaves to root in order.
""",
    "0367_valid_perfect_square": """# How We Solve Valid Perfect Square

Binary search finds whether any mid satisfies mid * mid == num.

## Steps

1. Search between 1 and num.
2. Compare square of mid with num.
3. Return true on exact match, false when search ends.
""",
    "0368_largest_divisible_subset": """# How We Solve Largest Divisible Subset

Sorted DP extends chains when larger values divide the previous one.

## Steps

1. Sort nums ascending.
2. For each value, extend any valid smaller divisor chain.
3. Keep the longest chain found.
""",
    "0369_plus_one_linked_list": """# How We Solve Plus One Linked List

Carry only affects the suffix after the rightmost non-nine digit.

## Steps

1. Walk the list, remembering the last node not equal to 9.
2. Increment that node and zero all following nodes.
3. Use a sentinel when the carry creates a new leading digit.
""",
    "0370_range_addition": """# How We Solve Range Addition

A difference array applies range increments in constant time.

## Steps

1. Add inc at start and subtract inc after end for each update.
2. Prefix-sum the difference array.
3. Return the final modified array.
""",
    "0371_sum_of_two_integers": """# How We Solve Sum of Two Integers

Bit addition uses XOR for sum bits and AND-shift for carry.

## Steps

1. Repeat while carry is nonzero.
2. XOR a and b for partial sum, mask to 32 bits.
3. Shift carry left and continue; fix sign for Python ints.
""",
    "0372_super_pow": """# How We Solve Super Pow

Process exponent digits left to right with modular exponentiation.

## Steps

1. Reduce a modulo 1337.
2. For each digit, raise current result to the 10th power mod 1337.
3. Multiply by a to the digit power mod 1337.
""",
    "0373_find_k_pairs_with_smallest_sums": """# How We Solve Find K Pairs with Smallest Sums

A min-heap expands the smallest pair sums greedily.

## Steps

1. Seed the heap with (nums1[i] + nums2[0], i, 0).
2. Pop the smallest pair and append it to the answer.
3. Push the next pair using the same nums1 index and nums2 j + 1.
""",
    "0374_guess_number_higher_or_lower": """# How We Solve Guess Number Higher or Lower

Binary search on the answer range using the guess API.

## Steps

1. Maintain left and right bounds on 1..n.
2. Guess the midpoint and read -1, 0, or 1.
3. Narrow the range until the pick is found.
""",
    "0375_guess_number_higher_or_lower_ii": """# How We Solve Guess Number Higher or Lower II

Interval DP minimizes worst-case guessing cost.

## Steps

1. Fill dp[left][right] for every interval length.
2. Try each guess as the split point.
3. Add guess plus the worse side of the two subproblems.
""",
    "0376_wiggle_subsequence": """# How We Solve Wiggle Subsequence

Track longest wiggle ending up or ending down.

## Steps

1. Start up and down lengths at 1.
2. Extend up when the current value rises from the previous.
3. Extend down when it falls; return the maximum length.
""",
    "0377_combination_sum_iv": """# How We Solve Combination Sum IV

Order-sensitive DP counts ways to reach each target amount.

## Steps

1. Set dp[0] = 1.
2. For each amount, add dp[amount - num] across all nums.
3. Return dp[target].
""",
    "0378_kth_smallest_element_in_a_sorted_matrix": """# How We Solve Kth Smallest Element in a Sorted Matrix

Binary search counts values less than or equal to mid.

## Steps

1. Search the value range from top-left to bottom-right.
2. For each mid, count elements row-wise with a moving column pointer.
3. Move left or right based on whether count is at least k.
""",
    "0379_design_phone_directory": """# How We Solve Design Phone Directory

Track available numbers in a set with deterministic minimum allocation.

## Steps

1. Initialize all slots as available.
2. get removes and returns the smallest available number.
3. check tests availability; release returns a number to the pool.
""",
    "0380_insert_delete_getrandom_o1": """# How We Solve Insert Delete GetRandom O(1)

Array plus index map enables swap-delete in constant time.

## Steps

1. insert appends and records index in a hash map.
2. remove swaps the target with the last element and pops.
3. getRandom reads from the backing array in O(1).
""",
    "0381_insert_delete_getrandom_o1_duplicates_allowed": """# How We Solve Insert Delete GetRandom O(1) - Duplicates Allowed

Track every index per value so duplicates can coexist in the array.

## Steps

1. insert always appends; return false when the value already existed.
2. remove swaps one occurrence with the tail and updates all index sets.
3. getRandom samples from the backing array in O(1).
""",
    "0382_linked_list_random_node": """# How We Solve Linked List Random Node

Reservoir sampling picks each node with equal probability in one pass.

## Steps

1. Walk the list once, collecting node values.
2. On each getRandom call, choose uniformly from the collected nodes.
3. Constructor stores the list head for repeated sampling.
""",
    "0383_ransom_note": """# How We Solve Ransom Note

Count magazine characters and consume them while building the note.

## Steps

1. Build a frequency map from magazine.
2. For each ransom-note character, decrement its count.
3. Return false if any character is unavailable.
""",
    "0384_shuffle_an_array": """# How We Solve Shuffle an Array

Keep the original array and Fisher-Yates shuffle a fresh copy each time.

## Steps

1. Store the initial nums in reset state.
2. reset returns a copy of the original array.
3. shuffle copies original values and applies random permutation.
""",
    "0385_mini_parser": """# How We Solve Mini Parser

Stack-based parsing builds nested lists as brackets open and close.

## Steps

1. If the string is a plain integer, return a NestedInteger wrapper.
2. Push a new list on '[' and attach completed integers on ',' or ']'.
3. Pop finished lists into their parent when ']' closes a segment.
""",
    "0386_lexicographical_numbers": """# How We Solve Lexicographical Numbers

DFS over a 1-9 trie visits numbers in dictionary order.

## Steps

1. Start DFS from 1.
2. Append the current number, then explore current * 10.
3. If the last digit is below 9, also explore current + 1.
""",
    "0387_first_unique_character_in_a_string": """# How We Solve First Unique Character in a String

Two-pass counting finds the earliest character with count one.

## Steps

1. Count every character in the string.
2. Scan left to right for the first count equal to 1.
3. Return -1 when no unique character exists.
""",
    "0388_longest_absolute_file_path": """# How We Solve Longest Absolute File Path

Tab depth tracks directory prefixes on a stack.

## Steps

1. Parse each line and measure depth by tab count.
2. Pop stack until depth matches; directories extend prefix length.
3. For files, add name length to current prefix and track the maximum.
""",
    "0389_find_the_difference": """# How We Solve Find the Difference

XOR cancels matching characters and leaves the extra one.

## Steps

1. XOR every character code in s and t together.
2. The remaining value is the added character's code.
3. Convert that code back to a one-character string.
""",
    "0390_elimination_game": """# How We Solve Elimination Game

Track surviving interval endpoints instead of simulating every removal.

## Steps

1. Maintain left, right, step, and remaining count.
2. Move the active endpoint inward when elimination starts from that side.
3. Halve the interval each round until one number remains.
""",
    "0391_perfect_rectangle": """# How We Solve Perfect Rectangle

Corner XOR and area equality prove a perfect cover without gaps or overlaps.

## Steps

1. Track each rectangle corner in a set, toggling membership on repeats.
2. Accumulate total area and the bounding box extents.
3. Accept only when four outer corners remain and areas match.
""",
    "0392_is_subsequence": """# How We Solve Is Subsequence

Advance through t and consume characters of s in order.

## Steps

1. Keep an index into s.
2. For each character in t, advance when it matches the next needed character.
3. Return true when the index reaches the end of s.
""",
    "0393_utf_8_validation": """# How We Solve UTF-8 Validation

Decode leading byte patterns and verify continuation bytes.

## Steps

1. From each leading byte, determine how many continuation bytes follow.
2. Require each continuation byte to start with the 10 prefix.
3. Reject malformed leads or leftover unfinished sequences.
""",
    "0394_decode_string": """# How We Solve Decode String

A stack stores unfinished prefixes and repeat counts around brackets.

## Steps

1. Accumulate digits into the current repeat count.
2. On '[', push the current string and count, then reset.
3. On ']', pop and expand the decoded segment by the saved count.
""",
    "0395_longest_substring_with_at_least_k_repeating_characters": """# How We Solve Longest Substring with At Least K Repeating Characters

Split on rare characters and recurse into valid segments.

## Steps

1. Count character frequencies in the current string.
2. If any character appears fewer than k times, split on it.
3. Recurse on each part and take the maximum length.
""",
    "0396_rotate_function": """# How We Solve Rotate Function

Use the recurrence relating successive rotations to update F in O(1).

## Steps

1. Compute the initial weighted sum and the total of all values.
2. Each rotation adds sum and subtracts n times the leaving element.
3. Track the maximum F across all rotations.
""",
    "0397_integer_replacement": """# How We Solve Integer Replacement

Greedy parity rules minimize the path from n down to 1.

## Steps

1. Halve even numbers.
2. For odd n, prefer n-1 when n % 4 == 1 or n == 3; otherwise n+1.
3. Count each operation until reaching 1.
""",
    "0398_random_pick_index": """# How We Solve Random Pick Index

Index lists per value enable uniform random selection in O(1).

## Steps

1. Build a map from each value to its occurrence indices.
2. pick chooses uniformly among the stored indices for the target.
3. Constructor stores the mapping once for repeated queries.
""",
    "0399_evaluate_division": """# How We Solve Evaluate Division

Model equations as a weighted directed graph and DFS each query.

## Steps

1. Add both directions of every equation as edge weights.
2. Search for a path from the dividend to the divisor.
3. Multiply edge weights along the path; return -1 when disconnected.
""",
    "0400_nth_digit": """# How We Solve Nth Digit

Skip digit-length buckets until locating the exact digit.

## Steps

1. Subtract counts for 1-digit, 2-digit, ... ranges while n is large.
2. Find the number that contains the remaining digit.
3. Return that digit by its offset inside the number.
""",
    "0401_binary_watch": """# How We Solve Binary Watch

Enumerate valid hour/minute pairs whose LED bit counts sum to turnedOn.

## Steps

1. Loop hours 0-11 and minutes 0-59.
2. Count set bits in both values.
3. Format matching times as H:MM.
""",
    "0402_remove_k_digits": """# How We Solve Remove K Digits

A monotonic increasing stack greedily drops peaks.

## Steps

1. Push digits while removing larger previous digits while removals remain.
2. Trim leftover removals from the end.
3. Strip leading zeros and return "0" if empty.
""",
    "0403_frog_jump": """# How We Solve Frog Jump

Track reachable jump sizes at each stone with a DP set.

## Steps

1. Map every stone to the jump lengths that can land there.
2. From each jump k, try k-1, k, and k+1 forward.
3. Succeed when the last stone receives any jump.
""",
    "0404_sum_of_left_leaves": """# How We Solve Sum of Left Leaves

DFS adds a left child only when that child is a leaf.

## Steps

1. If the left child is a leaf, add its value.
2. Otherwise recurse into the left subtree.
3. Always recurse into the right subtree.
""",
    "0405_convert_a_number_to_hexadecimal": """# How We Solve Convert a Number to Hexadecimal

Treat the value as unsigned and emit nibbles from least significant.

## Steps

1. Mask to 32 bits so negatives use two's complement.
2. Append hex digits for the low 4 bits repeatedly.
3. Reverse the collected digits into the final string.
""",
    "0406_queue_reconstruction_by_height": """# How We Solve Queue Reconstruction by Height

Insert people from tallest to shortest at index k.

## Steps

1. Sort by height descending, then by k ascending.
2. Insert each person at position equal to their k value.
3. Earlier taller people already occupy the correct relative slots.
""",
    "0407_trapping_rain_water_ii": """# How We Solve Trapping Rain Water II

Min-heap BFS grows inward from the border water level.

## Steps

1. Push all border cells into a min-heap as the initial wall.
2. Pop the lowest cell and visit unvisited neighbors.
3. Trap water up to the current wall height and raise the wall inward.
""",
    "0408_valid_word_abbreviation": """# How We Solve Valid Word Abbreviation

Two pointers expand numeric skips and match literal characters.

## Steps

1. Reject leading zeros in number segments.
2. Advance through the word by the parsed count.
3. Require both pointers to finish exactly.
""",
    "0409_longest_palindrome": """# How We Solve Longest Palindrome

Pair identical letters and optionally keep one center character.

## Steps

1. Count frequencies of each character.
2. Add even contributions from every count.
3. Add one more if any odd count remains for the center.
""",
    "0410_split_array_largest_sum": """# How We Solve Split Array Largest Sum

Binary search the minimum feasible largest subarray sum.

## Steps

1. Search between max(nums) and sum(nums).
2. Greedily count how many parts a candidate limit needs.
3. Shrink the search until the smallest valid limit remains.
""",
    "0411_minimum_unique_word_abbreviation": """# How We Solve Minimum Unique Word Abbreviation

DFS builds abbreviations and keeps the shortest valid unique one.

## Steps

1. Match abbreviations against target and dictionary words with two pointers.
2. Recursively choose to skip or reveal each target character.
3. Return the shortest valid abbreviation, breaking ties lexicographically.
""",
    "0412_fizz_buzz": """# How We Solve Fizz Buzz

Check divisibility rules in priority order for each number.

## Steps

1. Iterate from 1 through n.
2. Append FizzBuzz, Fizz, Buzz, or the number itself.
3. Return the full string list.
""",
    "0413_arithmetic_slices": """# How We Solve Arithmetic Slices

Extend each arithmetic run and count new ending slices.

## Steps

1. Compare consecutive differences starting at index 2.
2. Increment the current run length when the difference matches.
3. Add the run length to the total count.
""",
    "0414_third_maximum_number": """# How We Solve Third Maximum Number

Track the three largest distinct values in one pass.

## Steps

1. Skip duplicate values already seen in the top ranks.
2. Shift first, second, and third when a larger value appears.
3. Return third if it exists, otherwise the maximum.
""",
    "0415_add_strings": """# How We Solve Add Strings

Add digits from the end with carry like grade-school addition.

## Steps

1. Walk both strings from the least significant digit.
2. Accumulate carry and append the ones digit.
3. Reverse the collected digits into the result.
""",
    "0416_partition_equal_subset_sum": """# How We Solve Partition Equal Subset Sum

Subset-sum DP checks whether half the total is reachable.

## Steps

1. Reject odd totals immediately.
2. Build reachable sums with each number.
3. Return true when the half-sum target becomes reachable.
""",
    "0417_pacific_atlantic_water_flow": """# How We Solve Pacific Atlantic Water Flow

DFS from both oceans and intersect reachable cells.

## Steps

1. Flood from Pacific borders and Atlantic borders separately.
2. Only move to equal or higher heights.
3. Return coordinates reachable from both oceans.
""",
    "0418_sentence_screen_fitting": """# How We Solve Sentence Screen Fitting

Simulate row filling word by word and count completed sentences.

## Steps

1. Pack words left to right with required spaces.
2. Wrap to the next row when the next word does not fit.
3. Increment the count whenever the word index wraps to zero.
""",
    "0419_battleships_in_a_board": """# How We Solve Battleships in a Board

Count ship heads only at cells with no X above or left.

## Steps

1. Scan every board cell.
2. Ignore X cells that continue a ship horizontally or vertically.
3. Count each remaining X as one battleship.
""",
    "0420_strong_password_checker": """# How We Solve Strong Password Checker

Greedy edits combine length fixes, type fixes, and repeat replacements.

## Steps

1. Count missing character classes and triple-repeat replacements.
2. Insert characters when length is below six.
3. When too long, use deletions to reduce needed replacements and add missing types.
""",
    "0421_maximum_xor_of_two_numbers_in_an_array": """# How We Solve Maximum XOR of Two Numbers in an Array

Build a binary trie of all numbers, then for each value walk the trie preferring the opposite bit at every level.

## Steps

1. Insert every number into a bit trie from the highest set bit down.
2. For each number, greedily choose the complementary bit when a branch exists.
3. Track the maximum XOR value found across all pairs.
""",
    "0422_valid_word_square": """# How We Solve Valid Word Square

A word square is valid when character at `(row, col)` equals character at `(col, row)` for every filled cell.

## Steps

1. Walk each row and column index within the current word.
2. Reject if the mirrored position is out of bounds.
3. Reject on any character mismatch; otherwise the square is valid.
""",
    "0423_reconstruct_original_digits_from_english": """# How We Solve Reconstruct Original Digits from English

English digit words share unique letters, so count digits in a fixed order that removes ambiguity.

## Steps

1. Count letters in the input string.
2. Read digits with unique markers first: zero, two, four, six, eight.
3. Derive remaining digits from leftover letters and output sorted digits.
""",
    "0424_longest_repeating_character_replacement": """# How We Solve Longest Repeating Character Replacement

Use a sliding window that stays valid while replacements needed are at most `k`.

## Steps

1. Expand the right edge and track character frequencies in the window.
2. Keep the count of the dominant character in the window.
3. Shrink from the left while `(window size - dominant count) > k`.
4. Record the longest valid window length.
""",
    "0425_word_squares": """# How We Solve Word Squares

Build word squares row by row with a prefix map so each next word matches required column prefixes.

## Steps

1. Index words by every prefix they contain.
2. DFS row by row, forming the prefix from column letters chosen so far.
3. Try every word matching that prefix and backtrack when the square is complete.
""",
    "0426_convert_binary_search_tree_to_sorted_doubly_linked_list": """# How We Solve Convert BST to Sorted Doubly Linked List

Inorder traversal of a BST visits nodes in sorted order, which is exactly the circular list order.

## Steps

1. Recursively traverse left, then current node, then right.
2. Link the previous inorder node to the current node with `left`/`right` pointers.
3. After traversal, connect head and tail to form a circular doubly linked list.
""",
    "0427_construct_quad_tree": """# How We Solve Construct Quad Tree

Recursively split the grid into four quadrants and merge uniform regions into leaf nodes.

## Steps

1. Base case: a 1x1 cell becomes a leaf with that value.
2. Build the four child quadrants recursively.
3. If all four children are leaves with the same value, return one merged leaf.
4. Otherwise return an internal node pointing to the four children.
""",
    "0428_serialize_and_deserialize_n_ary_tree": """# How We Solve Serialize and Deserialize N-ary Tree

Breadth-first encoding stores each node value, its child count, then its child values in order.

## Steps

1. BFS over the tree, appending `value, childCount, childValues...` for each node.
2. Decode by reading the root record, enqueueing placeholder child nodes.
3. Fill each queued node by reading its own count and child values from the stream.
""",
    "0429_n_ary_tree_level_order_traversal": """# How We Solve N-ary Tree Level Order Traversal

Standard BFS processes one level at a time by snapshotting the queue size before dequeuing.

## Steps

1. Start with the root in a queue.
2. For each level, dequeue exactly the current queue length.
3. Append each node's value and enqueue all of its children.
4. Push the collected level into the result and repeat until empty.
""",
    "0430_flatten_a_multilevel_doubly_linked_list": """# How We Solve Flatten a Multilevel Doubly Linked List

When a node has a child list, flatten it and splice it between the node and its original next node.

## Steps

1. Walk the main list left to right.
2. If a node has `child`, recursively flatten that sublist.
3. Insert the flattened sublist after the current node and reconnect `prev`/`next`.
4. Clear the child pointer and continue from the former next node.
""",
    "0431_encode_n_ary_tree_to_binary_tree": """# How We Solve Encode N-ary Tree to Binary Tree

Map the first N-ary child to the binary `left` pointer and link remaining siblings with `right`.

## Steps

1. Encode: binary left = first child, chain siblings via binary right pointers.
2. Decode: walk the left child and collect every node reached via right links as N-ary children.
3. Round-trip preserves the original tree structure.
""",
    "0432_all_oone_data_structure": """# How We Solve All O`one` Data Structure

Maintain a doubly linked list of count buckets plus a map from keys to their bucket.

## Steps

1. Each bucket stores all keys with the same frequency.
2. `inc` moves a key to the next higher bucket (creating it if needed).
3. `getMaxKey` / `getMinKey` read any key from the tail or head bucket.
""",
    "0433_minimum_genetic_mutation": """# How We Solve Minimum Genetic Mutation

Treat each valid gene as a graph node; edges connect genes one letter apart.

## Steps

1. BFS from the start gene through the bank.
2. Try changing each position to A/C/G/T and enqueue unvisited bank genes.
3. Return the step count when the end gene is reached, or -1 if unreachable.
""",
    "0434_number_of_segments_in_a_string": """# How We Solve Number of Segments in a String

Count contiguous non-space runs in one pass.

## Steps

1. Track whether the current character is inside a segment.
2. Increment the count when a non-space character starts a new segment.
3. Reset the flag on spaces.
""",
    "0435_non_overlapping_intervals": """# How We Solve Non-overlapping Intervals

Greedy interval scheduling: keep intervals that end earliest.

## Steps

1. Sort intervals by end time.
2. Greedily take the next interval that starts at or after the previous end.
3. Count overlaps removed when a start is before the current end.
""",
    "0436_find_right_interval": """# How We Solve Find Right Interval

For each interval start, binary search the smallest start that is at least its end.

## Steps

1. Sort interval starts while remembering original indices.
2. For each interval, binary search the first start >= its end.
3. Return the original index or -1 if none exists.
""",
    "0437_path_sum_iii": """# How We Solve Path Sum III

Prefix sums on root-to-node paths let us count downward paths in O(n).

## Steps

1. DFS while tracking cumulative sum from the root to the current node.
2. Add the count of earlier prefixes equal to `current - target`.
3. Backtrack prefix counts when leaving a node.
""",
    "0438_find_all_anagrams_in_a_string": """# How We Solve Find All Anagrams in a String

Slide a fixed window of length `len(p)` and compare letter frequencies.

## Steps

1. Build the target frequency array for `p`.
2. Expand the window one character at a time in `s`.
3. When window size matches, record the start index if frequencies match.
""",
    "0439_ternary_expression_parser": """# How We Solve Ternary Expression Parser

Find the top-level colon that matches the first question mark, then recurse.

## Steps

1. If there is no `?`, return the single character.
2. Scan for the matching `:` with nesting depth for nested ternaries.
3. Recurse on the true branch if the condition is `T`, otherwise the false branch.
""",
    "0440_k_th_smallest_in_lexicographical_order": """# How We Solve K-th Smallest in Lexicographical Order

Numbers form a 10-ary trie; count how many numbers live under each prefix.

## Steps

1. Start at prefix `1` and treat `k` as steps remaining (0-indexed).
2. Count numbers in the current prefix subtree versus the next sibling prefix.
3. Go deeper (×10) or move to the next sibling (+1) until `k` reaches zero.
""",
    "0441_arranging_coins": """# How We Solve Arranging Coins

Find the largest complete staircase row count whose triangular sum fits in `n`.

## Steps

1. Binary search on the answer `k` in `[0, n]`.
2. Check whether `k * (k + 1) / 2` is at most `n`.
3. Return the maximum valid `k`.
""",
    "0442_find_all_duplicates_in_an_array": """# How We Solve Find All Duplicates in an Array

Use the array itself as a sign bit at each value's index.

## Steps

1. For each number, map to index `abs(num) - 1`.
2. If that slot is already negative, the number is a duplicate.
3. Otherwise negate the value at that index.
""",
    "0443_string_compression": """# How We Solve String Compression

Compress runs in place with read/write pointers.

## Steps

1. Scan each group of identical characters.
2. Write the character, then write count digits when count exceeds one.
3. Return the new compressed length.
""",
    "0444_sequence_reconstruction": """# How We Solve Sequence Reconstruction

Build precedence edges from consecutive pairs in every subsequence, then check for a unique topological order.

## Steps

1. Add directed edges for each adjacent pair (deduplicated).
2. Run Kahn topological sort; fail if the queue ever has more than one choice.
3. Compare the resulting order with `org`.
""",
    "0445_add_two_numbers_ii": """# How We Solve Add Two Numbers II

Push both lists onto stacks so digits can be added from least significant upward.

## Steps

1. Collect all digits from `l1` and `l2` into stacks.
2. Pop while either stack or carry remains, building the result list in reverse.
3. Prepend each new digit node to the answer list.
""",
    "0446_arithmetic_slices_ii_subsequence": """# How We Solve Arithmetic Slices II - Subsequence

Dynamic programming counts arithmetic subsequences ending at each index per difference.

## Steps

1. For each pair `(j, i)`, compute difference `nums[i] - nums[j]`.
2. Add prior counts for that difference at `j` to the answer.
3. Extend the DP map at `i` with new length-2 and longer subsequences.
""",
    "0447_number_of_boomerangs": """# How We Solve Number of Boomerangs

For each anchor point, count how many other points share each squared distance.

## Steps

1. For every ordered triple `(i, j, k)`, distance from `i` to `j` must equal distance from `i` to `k`.
2. Group points by squared distance from the anchor.
3. Add `count * (count - 1)` for each distance bucket.
""",
    "0448_find_all_numbers_disappeared_in_an_array": """# How We Solve Find All Numbers Disappeared in an Array

Mark visited indices in place using negative signs, same idea as finding duplicates.

## Steps

1. For each value, negate the entry at index `abs(value) - 1`.
2. Indices that stay positive correspond to missing numbers `index + 1`.
3. Collect those indices into the result.
""",
    "0449_serialize_and_deserialize_bst": """# How We Solve Serialize and Deserialize BST

Preorder traversal with explicit null markers preserves BST structure.

## Steps

1. Serialize with preorder, writing `#` for null children.
2. Deserialize by reading tokens left-to-right and recursively rebuilding nodes.
3. Round-trip the tree through encode and decode.
""",
    "0450_delete_node_in_a_bst": """# How We Solve Delete Node in a BST

Standard BST deletion with recursive search and inorder successor replacement.

## Steps

1. Recurse left or right until the key matches the current node.
2. If a child is missing, return the other child.
3. Otherwise copy the leftmost value from the right subtree and delete that successor node.
""",
    "0451_sort_characters_by_frequency": """# How We Solve Sort Characters By Frequency

Count characters, then emit them from highest frequency to lowest.

## Steps

1. Build a frequency map for the string.
2. Sort characters by descending count, breaking ties by character code.
3. Repeat each character according to its count and concatenate.
""",
    "0452_minimum_number_of_arrows_to_burst_balloons": """# How We Solve Minimum Number of Arrows to Burst Balloons

Greedy interval covering: sort balloons by end coordinate and shoot when the next start exceeds the current arrow position.

## Steps

1. Sort intervals by their right endpoint.
2. Place the first arrow at the first balloon's end.
3. Extend or add a new arrow whenever a balloon starts after the current arrow position.
""",
    "0453_minimum_moves_to_equal_array_elements": """# How We Solve Minimum Moves to Equal Array Elements

Each increment move raises one element by one, so the minimum target is the array minimum.

## Steps

1. Find the minimum value in the array.
2. Sum the differences between every element and that minimum.
3. That sum equals the minimum number of increment moves.
""",
    "0454_4sum_ii": """# How We Solve 4Sum II

Reduce four arrays to two by hashing all sums from the first pair.

## Steps

1. Count every value of `nums1[i] + nums2[j]`.
2. For each `nums3[k] + nums4[l]`, add the count of `-(that sum)` to the answer.
3. Return the total number of zero-sum quadruples.
""",
    "0455_assign_cookies": """# How We Solve Assign Cookies

Sort children and cookies, then greedily assign the smallest sufficient cookie.

## Steps

1. Sort greed factors and cookie sizes.
2. Walk both arrays with two pointers.
3. When a cookie satisfies the current child, advance the child pointer.
""",
    "0456_132_pattern": """# How We Solve 132 Pattern

Scan from the right while tracking the best candidate for the middle value `3` in a `1-3-2` pattern.

## Steps

1. Maintain a stack of decreasing values as potential `3`s.
2. Track the largest valid middle value seen so far.
3. If a new value is smaller than that middle value, a `132` pattern exists.
""",
    "0457_circular_array_loop": """# How We Solve Circular Array Loop

Detect a cycle that moves in one direction only and has length greater than one.

## Steps

1. For each unvisited index, run fast/slow pointers with consistent direction.
2. Reject cycles of length one or direction changes mid-loop.
3. Mark exhausted paths by zeroing visited indices.
""",
    "0458_poor_pigs": """# How We Solve Poor Pigs

Each pig can distinguish among several test outcomes across rounds; find the minimum pigs needed to cover all buckets.

## Steps

1. Compute how many outcome states one round provides.
2. Each pig multiplies the distinguishable state space by that base.
3. Increase the pig count until capacity is at least the number of buckets.
""",
    "0459_repeated_substring_pattern": """# How We Solve Repeated Substring Pattern

If a string equals repeated copies of a substring, it appears inside its own rotation trick.

## Steps

1. Concatenate the string with itself.
2. Remove the first and last characters of the doubled string.
3. Check whether the original string occurs in that middle section.
""",
    "0460_lfu_cache": """# How We Solve LFU Cache

Track keys in frequency buckets and evict from the least frequently used bucket, breaking ties by LRU order within the bucket.

## Steps

1. Map each key to its value and frequency.
2. Keep lists of keys grouped by frequency, plus the current minimum frequency.
3. On get/put, promote keys to higher-frequency buckets; evict the oldest key in the min bucket when over capacity.
""",
    "0461_hamming_distance": """# How We Solve Hamming Distance

Count the number of set bits in the XOR of the two integers.

## Steps

1. Compute `x ^ y`.
2. Return the population count (number of 1 bits) in the result.
""",
    "0462_minimum_moves_to_equal_array_elements_ii": """# How We Solve Minimum Moves to Equal Array Elements II

The optimal target for minimizing absolute moves is the median.

## Steps

1. Sort the array.
2. Take the middle element as the target median.
3. Sum absolute differences from every element to that median.
""",
    "0463_island_perimeter": """# How We Solve Island Perimeter

Each land cell contributes four edges, minus shared borders with neighbors above and left.

## Steps

1. Scan the grid for land cells (`1`).
2. Add four edges per land cell.
3. Subtract two for each adjacent land neighbor (top or left) to avoid double counting.
""",
    "0464_can_i_win": """# How We Solve Can I Win

Two players pick unused integers from 1..n; use bitmask memoization for game states.

## Steps

1. If the desired total is unreachable by the full sum, the first player loses.
2. Represent chosen numbers as a bitmask state.
3. Memoize whether the current player can force a win from each state.
""",
    "0465_optimal_account_balancing": """# How We Solve Optimal Account Balancing

Net each person's balance, then settle debts with minimum transfers via DFS matching.

## Steps

1. Aggregate net balance per person from all transactions.
2. Keep only non-zero balances.
3. DFS try pairing creditors and debtors to minimize transfer count.
""",
    "0466_count_the_repetitions": """# How We Solve Count The Repetitions

Simulate matching `s2` inside repeated `s1`, then detect cycles to skip bulk repetitions.

## Steps

1. Walk through `n1` copies of `s1`, counting full matches of `s2`.
2. Record `(s2 index, match count)` when a repeat position revisits.
3. Jump ahead using the detected cycle and divide by `n2`.
""",
    "0467_unique_substrings_in_wraparound_string": """# How We Solve Unique Substrings in Wraparound String

Track the longest wraparound substring ending at each letter in the infinite `abc...z` string.

## Steps

1. Extend run length when consecutive letters differ by one modulo 26.
2. Reset length to one when the wraparound chain breaks.
3. Sum the best length per ending letter.
""",
    "0468_validate_ip_address": """# How We Solve Validate IP Address

Validate IPv4 and IPv6 formats separately; return Neither if both fail.

## Steps

1. IPv4: four dot-separated parts, each 0–255 without leading zeros (except `0`).
2. IPv6: eight colon-separated hex groups, each 1–4 hex digits.
3. Return the matching label or Neither.
""",
    "0469_convex_polygon": """# How We Solve Convex Polygon

All turns around the polygon must bend in the same rotational direction.

## Steps

1. Walk consecutive triples of vertices (with wrap-around).
2. Compute the 2D cross product of edge vectors.
3. Require all non-zero cross products to share the same sign.
""",
    "0470_implement_rand10_using_rand7": """# How We Solve Implement Rand10() Using Rand7()

Use rejection sampling on pairs of `rand7()` calls to cover a uniform range up to 40.

## Steps

1. Form `num = (rand7() - 1) * 7 + rand7()` to get 1..49 uniformly.
2. Reject values above 40 to avoid bias.
3. Map accepted values to 1..10 with modulo arithmetic.
""",
    "0471_encode_string_with_shortest_length": """# How We Solve Encode String with Shortest Length

Dynamic programming builds the shortest encoding for each prefix using repeated-substring compression.

## Steps

1. For each substring, try all unit lengths that divide it evenly and encode as `k[unit]`.
2. DP over prefixes: combine shorter encodings with encoded suffixes.
3. Break ties by lexicographic order when lengths are equal.
""",
    "0472_concatenated_words": """# How We Solve Concatenated Words

Process words from shortest to longest and test whether each word can be built from smaller dictionary words.

## Steps

1. Sort words by length so building blocks are available first.
2. Temporarily remove the current word from the dictionary.
3. Run word-break DP to see if the word decomposes into dictionary entries.
""",
    "0473_matchsticks_to_square": """# How We Solve Matchsticks to Square

Partition matchsticks into four equal sides with backtracking.

## Steps

1. Reject if total length is not divisible by four.
2. Sort matchsticks descending to prune early.
3. DFS assign each stick to a side, skipping duplicate side attempts.
""",
    "0474_ones_and_zeroes": """# How We Solve Ones and Zeroes

0/1 knapsack with two capacities: maximum strings using at most m zeros and n ones.

## Steps

1. Count zeros and ones in each string.
2. Update a 2D DP table from back to front for each string.
3. Return the maximum number of strings chosen.
""",
    "0475_heaters": """# How We Solve Heaters

For each house, find the nearest heater with binary search on sorted heater positions.

## Steps

1. Sort heater coordinates.
2. For each house, locate insertion point with binary search.
3. Take the minimum distance to the closest heater on either side.
""",
    "0476_number_complement": """# How We Solve Number Complement

Flip every bit in the binary representation of the number.

## Steps

1. Build a mask covering all bits of `num` by spreading highest set bit.
2. XOR `num` with that mask.
3. Return the complemented value.
""",
    "0477_total_hamming_distance": """# How We Solve Total Hamming Distance

Sum contributions bit by bit instead of comparing every pair.

## Steps

1. For each bit position, count how many numbers have 0 vs 1.
2. Add `zeros * ones` to the answer for that bit.
3. Repeat for all 32 bits.
""",
    "0478_generate_random_point_in_a_circle": """# How We Solve Generate Random Point in a Circle

Rejection sampling inside the bounding square yields uniform points in the disk.

## Steps

1. Sample `(x, y)` uniformly in the square `[-r, r]`.
2. Reject pairs with `x^2 + y^2 > r^2`.
3. Translate accepted points by the circle center and round for output.
""",
    "0479_largest_palindrome_product": """# How We Solve Largest Palindrome Product

Construct palindromes from n-digit prefixes and search for valid factor pairs.

## Steps

1. Build candidate palindromes from descending n-digit numbers.
2. Test divisors downward from the upper n-digit bound.
3. Return the largest valid palindrome product modulo 1337.
""",
    "0480_sliding_window_median": """# How We Solve Sliding Window Median

Maintain a sorted window with binary search insert and delete.

## Steps

1. Sort the initial window of size `k`.
2. Slide by removing the outgoing value and inserting the incoming one with `bisect`.
3. Read the middle element(s) for each window median.
""",
    "0481_magical_string": """# How We Solve Magical String

Generate the self-describing sequence and count ones in the first n characters.

## Steps

1. Start from `[1, 2, 2]` and read counts from index 2 onward.
2. Append one or two alternating values (1/2) according to each count.
3. Return how many `1`s appear in the first `n` elements.
""",
    "0482_license_key_formatting": """# How We Solve License Key Formatting

Normalize characters, then regroup from the left with the special first segment length.

## Steps

1. Remove dashes and uppercase all alphanumeric characters.
2. Let the first group length be `len % k` (or `k` when divisible).
3. Join remaining groups of size `k` with dashes.
""",
    "0483_smallest_good_base": """# How We Solve Smallest Good Base

Search for a base k whose geometric series 1 + k + k² + … equals n.

## Steps

1. Try series lengths from large to small (high exponent first).
2. Binary search base k for each length using the partial sum.
3. Return the first valid k; fallback is n − 1.
""",
    "0484_find_permutation": """# How We Solve Find Permutation

Build the lexicographically smallest permutation matching the I/D pattern with a stack.

## Steps

1. Push numbers sequentially onto a stack.
2. On `I`, pop the stack into the result (a decreasing run ends).
3. After scanning, pop any remaining stack values.
""",
    "0485_max_consecutive_ones": """# How We Solve Max Consecutive Ones

Track the longest run of consecutive 1s in one pass.

## Steps

1. Increment a counter on each 1 and update the best seen.
2. Reset the counter on 0.
3. Return the maximum run length.
""",
    "0486_predict_the_winner": """# How We Solve Predict the Winner

Interval DP stores the score difference the current player can guarantee.

## Steps

1. Base case: single pile gives that pile's value.
2. For wider intervals, take max of picking left or right minus opponent's best reply.
3. Player 1 wins if `dp[0][n-1] >= 0`.
""",
    "0487_max_consecutive_ones_ii": """# How We Solve Max Consecutive Ones II

Sliding window allows at most one zero inside the window.

## Steps

1. Expand the right pointer and count zeros in the window.
2. Shrink from the left while more than one zero is present.
3. Track the maximum window size.
""",
    "0488_zuma_game": """# How We Solve Zuma Game

DFS with memo tries each useful insertion, then repeatedly removes runs of three or more.

## Steps

1. After each insert, shrink the board by deleting consecutive triples.
2. Only insert a hand color next to the same color on the board.
3. Memoize on `(board, hand)` and return minimum steps or −1.
""",
    "0489_robot_room_cleaner": """# How We Solve Robot Room Cleaner

DFS explores reachable cells using only move/turn APIs, backtracking to undo moves.

## Steps

1. Clean the current cell, then try all four directions.
2. Move forward when open, recurse, then reverse turns and move back.
3. Mark visited `(row, col, direction)` states to avoid cycles.
""",
    "0490_the_maze": """# How We Solve The Maze

Model the ball rolling until it hits a wall, then DFS/BFS on stop positions.

## Steps

1. From each cell, slide in four directions until the next cell is blocked.
2. Mark stop cells visited to prevent repeats.
3. Return true if the destination stop is reachable.
""",
    "0491_non_decreasing_subsequences": """# How We Solve Non-decreasing Subsequences

Backtracking builds subsequences of length at least two while skipping duplicates at the same depth.

## Steps

1. Recurse from each start index, only appending non-decreasing values.
2. Skip repeated values at the same recursion level with a local set.
3. Collect subsequences of length ≥ 2 and return them sorted.
""",
    "0492_construct_the_rectangle": """# How We Solve Construct the Rectangle

Find the most square-like factor pair for the given area.

## Steps

1. Iterate width from √area down to 1.
2. When area is divisible by width, length is area / width.
3. Return `[length, width]` with length ≥ width.
""",
    "0493_reverse_pairs": """# How We Solve Reverse Pairs

Count pairs with i < j and nums[i] > 2 * nums[j] during merge sort.

## Steps

1. Recursively split the array and count pairs in each half.
2. For each left element, advance a pointer while the 2× condition holds on the right half.
3. Merge sorted halves and return the total count.
""",
    "0494_target_sum": """# How We Solve Target Sum

Convert ± assignments into counting subsets with a fixed positive sum.

## Steps

1. Check parity and bounds; let `need = (sum(nums) + target) / 2`.
2. DP counts ways to reach each subset sum.
3. Return `dp[need]`.
""",
    "0495_teemo_attacking": """# How We Solve Teemo Attacking

Sum poison durations, capping overlap between consecutive attacks.

## Steps

1. Start with one full duration for the first attack.
2. For each later attack, add min(duration, gap since previous).
3. Return the total poisoned time.
""",
    "0496_next_greater_element_i": """# How We Solve Next Greater Element I

Monotonic stack on nums2 records the next greater value for each element.

## Steps

1. Scan nums2, popping smaller stack values when a larger num appears.
2. Map each popped value to the current num.
3. Answer nums1 using that map, defaulting to −1.
""",
    "0497_random_point_in_non_overlapping_rectangles": """# How We Solve Random Point in Non-overlapping Rectangles

Pick a uniform random integer point using prefix sums over rectangle areas.

## Steps

1. Build cumulative counts of points per rectangle.
2. Choose a global linear index with randomness (mocked in tests).
3. Decode index to `(x, y)` inside the chosen rectangle.
""",
    "0498_diagonal_traverse": """# How We Solve Diagonal Traverse

Simulate walking diagonally up-right and down-left across the matrix.

## Steps

1. Append the current cell, then move along the active diagonal direction.
2. Flip direction at top, bottom, left, or right borders.
3. Continue until all cells are visited.
""",
    "0499_the_maze_iii": """# How We Solve The Maze III

Dijkstra on roll-stop states minimizes distance, breaking ties lexicographically on the path string.

## Steps

1. From each stop cell, roll in four directions until blocked or entering the hole.
2. Push `(distance, path, row, col)` states; skip dominated entries.
3. Return the path when the hole is reached, else `"impossible"`.
""",
    "0500_keyboard_row": """# How We Solve Keyboard Row

Keep words whose letters all lie on a single QWERTY row.

## Steps

1. Map each letter to one of three keyboard rows.
2. Check that every letter in a word belongs to the same row.
3. Return all words that pass the check.
""",
    "0501_find_mode_in_binary_search_tree": """# How We Solve Find Mode in Binary Search Tree

Inorder traversal of a BST counts value frequencies.

## Steps

1. Walk the tree inorder, updating a frequency map.
2. Track the maximum frequency seen.
3. Return every value whose count equals that maximum.
""",
    "0502_ipo": """# How We Solve IPO

Repeatedly take the most profitable affordable project using a max-heap.

## Steps

1. Sort projects by required capital.
2. Push all newly affordable profits into a max-heap.
3. Pop the best profit up to k times and add it to current capital.
""",
    "0503_next_greater_element_ii": """# How We Solve Next Greater Element II

Treat the circular array as doubled length with a decreasing monotonic stack.

## Steps

1. Scan indices `0 .. 2n-1`, using `index % n` for values.
2. Pop smaller stack tops when a larger element appears.
3. Leave `-1` where no greater element exists.
""",
    "0504_base_7": """# How We Solve Base 7

Repeatedly take remainders modulo 7 and build digits in reverse.

## Steps

1. Handle zero and remember the sign separately.
2. Collect `% 7` digits until the number becomes zero.
3. Reverse digits into the final string, restoring the sign.
""",
    "0505_the_maze_ii": """# How We Solve The Maze II

Dijkstra on ball stop positions minimizes rolling distance to the destination.

## Steps

1. From each stop cell, roll in four directions until blocked.
2. Push `(distance, row, col)` into a min-heap for new stops.
3. Return the distance when the destination stop is reached, else `-1`.
""",
    "0506_relative_ranks": """# How We Solve Relative Ranks

Rank athletes by score and map the top three to medal labels.

## Steps

1. Sort indices by descending score.
2. Assign `"Gold Medal"`, `"Silver Medal"`, `"Bronze Medal"` to ranks 1–3.
3. Use numeric strings for all other ranks.
""",
    "0507_perfect_number": """# How We Solve Perfect Number

A perfect number equals the sum of its proper divisors.

## Steps

1. Start with divisor sum 1 for `num > 1`.
2. Add divisor pairs up to √num.
3. Return whether the total equals `num`.
""",
    "0508_most_frequent_subtree_sum": """# How We Solve Most Frequent Subtree Sum

Postorder traversal records each subtree sum and its frequency.

## Steps

1. Compute subtree sums recursively and count them.
2. Find the highest frequency.
3. Return all sums with that frequency, sorted ascending.
""",
    "0509_fibonacci_number": """# How We Solve Fibonacci Number

Iteratively advance two variables through the recurrence.

## Steps

1. Base cases: `F(0)=0`, `F(1)=1`.
2. Update `(prev, curr)` with `curr, prev+curr` for `n` steps.
3. Return the current value.
""",
    "0510_inorder_successor_in_bst_ii": """# How We Solve Inorder Successor in BST II

Use parent pointers without access to the root.

## Steps

1. If the node has a right subtree, return its leftmost node.
2. Otherwise climb parents while the node is a right child.
3. The parent after climbing is the successor, or null if none exists.
""",
    "0511_game_play_analysis_i": """# How We Solve Game Play Analysis I

Aggregate each player's earliest login date with SQL.

## Steps

1. Group the `Activity` table by `player_id`.
2. Take `MIN(event_date)` as `first_login`.
3. Return one row per player.
""",
    "0512_game_play_analysis_ii": """# How We Solve Game Play Analysis II

Join each player's first login row to get the device used that day.

## Steps

1. Subquery the minimum `event_date` per `player_id`.
2. Join back to `Activity` on player and that date.
3. Select `player_id` and `device_id`.
""",
    "0513_find_bottom_left_tree_value": """# How We Solve Find Bottom Left Tree Value

Level-order traversal keeps the first node seen on each row.

## Steps

1. BFS the tree level by level.
2. Record the first value in every level.
3. Return the last recorded value (deepest leftmost).
""",
    "0514_freedom_trail": """# How We Solve Freedom Trail

DP over ring position and key index minimizes rotations plus presses.

## Steps

1. Precompute all ring indices for each character.
2. Recurse on `(ringIndex, keyIndex)` with memoization.
3. Add min clockwise/counter rotation plus one press at each step.
""",
    "0515_find_largest_value_in_each_tree_row": """# How We Solve Find Largest Value in Each Tree Row

Track the maximum node value while BFS walks each level.

## Steps

1. Process the tree level by level.
2. Compare all nodes in the current level.
3. Append the level maximum to the answer.
""",
    "0516_longest_palindromic_subsequence": """# How We Solve Longest Palindromic Subsequence

Interval DP builds palindrome length inside each substring.

## Steps

1. Base case: single characters have length 1.
2. If ends match, add 2 to the inner interval result.
3. Otherwise take the better of dropping either end.
""",
    "0517_super_washing_machines": """# How We Solve Super Washing Machines

Balance clothes evenly using prefix excess and per-machine surplus.

## Steps

1. Return `-1` if total clothes is not divisible by machine count.
2. Track running prefix imbalance while scanning machines.
3. Answer is max of absolute prefix load and any single-machine excess.
""",
    "0518_coin_change_ii": """# How We Solve Coin Change II

Unbounded knapsack DP counts combinations for each amount.

## Steps

1. Initialize `dp[0] = 1`.
2. For each coin, add ways into larger amounts.
3. Return `dp[amount]`.
""",
    "0519_random_flip_matrix": """# How We Solve Random Flip Matrix

Swap-and-pop on remaining cell indices gives uniform random flips.

## Steps

1. Keep a list of unused flattened indices.
2. Pick a random index, map it to `(row, col)`, and swap-remove it.
3. `reset` rebuilds the full index list.
""",
    "0520_detect_capital": """# How We Solve Detect Capital

Valid capitalization is all upper, all lower, or title case only.

## Steps

1. Check whether the whole word is uppercase or lowercase.
2. Otherwise require exactly the first letter to be uppercase.
3. Return true if any allowed pattern matches.
""",
    "0521_longest_uncommon_subsequence_i": """# How We Solve Longest Uncommon Subsequence I

If the strings differ, the longer one cannot be a subsequence of the other when lengths differ; if equal, no uncommon subsequence exists.

## Steps

1. Compare the two strings for equality.
2. Return `-1` when they are identical.
3. Otherwise return the maximum length.
""",
    "0522_longest_uncommon_subsequence_ii": """# How We Solve Longest Uncommon Subsequence II

Keep each string that is not a subsequence of any other string in the list.

## Steps

1. Test each candidate against every other string with a subsequence check.
2. Skip candidates that appear inside another string.
3. Return the maximum remaining length, or `-1`.
""",
    "0523_continuous_subarray_sum": """# How We Solve Continuous Subarray Sum

Prefix sums modulo k reveal repeated remainders at least two indices apart.

## Steps

1. Track the earliest index for each remainder of the running prefix sum.
2. If the same remainder appears again with gap ≥ 2, return true.
3. Handle `k = 0` using raw prefix values.
""",
    "0524_longest_word_in_dictionary_through_deleting": """# How We Solve Longest Word in Dictionary through Deleting

Pick the longest dictionary word that is a subsequence of `s`, breaking ties lexicographically.

## Steps

1. Test each dictionary word as a subsequence of `s`.
2. Prefer longer matches, then smaller strings.
3. Return the best word found.
""",
    "0525_contiguous_array": """# How We Solve Contiguous Array

Map zeros to -1 and ones to +1, then seek the longest zero-sum subarray.

## Steps

1. Track running balance while scanning the array.
2. Store the first index where each balance occurs.
3. Maximize distance between equal balances.
""",
    "0526_beautiful_arrangement": """# How We Solve Beautiful Arrangement

Backtracking counts permutations where index and value divide each other.

## Steps

1. Try placing unused numbers at the current position.
2. Allow the placement only if `i % num == 0` or `num % i == 0`.
3. Count complete permutations.
""",
    "0527_word_abbreviation": """# How We Solve Word Abbreviation

Increase prefix length until every abbreviation is unique and shorter than the original when possible.

## Steps

1. Build `prefix + middle + lastChar` with `middle = len(word) - prefix - 1`.
2. Group words sharing the same abbreviation.
3. Bump prefixes for conflicting groups until all abbreviations differ.
""",
    "0528_random_pick_with_weight": """# How We Solve Random Pick with Weight

Prefix sums turn weighted choice into one binary search.

## Steps

1. Build cumulative weights during construction.
2. Draw a random integer in `[0, total)`.
3. Binary search the prefix array for the chosen index.
""",
    "0529_minesweeper": """# How We Solve Minesweeper

Reveal the clicked cell, then flood-fill empty regions recursively.

## Steps

1. If a mine is clicked, mark it `X`.
2. Otherwise count adjacent mines and write the digit or `B` for zero.
3. Expand DFS when the cell has no neighboring mines.
""",
    "0530_minimum_absolute_difference_in_bst": """# How We Solve Minimum Absolute Difference in BST

Inorder traversal visits BST values in sorted order.

## Steps

1. Walk the tree inorder while remembering the previous value.
2. Update the minimum difference between adjacent visited nodes.
3. Return the smallest gap found.
""",
    "0531_lonely_pixel_i": """# How We Solve Lonely Pixel I

A lonely black pixel has no other black pixels in its row or column.

## Steps

1. Precompute black-pixel counts for every row and column.
2. Scan the grid for cells that are black with count 1 in both dimensions.
3. Return how many such pixels exist.
""",
    "0532_k_diff_pairs_in_an_array": """# How We Solve K-diff Pairs in an Array

Each valid pair differs by exactly `k`, and duplicate values must not create duplicate pairs.

## Steps

1. Count frequency of each number.
2. For `k > 0`, add one pair for each value whose partner `value + k` exists.
3. For `k == 0`, add one pair for each value that appears at least twice.
""",
    "0533_lonely_pixel_ii": """# How We Solve Lonely Pixel II

Here `target` is the required number of black pixels in both the row and column.

## Steps

1. Count black pixels per row and per column.
2. For each black cell meeting the target counts, check that every row with black in that column matches the current row string.
3. Count all qualifying black pixels.
""",
    "0534_game_play_analysis_iii": """# How We Solve Game Play Analysis III

We need a running total of games played per player over time.

## Steps

1. Read rows from `Activity` ordered by player and date.
2. Use a window sum partitioned by `player_id`.
3. Return `player_id`, `event_date`, and the cumulative `games_played_so_far`.
""",
    "0535_encode_and_decode_tinyurl": """# How We Solve Encode and Decode TinyURL

Short URLs must round-trip back to the original long URL.

## Steps

1. Keep bidirectional maps between long URLs and generated short codes.
2. Assign incrementing codes on first encode of a URL.
3. Decode by looking up the short URL in the reverse map.
""",
    "0536_construct_binary_tree_from_string": """# How We Solve Construct Binary Tree from String

The string uses nested parentheses for left and right children.

## Steps

1. Parse the signed integer at the current position.
2. If `(` follows, recursively build the left subtree and consume `)`.
3. Repeat for the right subtree when another `(` appears.
""",
    "0537_complex_number_multiplication": """# How We Solve Complex Number Multiplication

Use `(a+bi)(c+di) = (ac-bd) + (ad+bc)i`.

## Steps

1. Parse real and imaginary parts from both input strings.
2. Apply the complex multiplication formula.
3. Format the result as `real+imaginary i`.
""",
    "0538_convert_bst_to_greater_tree": """# How We Solve Convert BST to Greater Tree

Visit nodes from largest to smallest so each node can absorb all greater values seen so far.

## Steps

1. Traverse the BST in reverse inorder (right, node, left).
2. Maintain a running sum of visited node values.
3. Replace each node value with that running sum.
""",
    "0539_minimum_time_difference": """# How We Solve Minimum Time Difference

Times wrap around midnight, so compare both adjacent sorted times and the circular gap.

## Steps

1. Convert each `HH:MM` string to minutes since midnight.
2. Sort the minute values and take the minimum adjacent difference.
3. Also compare the wrap-around distance across the day boundary.
""",
    "0540_single_element_in_a_sorted_array": """# How We Solve Single Element in a Sorted Array

Pairs occupy even/odd index blocks, so binary search can isolate the singleton.

## Steps

1. Binary search while keeping indices aligned to even positions.
2. If `nums[mid] == nums[mid + 1]`, the unique element is to the right.
3. Otherwise search left; the remaining index holds the answer.
""",
    "0541_reverse_string_ii": """# How We Solve Reverse String II

Reverse the first `k` characters of every `2k` block and leave the rest unchanged.

## Steps

1. Walk the string in steps of `2k`.
2. Reverse characters from the block start through `min(start + k, n)`.
3. Join the characters back into a string.
""",
    "0542_01_matrix": """# How We Solve 01 Matrix

Multi-source BFS from every zero finds the nearest zero for each cell.

## Steps

1. Initialize distances to zero at all `0` cells and enqueue them.
2. Expand in four directions, updating neighbors with a shorter distance.
3. Return the completed distance matrix.
""",
    "0543_diameter_of_binary_tree": """# How We Solve Diameter of Binary Tree

The diameter is the longest path between any two nodes measured in edges.

## Steps

1. Recursively compute each node's left and right subtree depths.
2. At each node, update the best answer with `leftDepth + rightDepth`.
3. Return the maximum diameter found.
""",
    "0544_output_contest_matches": """# How We Solve Output Contest Matches

Tournament pairing repeatedly matches the first remaining team with the last.

## Steps

1. Start with team labels `1..n`.
2. Pair `(first, last)` into `(a,b)` strings for each round.
3. Repeat until one bracket string remains.
""",
    "0545_boundary_of_binary_tree": """# How We Solve Boundary of Binary Tree

The boundary is root, left edge, leaves left-to-right, then right edge reversed.

## Steps

1. Collect the root and traverse the left boundary down non-leaf nodes.
2. Gather all leaf values inorder.
3. Append the right boundary values from bottom to top.
""",
    "0546_remove_boxes": """# How We Solve Remove Boxes

Dynamic programming tracks the best score for a range with trailing same-color boxes.

## Steps

1. Define `dp(l, r, k)` as the max points for `boxes[l..r]` plus `k` extra copies of `boxes[r]`.
2. Either remove the trailing run for `(k+1)^2` points or merge with an earlier matching box.
3. Return the memoized result for the full array.
""",
    "0547_number_of_provinces": """# How We Solve Number of Provinces

Connected cities in the adjacency matrix form provinces.

## Steps

1. Use union-find (or DFS) over city indices.
2. Union cities that are directly connected.
3. Count distinct connected components.
""",
    "0548_split_array_with_equal_sum": """# How We Solve Split Array with Equal Sum

Find indices `i`, `j`, `k` so four separated subarray sums are equal.

## Steps

1. Build prefix sums for the array.
2. For each middle index `j`, store equal first/second segment sums seen so far.
3. Check whether third and fourth segment sums match any stored value.
""",
    "0549_binary_tree_longest_consecutive_sequence_ii": """# How We Solve Binary Tree Longest Consecutive Sequence II

Consecutive paths may go down with difference `+1` or `-1`, including through the parent.

## Steps

1. DFS each node for longest increasing and decreasing chains in its subtrees.
2. Combine left and right chains through the parent when values differ by one.
3. Track the maximum path length anywhere in the tree.
""",
    "0550_game_play_analysis_iv": """# How We Solve Game Play Analysis IV

Measure what fraction of players return the day after their first login.

## Steps

1. Find each player's first login date.
2. Check whether that player has activity on the next calendar day.
3. Divide the count by total players and round to two decimals.
""",
}


def main() -> int:
    config = json.loads((ROOT / "config" / "solved-problems.json").read_text(encoding="utf-8-sig"))
    written = 0
    missing: list[str] = []

    for entry in config["entries"]:
        folder = entry["folder"]
        content = EXPLANATIONS.get(folder)
        if content is None:
            missing.append(folder)
            continue
        path = ROOT / folder / "EXPLANATION.md"
        path.write_text(content.strip() + "\n", encoding="utf-8")
        written += 1

    print(f"Wrote {written} EXPLANATION.md files")
    if missing:
        print("Missing explanations for:", ", ".join(missing))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
