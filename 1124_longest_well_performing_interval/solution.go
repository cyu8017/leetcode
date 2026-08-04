// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

func longestWPI(hours []int) int {
	score := 0
	firstSeen := map[int]int{0: -1}
	ans := 0
	for i, h := range hours {
		if h > 8 {
			score++
		} else {
			score--
		}
		if score > 0 {
			ans = i + 1
		} else if j, ok := firstSeen[score-1]; ok {
			if i-j > ans {
				ans = i - j
			}
		}
		if _, ok := firstSeen[score]; !ok {
			firstSeen[score] = i
		}
	}
	return ans
}
