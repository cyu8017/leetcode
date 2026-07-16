# 1086. High Five

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/high-five/](https://leetcode.com/problems/high-five/)
- **Premium:** Yes
- **Tags:** array, hash-table, sorting, heap-(priority-queue)

## Problem

Given a list of the scores of different students, `items`, where `items[i] = [ID_{i}, score_{i}]` represents one score from a student with `ID_{i}`, calculate each student's **top five average**.

Return *the answer as an array of pairs *`result`*, where *`result[j] = [ID_{j}, topFiveAverage_{j}]`* represents the student with *`ID_{j}`* and their **top five average**. Sort *`result`* by *`ID_{j}`* in **increasing order**.*

A student's **top five average** is calculated by taking the sum of their top five scores and dividing it by `5` using **integer division**.



**Example 1:**

**Input:** items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
**Output:** [[1,87],[2,88]]
**Explanation: **
The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.

**Example 2:**

**Input:** items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
**Output:** [[1,100],[7,100]]



**Constraints:**

	- `1 <= items.length <= 1000`

	- `items[i].length == 2`

	- `1 <= ID_{i} <= 1000`

	- `0 <= score_{i} <= 100`

	- For each `ID_{i}`, there will be **at least** five scores.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. How can we solve the problem if we have just one student?
2. Given an student sort their grades and get the top 5 average.
3. Generalize the idea to do it for many students.

## Approach

<!-- Describe your solution approach here -->
