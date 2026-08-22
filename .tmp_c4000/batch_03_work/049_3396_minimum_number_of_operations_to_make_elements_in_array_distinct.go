// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

func minimumOperations(nums []int) int {
	ops := 0
	for {
		seen := map[int]bool{}
		dup := false
		for _, x := range nums {
			if seen[x] {
				dup = true
				break
			}
			seen[x] = true
		}
		if !dup {
			return ops
		}
		if len(nums) <= 3 {
			return ops + 1
		}
		nums = nums[3:]
		ops++
	}
}
