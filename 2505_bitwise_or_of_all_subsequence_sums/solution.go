// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

func subsequenceSumOr(nums []int) int64 {
	var ans, prefix int64
	for _, x := range nums {
		prefix += int64(x)
		ans |= int64(x) | prefix
	}
	return ans
}
