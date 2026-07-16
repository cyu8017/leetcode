// LeetCode 0438 - Find All Anagrams in a String
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

func findAnagrams(s string, p string) []int {
	if len(p) > len(s) {
		return []int{}
	}

	need := make([]int, 26)
	window := make([]int, 26)
	for index := 0; index < len(p); index++ {
		need[p[index]-'a']++
	}

	result := make([]int, 0)
	left := 0
	for right := 0; right < len(s); right++ {
		window[s[right]-'a']++
		if right-left+1 > len(p) {
			window[s[left]-'a']--
			left++
		}
		if slicesEqual(window, need) {
			result = append(result, left)
		}
	}
	return result
}

func slicesEqual(left, right []int) bool {
	if len(left) != len(right) {
		return false
	}
	for index := range left {
		if left[index] != right[index] {
			return false
		}
	}
	return true
}
