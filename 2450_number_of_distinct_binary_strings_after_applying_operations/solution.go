// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

func countDistinctStrings(s string, k int) int {
	const mod = 1000000007
	n := len(s)
	ans := 1
	for i := 0; i < n-k+1; i++ {
		ans = int(int64(ans) * 2 % mod)
	}
	return ans
}
