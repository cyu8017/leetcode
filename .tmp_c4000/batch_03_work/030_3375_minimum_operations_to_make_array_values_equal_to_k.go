// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

func minOperations(nums []int, k int) int {
	seen := map[int]bool{}
	for _, x := range nums {
		if x < k {
			return -1
		}
		if x > k {
			seen[x] = true
		}
	}
	return len(seen)
}
