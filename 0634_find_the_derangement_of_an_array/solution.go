// LeetCode 0634 - Find the Derangement of An Array
// https://leetcode.com/problems/find-the-derangement-of-an-array/

func findDerangement(n int) int {
	const mod = 1000000007
	if n == 1 {
		return 0
	}
	prev2, prev1 := 0, 1
	for size := 3; size <= n; size++ {
		prev2, prev1 = prev1, (size-1)*(prev1+prev2)%mod
	}
	if n > 1 {
		return prev1
	}
	return 0
}
