// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

func maxLengthBetweenEqualCharacters(s string) int {
	first := map[byte]int{}
	ans := -1
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if j, ok := first[ch]; ok {
			if i-j-1 > ans {
				ans = i - j - 1
			}
		} else {
			first[ch] = i
		}
	}
	return ans
}
