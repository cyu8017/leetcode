// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

func minOperations(nums []int, k int) (ans int) {
	for _, x := range nums {
		ans = (ans + x) % k
	}
	return
}
