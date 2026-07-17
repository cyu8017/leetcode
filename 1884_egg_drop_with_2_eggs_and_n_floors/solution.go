// LeetCode 1884 - Egg Drop With 2 Eggs and N Floors
// https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

func twoEggDrop(n int) int {
	moves := 0
	covered := 0
	for covered < n {
		moves++
		covered += moves
	}
	return moves
}
