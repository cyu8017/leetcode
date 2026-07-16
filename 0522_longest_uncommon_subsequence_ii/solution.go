// LeetCode 0522 - Longest Uncommon Subsequence II
// https://leetcode.com/problems/longest-uncommon-subsequence-ii/

func findLUSlength(strs []string) int {
	isSubsequence := func(target, source string) bool {
		index := 0
		for _, ch := range source {
			if index < len(target) && target[index] == byte(ch) {
				index++
			}
		}
		return index == len(target)
	}

	result := -1
	for i, candidate := range strs {
		uncommon := true
		for j, other := range strs {
			if i != j && isSubsequence(candidate, other) {
				uncommon = false
				break
			}
		}
		if uncommon && len(candidate) > result {
			result = len(candidate)
		}
	}
	return result
}
