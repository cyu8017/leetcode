// LeetCode 1320 - Minimum Distance to Type a Word Using Two Fingers
// https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

func minimumDistance(word string) int {
	distance := func(a, b int) int {
		if a == 26 {
			return 0
		}
		abs := func(x int) int {
			if x < 0 {
				return -x
			}
			return x
		}
		return abs(a/6-b/6) + abs(a%6-b%6)
	}
	letters := make([]int, len(word))
	for i := range word {
		letters[i] = int(word[i] - 'A')
	}
	dp := map[int]int{26: 0}
	previous := letters[0]
	for idx := 1; idx < len(letters); idx++ {
		current := letters[idx]
		nxt := map[int]int{}
		for free, cost := range dp {
			v1 := cost + distance(previous, current)
			if v, ok := nxt[free]; !ok || v1 < v {
				nxt[free] = v1
			}
			v2 := cost + distance(free, current)
			if v, ok := nxt[previous]; !ok || v2 < v {
				nxt[previous] = v2
			}
		}
		dp = nxt
		previous = current
	}
	ans := int(^uint(0) >> 1)
	for _, v := range dp {
		if v < ans {
			ans = v
		}
	}
	return ans
}
