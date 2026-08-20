// LeetCode 2374 - Node With Highest Edge Score
// https://leetcode.com/problems/node-with-highest-edge-score/

func edgeScore(edges []int) int {
	n := len(edges)
	score := make([]int64, n)
	for i, to := range edges {
		score[to] += int64(i)
	}
	ans := 0
	for i := 1; i < n; i++ {
		if score[i] > score[ans] {
			ans = i
		}
	}
	return ans
}
