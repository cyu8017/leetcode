// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/


func minCapability(nums []int, k int) int {
	lo, hi := nums[0], nums[0]
	for _, x := range nums {
		if x < lo {
			lo = x
		}
		if x > hi {
			hi = x
		}
	}
	ok := func(cap int) bool {
		cnt := 0
		for i := 0; i < len(nums); {
			if nums[i] <= cap {
				cnt++
				i += 2
			} else {
				i++
			}
		}
		return cnt >= k
	}
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
