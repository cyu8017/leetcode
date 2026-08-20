// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/


func circularGameLosers(n int, k int) []int {
	seen := make([]bool, n)
	i, step := 0, 1
	for !seen[i] {
		seen[i] = true
		i = (i + step*k) % n
		step++
	}
	ans := []int{}
	for j := 0; j < n; j++ {
		if !seen[j] {
			ans = append(ans, j+1)
		}
	}
	return ans
}
