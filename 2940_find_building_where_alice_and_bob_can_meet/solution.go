// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

func leftmostBuildingQueries(heights []int, queries [][]int) []int {
	ans := make([]int, len(queries))
	for i := range ans {
		ans[i] = -1
	}
	type item struct{ h, qi int }
	buckets := make([][]item, len(heights))
	for qi, q := range queries {
		a, b := q[0], q[1]
		if a > b {
			a, b = b, a
		}
		if a == b || heights[a] < heights[b] {
			ans[qi] = b
			continue
		}
		buckets[b] = append(buckets[b], item{heights[a], qi})
	}
	st := [][2]int{} // height, index
	for i := len(heights) - 1; i >= 0; i-- {
		for _, it := range buckets[i] {
			lo, hi := 0, len(st)-1
			pos := -1
			for lo <= hi {
				mid := (lo + hi) / 2
				if st[mid][0] > it.h {
					pos = st[mid][1]
					lo = mid + 1
				} else {
					hi = mid - 1
				}
			}
			ans[it.qi] = pos
		}
		for len(st) > 0 && st[len(st)-1][0] <= heights[i] {
			st = st[:len(st)-1]
		}
		st = append(st, [2]int{heights[i], i})
	}
	return ans
}
