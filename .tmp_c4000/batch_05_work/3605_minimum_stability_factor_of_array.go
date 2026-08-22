// LeetCode 3605 - Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/

func minStable(nums []int, maxC int) int {
	n := len(nums)
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	ok := func(x int) bool {
		if x >= n {
			return true
		}
		changes := 0
		i := 0
		for i+x < n {
			g := nums[i]
			for j := i + 1; j <= i+x; j++ {
				g = gcd(g, nums[j])
			}
			if g > 1 {
				changes++
				i += x + 1
			} else {
				i++
			}
		}
		return changes <= maxC
	}
	lo, hi := 0, n
	for lo < hi {
		mid := (lo + hi) / 2
		if ok(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
