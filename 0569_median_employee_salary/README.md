# 0569. Median Employee Salary

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/median-employee-salary/](https://leetcode.com/problems/median-employee-salary/)
- **Premium:** Yes
- **Tags:** database

## Problem

Table: `Employee`

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| company      | varchar |
| salary       | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the company and the salary of one employee.



Write a solution to find the rows that contain the median salary of each company. While calculating the median, when you sort the salaries of the company, break the ties by `id`.

Return the result table in **any order**.

The result format is in the following example.



**Example 1:**

**Input:**
Employee table:
+----+---------+--------+
| id | company | salary |
+----+---------+--------+
| 1  | A       | 2341   |
| 2  | A       | 341    |
| 3  | A       | 15     |
| 4  | A       | 15314  |
| 5  | A       | 451    |
| 6  | A       | 513    |
| 7  | B       | 15     |
| 8  | B       | 13     |
| 9  | B       | 1154   |
| 10 | B       | 1345   |
| 11 | B       | 1221   |
| 12 | B       | 234    |
| 13 | C       | 2345   |
| 14 | C       | 2645   |
| 15 | C       | 2645   |
| 16 | C       | 2652   |
| 17 | C       | 65     |
+----+---------+--------+
**Output:**
+----+---------+--------+
| id | company | salary |
+----+---------+--------+
| 5  | A       | 451    |
| 6  | A       | 513    |
| 12 | B       | 234    |
| 9  | B       | 1154   |
| 14 | C       | 2645   |
+----+---------+--------+
**Explanation:**
For company A, the rows sorted are as follows:
+----+---------+--------+
| id | company | salary |
+----+---------+--------+
| 3  | A       | 15     |
| 2  | A       | 341    |
| 5  | A       | 451    |



**Follow up:** Could you solve it without using any built-in or window functions?

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Still remember how to select the sum which group by one column?
2. Try to think about how to get the median from a sorted list.
3. How to get the median one item for odd number list while how to get the median two items for even number list, try to unify them.

## Approach

<!-- Describe your solution approach here -->
