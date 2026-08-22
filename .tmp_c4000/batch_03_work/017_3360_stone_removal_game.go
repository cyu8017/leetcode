// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

func canAliceWin(n int) bool {
	take := 10
	alice := true
	for n >= take && take > 0 {
		n -= take
		take--
		alice = !alice
	}
	return !alice
}
