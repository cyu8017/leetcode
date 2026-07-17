// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

func findingUsersActiveMinutes(logs [][]int, k int) []int {
	userMinutes := make(map[int]map[int]bool)
	for _, log := range logs {
		userID, minute := log[0], log[1]
		if userMinutes[userID] == nil {
			userMinutes[userID] = make(map[int]bool)
		}
		userMinutes[userID][minute] = true
	}

	answer := make([]int, k)
	for _, minutes := range userMinutes {
		uam := len(minutes)
		if uam <= k {
			answer[uam-1]++
		}
	}
	return answer
}
