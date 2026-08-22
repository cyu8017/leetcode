// LeetCode 3802 - Number of Ways to Paint Sheets
// https://leetcode.com/problems/number-of-ways-to-paint-sheets/

import "sort"

func numberOfWays(n int, limit []int) int {
	const mod int64 = 1000000007
	sort.Ints(limit)
	points := []int{1, n}
	for _, x := range limit {
		if x+1 > 1 && x+1 < n {
			points = append(points, x+1)
		}
		if n-x > 1 && n-x < n {
			points = append(points, n-x)
		}
	}
	sort.Ints(points)
	unique := points[:0]
	for _, x := range points {
		if len(unique) == 0 || unique[len(unique)-1] != x {
			unique = append(unique, x)
		}
	}
	countGE := func(x int) int64 {
		return int64(len(limit) - sort.SearchInts(limit, x))
	}
	var ans int64
	for i := 0; i+1 < len(unique); i++ {
		x := unique[i]
		a, b := countGE(x), countGE(n-x)
		same := countGE(max3802(x, n-x))
		ways := (a*b - same) % mod
		length := int64(unique[i+1] - x)
		ans = (ans + ways*length) % mod
	}
	if ans < 0 {
		ans += mod
	}
	return int(ans)
}

func max3802(a, b int) int {
	if a > b {
		return a
	}
	return b
}