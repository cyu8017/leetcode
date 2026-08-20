// LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

func minimumPossibleSum(n int, target int) int {
	const mod = 1_000_000_007
	m := target / 2
	if n <= m {
		return int(int64(n) * int64(n+1) / 2 % mod)
	}
	sum := int64(m) * int64(m+1) / 2
	remain := n - m
	sum += int64(remain)*int64(target) + int64(remain)*int64(remain-1)/2
	return int(sum % mod)
}
