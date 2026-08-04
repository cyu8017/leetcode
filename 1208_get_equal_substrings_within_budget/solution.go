// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

func equalSubstring(s string, t string, maxCost int) int {
	left, cost, answer := 0, 0, 0
	for right := 0; right < len(s); right++ {
		diff := int(s[right]) - int(t[right])
		if diff < 0 {
			diff = -diff
		}
		cost += diff
		for cost > maxCost {
			d := int(s[left]) - int(t[left])
			if d < 0 {
				d = -d
			}
			cost -= d
			left++
		}
		if right-left+1 > answer {
			answer = right - left + 1
		}
	}
	return answer
}
