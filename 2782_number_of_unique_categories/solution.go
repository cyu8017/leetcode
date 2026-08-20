// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

func numberOfCategories(n int, categoryHandler []int) int {
	seen := map[int]bool{}
	for _, c := range categoryHandler {
		seen[c] = true
	}
	return len(seen)
}
