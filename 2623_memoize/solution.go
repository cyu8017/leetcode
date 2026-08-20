// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/


func memoize(fn func(int) int) func(int) int {
	cache := map[int]int{}
	return func(x int) int {
		if v, ok := cache[x]; ok {
			return v
		}
		v := fn(x)
		cache[x] = v
		return v
	}
}
