// LeetCode 2972 - Count the Number of Incremovable Subarrays II
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/

func incremovableSubarrayCount(nums []int) int64 {
	n := len(nums)
	left := 0
	for left+1 < n && nums[left] < nums[left+1] {
		left++
	}
	if left == n-1 {
		return int64(n) * int64(n+1) / 2
	}
	var ans int64 = int64(left + 2)
	right := n - 1
	for right > 0 && (right == n-1 || nums[right] < nums[right+1]) {
		for left >= 0 && nums[left] >= nums[right] {
			left--
		}
		ans += int64(left + 2)
		right--
		if right > 0 && nums[right] >= nums[right+1] {
			break
		}
	}
	return ans
}
