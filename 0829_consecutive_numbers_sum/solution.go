// LeetCode 0829 - Consecutive Numbers Sum
// https://leetcode.com/problems/consecutive-numbers-sum/

func consecutiveNumbersSum(n int) int {
	ans, k := 0, 1
	for k*(k-1)/2 < n {
		if (n-k*(k-1)/2)%k == 0 {
			ans++
		}
		k++
	}
	return ans
}
