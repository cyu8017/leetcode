// LeetCode 0070 - Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/

func climbStairs(n int) int {
	if n <= 2 {
		return n
	}

	prev := 1
	curr := 2

	for i := 3; i <= n; i++ {
		prev, curr = curr, prev+curr
	}

	return curr
}
