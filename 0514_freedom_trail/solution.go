// LeetCode 0514 - Freedom Trail
// https://leetcode.com/problems/freedom-trail/

func findRotateSteps(ring string, key string) int {
	positions := map[byte][]int{}
	for index := 0; index < len(ring); index++ {
		char := ring[index]
		positions[char] = append(positions[char], index)
	}

	memo := map[[2]int]int{}
	var dp func(ringIndex, keyIndex int) int
	dp = func(ringIndex, keyIndex int) int {
		if keyIndex == len(key) {
			return 0
		}
		state := [2]int{ringIndex, keyIndex}
		if value, ok := memo[state]; ok {
			return value
		}

		best := int(^uint(0) >> 1)
		for _, pos := range positions[key[keyIndex]] {
			clockwise := (pos - ringIndex + len(ring)) % len(ring)
			counter := (ringIndex - pos + len(ring)) % len(ring)
			steps := min(clockwise, counter) + 1
			best = min(best, steps+dp(pos, keyIndex+1))
		}
		memo[state] = best
		return best
	}

	return dp(0, 0)
}
