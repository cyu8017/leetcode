// LeetCode 1535 - Find the Winner of an Array Game
// https://leetcode.com/problems/find-the-winner-of-an-array-game/

func getWinner(arr []int, k int) int {
	champion, wins := arr[0], 0
	for _, challenger := range arr[1:] {
		if champion > challenger {
			wins++
		} else {
			champion, wins = challenger, 1
		}
		if wins == k {
			break
		}
	}
	return champion
}
