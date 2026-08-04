// LeetCode 1423 - Maximum Points You Can Obtain from Cards
// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

func maxScore(cardPoints []int, k int) int {
	total := 0
	for _, v := range cardPoints {
		total += v
	}
	if k == len(cardPoints) {
		return total
	}
	window := len(cardPoints) - k
	current := 0
	for i := 0; i < window; i++ {
		current += cardPoints[i]
	}
	smallest := current
	for i := window; i < len(cardPoints); i++ {
		current += cardPoints[i] - cardPoints[i-window]
		if current < smallest {
			smallest = current
		}
	}
	return total - smallest
}
