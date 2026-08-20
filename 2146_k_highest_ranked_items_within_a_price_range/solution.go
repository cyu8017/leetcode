// LeetCode 2146 - K Highest Ranked Items Within a Price Range
// https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

import "sort"

func highestRankedKItems(grid [][]int, pricing []int, start []int, k int) [][]int {
	m, n := len(grid), len(grid[0])
	low, high := pricing[0], pricing[1]
	type item struct{ dist, price, r, c int }
	vis := make([][]bool, m)
	for i := range vis {
		vis[i] = make([]bool, n)
	}
	q := [][3]int{{start[0], start[1], 0}}
	vis[start[0]][start[1]] = true
	cands := []item{}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		r, c, d := cur[0], cur[1], cur[2]
		if grid[r][c] >= low && grid[r][c] <= high {
			cands = append(cands, item{d, grid[r][c], r, c})
		}
		for _, dir := range dirs {
			nr, nc := r+dir[0], c+dir[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && !vis[nr][nc] && grid[nr][nc] != 0 {
				vis[nr][nc] = true
				q = append(q, [3]int{nr, nc, d + 1})
			}
		}
	}
	sort.Slice(cands, func(i, j int) bool {
		a, b := cands[i], cands[j]
		if a.dist != b.dist {
			return a.dist < b.dist
		}
		if a.price != b.price {
			return a.price < b.price
		}
		if a.r != b.r {
			return a.r < b.r
		}
		return a.c < b.c
	})
	if k > len(cands) {
		k = len(cands)
	}
	ans := make([][]int, k)
	for i := 0; i < k; i++ {
		ans[i] = []int{cands[i].r, cands[i].c}
	}
	return ans
}
