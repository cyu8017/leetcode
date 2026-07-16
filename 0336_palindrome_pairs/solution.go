// LeetCode 0336 - Palindrome Pairs
// https://leetcode.com/problems/palindrome-pairs/

func palindromePairs(words []string) [][]int {
	wordMap := make(map[string]int, len(words))
	for index, word := range words {
		wordMap[word] = index
	}

	type pair struct {
		left  int
		right int
	}
	seen := make(map[pair]struct{})

	isPalindrome := func(value string) bool {
		left := 0
		right := len(value) - 1
		for left < right {
			if value[left] != value[right] {
				return false
			}
			left++
			right--
		}
		return true
	}

	reverseString := func(value string) string {
		runes := []rune(value)
		for left, right := 0, len(runes)-1; left < right; left, right = left+1, right-1 {
			runes[left], runes[right] = runes[right], runes[left]
		}
		return string(runes)
	}

	for index, word := range words {
		for split := 0; split <= len(word); split++ {
			left := word[:split]
			right := word[split:]
			if isPalindrome(left) {
				reversedRight := reverseString(right)
				if other, ok := wordMap[reversedRight]; ok && other != index {
					seen[pair{other, index}] = struct{}{}
				}
			}
			if isPalindrome(right) {
				reversedLeft := reverseString(left)
				if other, ok := wordMap[reversedLeft]; ok && other != index {
					seen[pair{index, other}] = struct{}{}
				}
			}
		}
	}

	result := make([][]int, 0, len(seen))
	for key := range seen {
		result = append(result, []int{key.left, key.right})
	}
	return result
}
