# 2097. Valid Arrangement of Pairs

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/valid-arrangement-of-pairs/](https://leetcode.com/problems/valid-arrangement-of-pairs/)
- **Tags:** array, depth-first-search, graph-theory, eulerian-circuit

## Problem

You are given a **0-indexed** 2D integer array `pairs` where `pairs[i] = [start_{i}, end_{i}]`. An arrangement of `pairs` is **valid** if for every index `i` where `1 <= i < pairs.length`, we have `end_{i-1} == start_{i}`.

Return **any** valid arrangement of *`pairs`.

**Note:** The inputs will be generated such that there exists a valid arrangement of `pairs`.

**Example 1:**

```
**Input:** pairs = [[5,1],[4,5],[11,9],[9,4]]
**Output:** [[11,9],[9,4],[4,5],[5,1]]
**Explanation:
**This is a valid arrangement since end_{i-1} always equals start_{i}.
end_{0} = 9 == 9 = start_{1}
end_{1} = 4 == 4 = start_{2}
end_{2} = 5 == 5 = start_{3}
```

**Example 2:**

```
**Input:** pairs = [[1,3],[3,2],[2,1]]
**Output:** [[1,3],[3,2],[2,1]]
**Explanation:**
This is a valid arrangement since end_{i-1} always equals start_{i}.
end_{0} = 3 == 3 = start_{1}
end_{1} = 2 == 2 = start_{2}
The arrangements [[2,1],[1,3],[3,2]] and [[3,2],[2,1],[1,3]] are also valid.
```

**Example 3:**

```
**Input:** pairs = [[1,2],[1,3],[2,1]]
**Output:** [[1,2],[2,1],[1,3]]
**Explanation:**
This is a valid arrangement since end_{i-1} always equals start_{i}.
end_{0} = 2 == 2 = start_{1}
end_{1} = 1 == 1 = start_{2}
```

**Constraints:**

- `1 <= pairs.length <= 10^{5}`

	- `pairs[i].length == 2`

	- `0 <= start_{i}, end_{i} <= 10^{9}`

	- `start_{i} != end_{i}`

	- No two pairs are exactly the same.

	- There **exists** a valid arrangement of `pairs`.

### Hints

1. Could you convert this into a graph problem?
2. Consider the pairs as edges and each number as a node.
3. We have to find an Eulerian path of this graph. Hierholzer’s algorithm can be used.

## Approach

<!-- Describe your solution approach here -->
