// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

func uniqueOccurrences(arr []int) bool {
	count := map[int]int{}
	for _, x := range arr {
		count[x]++
	}
	seen := map[int]bool{}
	for _, c := range count {
		if seen[c] {
			return false
		}
		seen[c] = true
	}
	return true
}
