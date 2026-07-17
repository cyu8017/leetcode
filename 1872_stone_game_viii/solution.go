// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/

func stoneGameVIII(stones []int) int {
	n := len(stones)
	for i := 1; i < n; i++ {
		stones[i] += stones[i-1]
	}

	score := stones[n-1]
	for i := n - 2; i > 0; i-- {
		if stones[i]-score > score {
			score = stones[i] - score
		}
	}
	return score
}
