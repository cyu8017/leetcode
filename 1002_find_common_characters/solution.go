// LeetCode 1002 - Find Common Characters
// https://leetcode.com/problems/find-common-characters/

func commonChars(words []string) []string {
	common := make([]int, 26)
	for i := range common {
		common[i] = 1 << 30
	}
	for _, w := range words {
		cnt := make([]int, 26)
		for i := 0; i < len(w); i++ {
			cnt[w[i]-'a']++
		}
		for i := 0; i < 26; i++ {
			if cnt[i] < common[i] {
				common[i] = cnt[i]
			}
		}
	}
	ans := []string{}
	for i := 0; i < 26; i++ {
		for common[i] > 0 {
			ans = append(ans, string(byte('a'+i)))
			common[i]--
		}
	}
	return ans
}
