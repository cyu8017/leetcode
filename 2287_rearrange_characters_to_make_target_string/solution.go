// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

func rearrangeCharacters(s string, target string) int {
	var sc, tc [26]int
	for i := 0; i < len(s); i++ {
		sc[s[i]-'a']++
	}
	for i := 0; i < len(target); i++ {
		tc[target[i]-'a']++
	}
	ans := int(1e9)
	for i := 0; i < 26; i++ {
		if tc[i] == 0 {
			continue
		}
		if sc[i]/tc[i] < ans {
			ans = sc[i] / tc[i]
		}
	}
	return ans
}
