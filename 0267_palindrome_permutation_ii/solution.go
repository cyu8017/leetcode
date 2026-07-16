// LeetCode 0267 - Palindrome Permutation II
// https://leetcode.com/problems/palindrome-permutation-ii/

import "sort"

func generatePalindromes(s string) []string {
	counts := make(map[rune]int)
	for _, char := range s {
		counts[char]++
	}

	middle := ""
	var oddChars []rune
	for char, count := range counts {
		if count%2 != 0 {
			oddChars = append(oddChars, char)
		}
	}
	if len(oddChars) > 1 {
		return nil
	}
	if len(oddChars) == 1 {
		middle = string(oddChars[0])
	}

	keys := make([]rune, 0, len(counts))
	for char := range counts {
		keys = append(keys, char)
	}
	sort.Slice(keys, func(i, j int) bool { return keys[i] < keys[j] })

	half := make([]rune, 0, len(s)/2)
	for _, char := range keys {
		for i := 0; i < counts[char]/2; i++ {
			half = append(half, char)
		}
	}

	result := []string{}
	used := make([]bool, len(half))
	path := make([]rune, 0, len(half))

	var backtrack func()
	backtrack = func() {
		if len(path) == len(half) {
			prefix := string(path)
			runes := []rune(prefix)
			for left, right := 0, len(runes)-1; left < right; left, right = left+1, right-1 {
				runes[left], runes[right] = runes[right], runes[left]
			}
			result = append(result, prefix+middle+string(runes))
			return
		}
		for index, char := range half {
			if used[index] {
				continue
			}
			if index > 0 && half[index] == half[index-1] && !used[index-1] {
				continue
			}
			used[index] = true
			path = append(path, char)
			backtrack()
			path = path[:len(path)-1]
			used[index] = false
		}
	}

	backtrack()
	return result
}
