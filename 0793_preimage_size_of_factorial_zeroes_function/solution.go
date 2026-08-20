// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
// https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

func preimageSizeFZF(k int) int {
	zeros := func(x int) int {
		count := 0
		for x > 0 {
			x /= 5
			count += x
		}
		return count
	}
	firstGE := func(target int) int {
		lo, hi := 0, 5*(target+1)
		for lo < hi {
			mid := (lo + hi) / 2
			if zeros(mid) < target {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		return lo
	}
	if zeros(firstGE(k)) == k {
		return 5
	}
	return 0
}
