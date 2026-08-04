// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

func maxRepOpt1(text string) int {
	count := [26]int{}
	for i := 0; i < len(text); i++ {
		count[text[i]-'a']++
	}
	n := len(text)
	ans := 0
	i := 0
	for i < n {
		j := i
		for j < n && text[j] == text[i] {
			j++
		}
		length := j - i
		k := j + 1
		for k < n && text[k] == text[i] {
			k++
		}
		length2 := 0
		if j < n {
			length2 = k - j - 1
		}
		cand := length + length2 + 1
		if cand > count[text[i]-'a'] {
			cand = count[text[i]-'a']
		}
		if cand > ans {
			ans = cand
		}
		i = j
	}
	return ans
}
