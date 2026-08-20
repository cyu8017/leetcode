// LeetCode 2760 - Longest Even Odd Subarray With Threshold
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

func longestAlternatingSubarray(nums []int, threshold int) int {
	ans := 0
	n := len(nums)
	for i := 0; i < n; i++ {
		if nums[i]%2 != 0 || nums[i] > threshold {
			continue
		}
		j := i
		for j+1 < n && nums[j+1] <= threshold && nums[j+1]%2 != nums[j]%2 {
			j++
		}
		if j-i+1 > ans {
			ans = j - i + 1
		}
	}
	return ans
}
