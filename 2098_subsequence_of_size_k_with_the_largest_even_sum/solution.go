// LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
// https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

import "sort"

func largestEvenSum(nums []int, k int) int64 {
	sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })
	var sum int64
	for i := 0; i < k; i++ {
		sum += int64(nums[i])
	}
	if sum%2 == 0 {
		return sum
	}
	// need to swap parity
	ans := int64(-1)
	// replace odd in first k with even outside, or even with odd outside
	oddIn, evenIn := -1, -1
	for i := k - 1; i >= 0; i-- {
		if nums[i]%2 == 1 && oddIn == -1 {
			oddIn = i
		}
		if nums[i]%2 == 0 && evenIn == -1 {
			evenIn = i
		}
	}
	oddOut, evenOut := -1, -1
	for i := k; i < len(nums); i++ {
		if nums[i]%2 == 1 && oddOut == -1 {
			oddOut = i
		}
		if nums[i]%2 == 0 && evenOut == -1 {
			evenOut = i
		}
	}
	if oddIn != -1 && evenOut != -1 {
		cand := sum - int64(nums[oddIn]) + int64(nums[evenOut])
		if cand > ans {
			ans = cand
		}
	}
	if evenIn != -1 && oddOut != -1 {
		cand := sum - int64(nums[evenIn]) + int64(nums[oddOut])
		if cand > ans {
			ans = cand
		}
	}
	return ans
}
