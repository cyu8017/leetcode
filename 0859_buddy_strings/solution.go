// LeetCode 0859 - Buddy Strings
// https://leetcode.com/problems/buddy-strings/

func buddyStrings(s string, goal string) bool {
	if len(s) != len(goal) {
		return false
	}
	if s == goal {
		seen := map[byte]bool{}
		for i := 0; i < len(s); i++ {
			if seen[s[i]] {
				return true
			}
			seen[s[i]] = true
		}
		return false
	}
	var diffs [][2]byte
	for i := 0; i < len(s); i++ {
		if s[i] != goal[i] {
			diffs = append(diffs, [2]byte{s[i], goal[i]})
		}
	}
	return len(diffs) == 2 && diffs[0][0] == diffs[1][1] && diffs[0][1] == diffs[1][0]
}
