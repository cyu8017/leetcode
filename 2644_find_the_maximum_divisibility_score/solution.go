// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/


func maxDivScore(nums []int, divisors []int) int {
	best, bestScore := divisors[0], -1
	for _, d := range divisors {
		score := 0
		for _, x := range nums {
			if x%d == 0 {
				score++
			}
		}
		if score > bestScore || (score == bestScore && d < best) {
			bestScore = score
			best = d
		}
	}
	return best
}
