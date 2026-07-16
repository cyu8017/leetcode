# 2250. Count Number of Rectangles Containing Each Point

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/](https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/)
- **Tags:** array, hash-table, binary-search, binary-indexed-tree, sorting

## Problem

You are given a 2D integer array `rectangles` where `rectangles[i] = [l_{i}, h_{i}]` indicates that `i^{th}` rectangle has a length of `l_{i}` and a height of `h_{i}`. You are also given a 2D integer array `points` where `points[j] = [x_{j}, y_{j}]` is a point with coordinates `(x_{j}, y_{j})`.

The `i^{th}` rectangle has its **bottom-left corner** point at the coordinates `(0, 0)` and its **top-right corner** point at `(l_{i}, h_{i})`.

Return* an integer array *`count`* of length *`points.length`* where *`count[j]`* is the number of rectangles that **contain** the *`j^{th}`* point.*

The `i^{th}` rectangle **contains** the `j^{th}` point if `0 <= x_{j} <= l_{i}` and `0 <= y_{j} <= h_{i}`. Note that points that lie on the **edges** of a rectangle are also considered to be contained by that rectangle.

**Example 1:**

```
**Input:** rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
**Output:** [2,1]
**Explanation:**
The first rectangle contains no points.
The second rectangle contains only the point (2, 1).
The third rectangle contains the points (2, 1) and (1, 4).
The number of rectangles that contain the point (2, 1) is 2.
The number of rectangles that contain the point (1, 4) is 1.
Therefore, we return [2, 1].
```

**Example 2:**

```
**Input:** rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]
**Output:** [1,3]
**Explanation:
**The first rectangle contains only the point (1, 1).
The second rectangle contains only the point (1, 1).
The third rectangle contains the points (1, 3) and (1, 1).
The number of rectangles that contain the point (1, 3) is 1.
The number of rectangles that contain the point (1, 1) is 3.
Therefore, we return [1, 3].
```

**Constraints:**

- `1 <= rectangles.length, points.length <= 5 * 10^{4}`

	- `rectangles[i].length == points[j].length == 2`

	- `1 <= l_{i}, x_{j} <= 10^{9}`

	- `1 <= h_{i}, y_{j} <= 100`

	- All the `rectangles` are **unique**.

	- All the `points` are **unique**.

### Hints

1. The heights of the rectangles and the y-coordinates of the points are only at most 100, so for each point, we can iterate over the possible heights of the rectangles that contain a given point.
2. For a given point and height, can we efficiently count how many rectangles with that height contain our point?
3. Sort the rectangles at each height and use binary search.

## Approach

<!-- Describe your solution approach here -->
