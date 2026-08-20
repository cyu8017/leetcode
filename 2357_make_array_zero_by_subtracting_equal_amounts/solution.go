// LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

func minimumOperations(nums []int) int {
	seen := map[int]bool{}
	for _, x := range nums {
		if x > 0 {
			seen[x] = true
		}
	}
	return len(seen)
}
