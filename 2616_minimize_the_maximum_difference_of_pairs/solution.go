// LeetCode 2616 - Minimize the Maximum Difference of Pairs
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/


import "sort"

func minimizeMax(nums []int, p int) int {
	sort.Ints(nums)
	ok := func(d int) bool {
		cnt := 0
		for i := 0; i+1 < len(nums); {
			if nums[i+1]-nums[i] <= d {
				cnt++
				i += 2
			} else {
				i++
			}
		}
		return cnt >= p
	}
	lo, hi := 0, nums[len(nums)-1]-nums[0]
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
