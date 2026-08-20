// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

func gcdValues(nums []int, queries []int64) []int {
	maxV := 0
	for _, x := range nums {
		if x > maxV {
			maxV = x
		}
	}
	cnt := make([]int, maxV+1)
	for _, x := range nums {
		cnt[x]++
	}
	divCnt := make([]int64, maxV+1)
	for g := 1; g <= maxV; g++ {
		var c int64
		for m := g; m <= maxV; m += g {
			c += int64(cnt[m])
		}
		divCnt[g] = c * (c - 1) / 2
	}
	exact := make([]int64, maxV+1)
	for g := maxV; g >= 1; g-- {
		exact[g] = divCnt[g]
		for m := 2 * g; m <= maxV; m += g {
			exact[g] -= exact[m]
		}
	}
	pref := make([]int64, maxV+1)
	for g := 1; g <= maxV; g++ {
		pref[g] = pref[g-1] + exact[g]
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		// find smallest g with pref[g] > q
		lo, hi := 1, maxV
		for lo < hi {
			mid := (lo + hi) / 2
			if pref[mid] > q {
				hi = mid
			} else {
				lo = mid + 1
			}
		}
		ans[i] = lo
	}
	return ans
}
