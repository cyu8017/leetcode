// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

func findPrimePairs(n int) [][]int {
	isPrime := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		isPrime[i] = true
	}
	for i := 2; i*i <= n; i++ {
		if isPrime[i] {
			for j := i * i; j <= n; j += i {
				isPrime[j] = false
			}
		}
	}
	ans := make([][]int, 0)
	for x := 2; x <= n/2; x++ {
		y := n - x
		if isPrime[x] && isPrime[y] {
			ans = append(ans, []int{x, y})
		}
	}
	return ans
}
