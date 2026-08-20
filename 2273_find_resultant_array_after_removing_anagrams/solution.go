// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

func removeAnagrams(words []string) []string {
	sig := func(w string) [26]int {
		var c [26]int
		for i := 0; i < len(w); i++ {
			c[w[i]-'a']++
		}
		return c
	}
	ans := []string{words[0]}
	prev := sig(words[0])
	for i := 1; i < len(words); i++ {
		cur := sig(words[i])
		if cur != prev {
			ans = append(ans, words[i])
			prev = cur
		}
	}
	return ans
}
