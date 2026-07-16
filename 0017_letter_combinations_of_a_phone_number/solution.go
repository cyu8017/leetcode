// LeetCode 0017 - Letter Combinations of a Phone Number
// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

var mapping = []string{
	"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz",
}

func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}

	result := make([]string, 0)
	path := make([]byte, 0, len(digits))

	var backtrack func(index int)
	backtrack = func(index int) {
		if index == len(digits) {
			result = append(result, string(path))
			return
		}
		for _, ch := range mapping[digits[index]-'0'] {
			path = append(path, byte(ch))
			backtrack(index + 1)
			path = path[:len(path)-1]
		}
	}

	backtrack(0)
	return result
}
