// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/


func last(nums []interface{}) interface{} {
	if len(nums) == 0 {
		return -1
	}
	return nums[len(nums)-1]
}
