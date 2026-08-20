// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/


import "sort"

func maxCount(banned []int, n int, maxSum int64) int {
	sort.Ints(banned)
	uniq := []int{}
	for _, x := range banned {
		if x >= 1 && x <= n && (len(uniq) == 0 || uniq[len(uniq)-1] != x) {
			uniq = append(uniq, x)
		}
	}
	ans := 0
	prev, remain := 0, maxSum
	check := func(l, r int64) {
		if l > r || remain <= 0 {
			return
		}
		// take as many from l..r as possible under remain
		lo, hi := l, r
		best := l - 1
		for lo <= hi {
			mid := (lo + hi) / 2
			cnt := mid - l + 1
			sum := (l + mid) * cnt / 2
			if sum <= remain {
				best = mid
				lo = mid + 1
			} else {
				hi = mid - 1
			}
		}
		if best >= l {
			cnt := int(best - l + 1)
			ans += cnt
			remain -= (l + best) * int64(cnt) / 2
		}
	}
	for _, b := range uniq {
		check(int64(prev+1), int64(b-1))
		prev = b
	}
	check(int64(prev+1), int64(n))
	return ans
}
