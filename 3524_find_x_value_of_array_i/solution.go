// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

func resultArray(nums []int, k int) []int64 {
	ans := make([]int64, k)
	dp := make([]int64, k)
	for _, num := range nums {
		newDp := make([]int64, k)
		nm := num % k
		newDp[nm] = 1
		for i := 0; i < k; i++ {
			newDp[(i*nm)%k] += dp[i]
		}
		for i := 0; i < k; i++ {
			ans[i] += newDp[i]
		}
		dp = newDp
	}
	return ans
}
