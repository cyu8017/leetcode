// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

func transformArray(nums []int) []int {
	for i, x := range nums {
		nums[i] = x % 2
	}
	// sort: zeros then ones
	j := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			nums[i], nums[j] = nums[j], nums[i]
			j++
		}
	}
	return nums
}
