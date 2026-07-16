// LeetCode 0488 - Zuma Game
// https://leetcode.com/problems/zuma-game/

import "math"

func shrink(s string) string {
	index := 0
	for index < len(s) {
		end := index
		for end < len(s) && s[end] == s[index] {
			end++
		}
		if end-index >= 3 {
			return shrink(s[:index] + s[end:])
		}
		index = end
	}
	return s
}

func findMinStep(board string, hand string) int {
	memo := map[string]int{}
	var dfs func(string, string) int
	dfs = func(b string, h string) int {
		key := b + "#" + h
		if value, ok := memo[key]; ok {
			return value
		}
		b = shrink(b)
		if b == "" {
			memo[key] = 0
			return 0
		}
		best := math.MaxInt32
		for insert := 0; insert <= len(b); insert++ {
			for pick := 0; pick < len(h); pick++ {
				color := h[pick]
				if insert < len(b) && b[insert] == color {
					// allowed
				} else if insert > 0 && b[insert-1] == color {
					// allowed
				} else {
					continue
				}
				nextBoard := shrink(b[:insert] + string(color) + b[insert:])
				if nextBoard == b {
					continue
				}
				nextHand := h[:pick] + h[pick+1:]
				steps := dfs(nextBoard, nextHand)
				if steps != math.MaxInt32 {
					if steps+1 < best {
						best = steps + 1
					}
				}
			}
		}
		memo[key] = best
		return best
	}
	result := dfs(board, hand)
	if result == math.MaxInt32 {
		return -1
	}
	return result
}
