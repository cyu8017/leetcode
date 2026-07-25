// LeetCode 1646 - Get Maximum in Generated Array
// https://leetcode.com/problems/get-maximum-in-generated-array/

func getMaximumGenerated(n int) int {
	if n < 2 {
		return n
	}
	a := make([]int, n+1)
	a[1] = 1
	ans := 1
	for i := 2; i <= n; i++ {
		if i%2 == 0 {
			a[i] = a[i/2]
		} else {
			a[i] = a[i/2] + a[i/2+1]
		}
		if a[i] > ans {
			ans = a[i]
		}
	}
	return ans
}
