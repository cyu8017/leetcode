// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

func maximumInvitations(grid [][]int) int {
	boys := len(grid)
	girls := len(grid[0])
	matchGirl := make([]int, girls)
	for i := range matchGirl {
		matchGirl[i] = -1
	}

	var dfs func(boy int, seen []bool) bool
	dfs = func(boy int, seen []bool) bool {
		for girl := 0; girl < girls; girl++ {
			if grid[boy][girl] == 1 && !seen[girl] {
				seen[girl] = true
				if matchGirl[girl] == -1 || dfs(matchGirl[girl], seen) {
					matchGirl[girl] = boy
					return true
				}
			}
		}
		return false
	}

	ans := 0
	for boy := 0; boy < boys; boy++ {
		seen := make([]bool, girls)
		if dfs(boy, seen) {
			ans++
		}
	}
	return ans
}
