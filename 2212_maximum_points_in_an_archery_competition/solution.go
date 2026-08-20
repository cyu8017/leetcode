// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

func maximumBobPoints(numArrows int, aliceArrows []int) []int {
	bestScore, best := -1, make([]int, 12)
	var dfs func(int, int, int, []int)
	dfs = func(i, remain, score int, bob []int) {
		if i == 12 {
			if score > bestScore {
				bestScore = score
				best = append([]int{}, bob...)
				if remain > 0 {
					best[0] += remain
				}
			}
			return
		}
		// skip
		dfs(i+1, remain, score, bob)
		need := aliceArrows[i] + 1
		if remain >= need {
			bob[i] = need
			dfs(i+1, remain-need, score+i, bob)
			bob[i] = 0
		}
	}
	dfs(0, numArrows, 0, make([]int, 12))
	return best
}
