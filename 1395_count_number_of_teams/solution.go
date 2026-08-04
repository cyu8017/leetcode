// LeetCode 1395 - Count Number of Teams
// https://leetcode.com/problems/count-number-of-teams/

func numTeams(rating []int) int {
	ans := 0
	for j, x := range rating {
		ll, lg, rl, rg := 0, 0, 0, 0
		for i := 0; i < j; i++ {
			if rating[i] < x {
				ll++
			} else {
				lg++
			}
		}
		for i := j + 1; i < len(rating); i++ {
			if rating[i] > x {
				rg++
			} else {
				rl++
			}
		}
		ans += ll*rg + lg*rl
	}
	return ans
}
