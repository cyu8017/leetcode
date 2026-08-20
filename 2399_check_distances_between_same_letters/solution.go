// LeetCode 2399 - Check Distances Between Same Letters
// https://leetcode.com/problems/check-distances-between-same-letters/

func checkDistances(s string, distance []int) bool {
	first := make([]int, 26)
	for i := range first {
		first[i] = -1
	}
	for i := 0; i < len(s); i++ {
		c := int(s[i] - 'a')
		if first[c] == -1 {
			first[c] = i
		} else if i-first[c]-1 != distance[c] {
			return false
		}
	}
	return true
}
