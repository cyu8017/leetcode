// LeetCode 0544 - Output Contest Matches
// https://leetcode.com/problems/output-contest-matches/

import "fmt"

func findContestMatch(n int) string {
	teams := make([]string, n)
	for team := 1; team <= n; team++ {
		teams[team-1] = fmt.Sprintf("%d", team)
	}

	for len(teams) > 1 {
		nextRound := make([]string, 0, len(teams)/2)
		for index := 0; index < len(teams)/2; index++ {
			nextRound = append(nextRound, fmt.Sprintf("(%s,%s)", teams[index], teams[len(teams)-1-index]))
		}
		teams = nextRound
	}

	return teams[0]
}
