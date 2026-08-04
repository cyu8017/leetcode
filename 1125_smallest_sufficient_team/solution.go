// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

func smallestSufficientTeam(req_skills []string, people [][]string) []int {
	skillID := map[string]int{}
	for i, s := range req_skills {
		skillID[s] = i
	}
	personMasks := make([]int, len(people))
	for i, skills := range people {
		mask := 0
		for _, skill := range skills {
			mask |= 1 << skillID[skill]
		}
		personMasks[i] = mask
	}
	target := (1 << len(req_skills)) - 1
	const inf = int(^uint(0) >> 1)
	dp := make([]int, 1<<len(req_skills))
	choice := make([]int, 1<<len(req_skills))
	prev := make([]int, 1<<len(req_skills))
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0
	for state := 0; state <= target; state++ {
		if dp[state] == inf {
			continue
		}
		for i, mask := range personMasks {
			ns := state | mask
			if dp[state]+1 < dp[ns] {
				dp[ns] = dp[state] + 1
				choice[ns] = i
				prev[ns] = state
			}
		}
	}
	ans := []int{}
	for state := target; state != 0; state = prev[state] {
		ans = append(ans, choice[state])
	}
	return ans
}
