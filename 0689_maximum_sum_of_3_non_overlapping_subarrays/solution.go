// LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

func maxSumOfThreeSubarrays(nums []int, k int) []int {
	n := len(nums)
	windows := n - k + 1
	sums := make([]int, windows)
	total := 0
	for i := 0; i < k; i++ {
		total += nums[i]
	}
	sums[0] = total
	for i := 1; i < windows; i++ {
		total += nums[i+k-1] - nums[i-1]
		sums[i] = total
	}
	left := make([]int, windows)
	best := 0
	for i := 0; i < windows; i++ {
		if sums[i] > sums[best] {
			best = i
		}
		left[i] = best
	}
	right := make([]int, windows)
	best = windows - 1
	for i := windows - 1; i >= 0; i-- {
		if sums[i] >= sums[best] {
			best = i
		}
		right[i] = best
	}
	answer := []int{0, 0, 0}
	bestTotal := -1
	for mid := k; mid < windows-k; mid++ {
		l, r := left[mid-k], right[mid+k]
		cur := sums[l] + sums[mid] + sums[r]
		if cur > bestTotal {
			bestTotal = cur
			answer = []int{l, mid, r}
		}
	}
	return answer
}
