# 1735. Count Ways to Make Array With Product

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/count-ways-to-make-array-with-product/](https://leetcode.com/problems/count-ways-to-make-array-with-product/)
- **Tags:** array, math, dynamic-programming, combinatorics, number-theory

## Problem

You are given a 2D integer array, `queries`. For each `queries[i]`, where `queries[i] = [n_{i}, k_{i}]`, find the number of different ways you can place positive integers into an array of size `n_{i}` such that the product of the integers is `k_{i}`. As the number of ways may be too large, the answer to the `i^{th}` query is the number of ways **modulo** `10^{9} + 7`.

Return *an integer array *`answer`* where *`answer.length == queries.length`*, and *`answer[i]`* is the answer to the *`i^{th}`* query.*

**Example 1:**

```
**Input:** queries = [[2,6],[5,1],[73,660]]
**Output:** [4,1,50734910]
**Explanation:** Each query is independent.
[2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6], [2,3], [3,2], [6,1].
[5,1]: There is 1 way to fill an array of size 5 that multiply to 1: [1,1,1,1,1].
[73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to 660. 1050734917 modulo 10^{9} + 7 = 50734910.
```

**Example 2:**

```
**Input:** queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
**Output:** [1,2,3,10,5]
```

**Constraints:**

- `1 <= queries.length <= 10^{4}`

	- `1 <= n_{i}, k_{i} <= 10^{4}`

### Hints

1. Prime-factorize ki and count how many ways you can distribute the primes among the ni positions.
2. After prime factorizing ki, suppose there are x amount of prime factor. There are (x + n - 1) choose (n - 1) ways to distribute the x prime factors into n positions, allowing repetitions.

## Approach

<!-- Describe your solution approach here -->
