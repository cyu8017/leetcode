// LeetCode 0789 - Escape The Ghosts
// https://leetcode.com/problems/escape-the-ghosts/

func escapeGhosts(ghosts [][]int, target []int) bool {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	targetDist := abs(target[0]) + abs(target[1])
	for _, g := range ghosts {
		if abs(g[0]-target[0])+abs(g[1]-target[1]) <= targetDist {
			return false
		}
	}
	return true
}
