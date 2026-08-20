// LeetCode 2038 - Remove Colored Pieces if Both Neighbors are the Same Color
// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

func winnerOfGame(colors string) bool {
	a, b := 0, 0
	for i := 1; i+1 < len(colors); i++ {
		if colors[i-1] == colors[i] && colors[i] == colors[i+1] {
			if colors[i] == 'A' {
				a++
			} else {
				b++
			}
		}
	}
	return a > b
}
