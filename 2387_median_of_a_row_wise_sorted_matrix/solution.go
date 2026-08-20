// LeetCode 2387 - Median of a Row Wise Sorted Matrix
// https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

func matrixMedian(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	lo, hi := 1, 1000000
	need := (m*n)/2 + 1
	countLE := func(x int) int {
		cnt := 0
		for _, row := range grid {
			l, r := 0, n
			for l < r {
				mid := (l + r) / 2
				if row[mid] <= x {
					l = mid + 1
				} else {
					r = mid
				}
			}
			cnt += l
		}
		return cnt
	}
	for lo < hi {
		mid := (lo + hi) / 2
		if countLE(mid) >= need {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
