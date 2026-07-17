// LeetCode 1733 - Minimum Number of People to Teach
// https://leetcode.com/problems/minimum-number-of-people-to-teach/

func minimumTeachings(n int, languages [][]int, friendships [][]int) int {
	users := len(languages)
	knows := make([][]bool, users)
	for user := range knows {
		knows[user] = make([]bool, n+1)
		for _, lang := range languages[user] {
			knows[user][lang] = true
		}
	}
	need := make(map[int]bool)
	for _, friendship := range friendships {
		u, v := friendship[0]-1, friendship[1]-1
		shares := false
		for _, lang := range languages[u] {
			if knows[v][lang] {
				shares = true
				break
			}
		}
		if !shares {
			need[u] = true
			need[v] = true
		}
	}
	if len(need) == 0 {
		return 0
	}
	best := users + 1
	for lang := 1; lang <= n; lang++ {
		teach := 0
		for user := range need {
			if !knows[user][lang] {
				teach++
			}
		}
		if teach < best {
			best = teach
		}
	}
	return best
}
