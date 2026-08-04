// LeetCode 1578 - Minimum Time to Make Rope Colorful
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

func minCost(colors string, neededTime []int) int {
	answer, maximum := 0, 0
	for i, cost := range neededTime {
		if i > 0 && colors[i] != colors[i-1] {
			maximum = 0
		}
		if maximum < cost {
			answer += maximum
			maximum = cost
		} else {
			answer += cost
		}
	}
	return answer
}
