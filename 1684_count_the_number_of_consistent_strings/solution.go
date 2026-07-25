// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

func countConsistentStrings(allowed string, words []string) int {
	ok := [26]bool{}
	for i := 0; i < len(allowed); i++ {
		ok[allowed[i]-'a'] = true
	}
	ans := 0
	for _, w := range words {
		good := true
		for i := 0; i < len(w); i++ {
			if !ok[w[i]-'a'] {
				good = false
				break
			}
		}
		if good {
			ans++
		}
	}
	return ans
}
