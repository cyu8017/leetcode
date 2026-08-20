// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

func longestSquareStreak(nums []int) int {
	set := map[int]bool{}
	for _, x := range nums {
		set[x] = true
	}
	best := -1
	for _, x := range nums {
		if !set[x] {
			continue
		}
		length := 0
		cur := x
		for set[cur] {
			length++
			delete(set, cur)
			if cur > 100000 {
				break
			}
			cur = cur * cur
		}
		if length >= 2 && length > best {
			best = length
		}
	}
	return best
}
