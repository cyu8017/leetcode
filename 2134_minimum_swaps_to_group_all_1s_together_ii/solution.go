// LeetCode 2134 - Minimum Swaps to Group All 1's Together II
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

func minSwaps(nums []int) int {
	ones := 0
	for _, x := range nums {
		ones += x
	}
	if ones == 0 {
		return 0
	}
	n := len(nums)
	window := 0
	for i := 0; i < ones; i++ {
		window += nums[i]
	}
	best := window
	for i := 0; i < n; i++ {
		window -= nums[i]
		window += nums[(i+ones)%n]
		if window > best {
			best = window
		}
	}
	return ones - best
}
