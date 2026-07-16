# 2155. All Divisions With the Highest Score of a Binary Array

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/](https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/)
- **Tags:** array

## Problem

You are given a **0-indexed** binary array `nums` of length `n`. `nums` can be divided at index `i` (where `0 <= i <= n)` into two arrays (possibly empty) `nums_{left}` and `nums_{right}`:

- `nums_{left}` has all the elements of `nums` between index `0` and `i - 1` **(inclusive)**, while `nums_{right}` has all the elements of nums between index `i` and `n - 1` **(inclusive)**.

	- If `i == 0`, `nums_{left}` is **empty**, while `nums_{right}` has all the elements of `nums`.

	- If `i == n`, `nums_{left}` has all the elements of nums, while `nums_{right}` is **empty**.

The **division score** of an index `i` is the **sum** of the number of `0`'s in `nums_{left}` and the number of `1`'s in `nums_{right}`.

Return **all distinct indices** that have the **highest** possible **division score**. You may return the answer in **any order**.

**Example 1:**

```
**Input:** nums = [0,0,1,0]
**Output:** [2,4]
**Explanation:** Division at index
- 0: nums_{left} is []. nums_{right} is [0,0,**1**,0]. The score is 0 + 1 = 1.
- 1: nums_{left} is [**0**]. nums_{right} is [0,**1**,0]. The score is 1 + 1 = 2.
- 2: nums_{left} is [**0**,**0**]. nums_{right} is [**1**,0]. The score is 2 + 1 = 3.
- 3: nums_{left} is [**0**,**0**,1]. nums_{right} is [0]. The score is 2 + 0 = 2.
- 4: nums_{left} is [**0**,**0**,1,**0**]. nums_{right} is []. The score is 3 + 0 = 3.
Indices 2 and 4 both have the highest possible division score 3.
Note the answer [4,2] would also be accepted.
```

**Example 2:**

```
**Input:** nums = [0,0,0]
**Output:** [3]
**Explanation:** Division at index
- 0: nums_{left} is []. nums_{right} is [0,0,0]. The score is 0 + 0 = 0.
- 1: nums_{left} is [**0**]. nums_{right} is [0,0]. The score is 1 + 0 = 1.
- 2: nums_{left} is [**0**,**0**]. nums_{right} is [0]. The score is 2 + 0 = 2.
- 3: nums_{left} is [**0**,**0**,**0**]. nums_{right} is []. The score is 3 + 0 = 3.
Only index 3 has the highest possible division score 3.
```

**Example 3:**

```
**Input:** nums = [1,1]
**Output:** [0]
**Explanation:** Division at index
- 0: nums_{left} is []. nums_{right} is [**1**,**1**]. The score is 0 + 2 = 2.
- 1: nums_{left} is [1]. nums_{right} is [**1**]. The score is 0 + 1 = 1.
- 2: nums_{left} is [1,1]. nums_{right} is []. The score is 0 + 0 = 0.
Only index 0 has the highest possible division score 2.
```

**Constraints:**

- `n == nums.length`

	- `1 <= n <= 10^{5}`

	- `nums[i]` is either `0` or `1`.

### Hints

1. When you iterate the array, maintain the number of zeros and ones on the left side. Can you quickly calculate the number of ones on the right side?
2. The number of ones on the right side equals the number of ones in the whole array minus the number of ones on the left side.
3. Alternatively, you can quickly calculate it by using a prefix sum array.

## Approach

<!-- Describe your solution approach here -->
