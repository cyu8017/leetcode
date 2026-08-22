// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

func maxSum(nums []int) int {
	seen := map[int]bool{}
	sum := 0
	hasPos := false
	maxNeg := int(-1e9)
	for _, x := range nums {
		if x < 0 {
			if x > maxNeg {
				maxNeg = x
			}
			continue
		}
		hasPos = true
		if !seen[x] {
			seen[x] = true
			sum += x
		}
	}
	if hasPos {
		return sum
	}
	return maxNeg
}
