# 2355. Maximum Number of Books You Can Take

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/maximum-number-of-books-you-can-take/](https://leetcode.com/problems/maximum-number-of-books-you-can-take/)
- **Premium:** Yes
- **Tags:** array, dynamic-programming, stack, monotonic-stack

## Problem

You are given a **0-indexed** integer array `books` of length `n` where `books[i]` denotes the number of books on the `i^{th}` shelf of a bookshelf.

You are going to take books from a **contiguous** section of the bookshelf spanning from `l` to `r` where `0 <= l <= r < n`. For each index `i` in the range `l <= i < r`, you must take **strictly fewer** books from shelf `i` than shelf `i + 1`.

Return *the **maximum** number of books you can take from the bookshelf.*



**Example 1:**

**Input:** books = [8,5,2,7,9]
**Output:** 19
**Explanation:**
- Take 1 book from shelf 1.
- Take 2 books from shelf 2.
- Take 7 books from shelf 3.
- Take 9 books from shelf 4.
You have taken 19 books, so return 19.
It can be proven that 19 is the maximum number of books you can take.

**Example 2:**

**Input:** books = [7,0,3,4,5]
**Output:** 12
**Explanation:**
- Take 3 books from shelf 2.
- Take 4 books from shelf 3.
- Take 5 books from shelf 4.
You have taken 12 books so return 12.
It can be proven that 12 is the maximum number of books you can take.

**Example 3:**

**Input:** books = [8,2,3,7,3,4,0,1,4,3]
**Output:** 13
**Explanation:**
- Take 1 book from shelf 0.
- Take 2 books from shelf 1.
- Take 3 books from shelf 2.
- Take 7 books from shelf 3.
You have taken 13 books so return 13.
It can be proven that 13 is the maximum number of books you can take.



**Constraints:**

	- `1 <= books.length <= 10^{5}`

	- `0 <= books[i] <= 10^{5}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Create a dp array where dp[i] is the maximum number of books you can take if you can only take books from bookshelves 0 to i and you must take books from bookshelf i.
2. Keep taking as many books as you can (i.e. starting from bookshelf i and going backwards, you take arr[i], arr[i] - 1, arr[i] - 2, … books).
3. You may reach an index j where arr[j] < arr[i] - (i - j). Have we already found the maximum number of books you can take from bookshelves 0 to j? How do we quickly find such an index j?
4. Keep a stack of possible indices for j. If x is the number at the top of the stack, keep popping from the stack while arr[x] ≥ arr[i] - (i - x). This is because if the inequality mentioned before is true, x will never be an index j as index i will run out of items first.

## Approach

<!-- Describe your solution approach here -->
