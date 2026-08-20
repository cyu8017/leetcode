// LeetCode 2139 - Minimum Moves to Reach Target Score
// https://leetcode.com/problems/minimum-moves-to-reach-target-score/

func minMoves(target int, maxDoubles int) int {
	ans := 0
	for target > 1 && maxDoubles > 0 {
		if target%2 == 1 {
			target--
			ans++
		} else {
			target /= 2
			maxDoubles--
			ans++
		}
	}
	return ans + target - 1
}
