// LeetCode 1482 - Minimum Number of Days to Make m Bouquets
// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

func minDays(bloomDay []int, m int, k int) int {
	if m*k > len(bloomDay) {
		return -1
	}
	possible := func(day int) bool {
		bouquets, run := 0, 0
		for _, x := range bloomDay {
			if x <= day {
				run++
			} else {
				run = 0
			}
			if run == k {
				bouquets++
				run = 0
			}
		}
		return bouquets >= m
	}
	lo, hi := bloomDay[0], bloomDay[0]
	for _, d := range bloomDay {
		if d < lo {
			lo = d
		}
		if d > hi {
			hi = d
		}
	}
	for lo < hi {
		mid := (lo + hi) / 2
		if possible(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
