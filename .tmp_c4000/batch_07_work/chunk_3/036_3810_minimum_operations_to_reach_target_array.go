// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

func minOperations(nums []int, target []int) int {
	s := make(map[int]struct{})
	for i := 0; i < len(nums); i++ {
		if nums[i] != target[i] {
			s[nums[i]] = struct{}{}
		}
	}
	return len(s)
}
