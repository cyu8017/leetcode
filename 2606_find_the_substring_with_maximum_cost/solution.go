// LeetCode 2606 - Find the Substring With Maximum Cost
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/


func maximumCostSubstring(s string, chars string, vals []int) int {
	val := [26]int{}
	for i := 0; i < 26; i++ {
		val[i] = i + 1
	}
	for i := 0; i < len(chars); i++ {
		val[chars[i]-'a'] = vals[i]
	}
	best, cur := 0, 0
	for i := 0; i < len(s); i++ {
		cur += val[s[i]-'a']
		if cur < 0 {
			cur = 0
		}
		if cur > best {
			best = cur
		}
	}
	return best
}
