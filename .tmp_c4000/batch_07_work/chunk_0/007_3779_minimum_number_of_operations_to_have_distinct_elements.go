// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

func minOperations(nums []int) int {
	st := make(map[int]struct{})
	for i := len(nums) - 1; i >= 0; i-- {
		if _, ok := st[nums[i]]; ok {
			return i/3 + 1
		}
		st[nums[i]] = struct{}{}
	}
	return 0
}
