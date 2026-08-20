// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/


func maximizeSum(nums []int, k int) int {
	mx := nums[0]
	for _, x := range nums {
		if x > mx {
			mx = x
		}
	}
	return k*mx + k*(k-1)/2
}
