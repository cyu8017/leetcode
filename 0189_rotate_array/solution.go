// LeetCode 0189 - Rotate Array
// https://leetcode.com/problems/rotate-array/

func rotate(nums []int, k int) {
	k %= len(nums)
	reverse := func(left, right int) {
		for left < right {
			nums[left], nums[right] = nums[right], nums[left]
			left++
			right--
		}
	}
	reverse(0, len(nums)-1)
	reverse(0, k-1)
	reverse(k, len(nums)-1)
}