// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

func flipgame(fronts []int, backs []int) int {
	same := map[int]bool{}
	for i := range fronts {
		if fronts[i] == backs[i] {
			same[fronts[i]] = true
		}
	}
	best := int(^uint(0) >> 1)
	for _, x := range fronts {
		if !same[x] && x < best {
			best = x
		}
	}
	for _, x := range backs {
		if !same[x] && x < best {
			best = x
		}
	}
	if best == int(^uint(0)>>1) {
		return 0
	}
	return best
}
