// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

func filterCharacters(s string, k int) string {
	cnt := [26]int{}
	for _, c := range s {
		cnt[c-'a']++
	}
	ans := []rune{}
	for _, c := range s {
		if cnt[c-'a'] < k {
			ans = append(ans, c)
		}
	}
	return string(ans)
}
