// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/

func factorialGenerator(n int) []int {
	ans := make([]int, 0, n)
	cur := 1
	for i := 1; i <= n; i++ {
		cur *= i
		ans = append(ans, cur)
	}
	return ans
}
