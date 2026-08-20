// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

func canAliceWin(a []string, b []string) bool {
	i, j := 0, 0
	last := byte(0)
	alice := true
	for {
		if alice {
			for i < len(a) && a[i][0] <= last {
				i++
			}
			if i == len(a) {
				return false
			}
			last = a[i][len(a[i])-1]
			i++
		} else {
			for j < len(b) && b[j][0] <= last {
				j++
			}
			if j == len(b) {
				return true
			}
			last = b[j][len(b[j])-1]
			j++
		}
		alice = !alice
	}
}
