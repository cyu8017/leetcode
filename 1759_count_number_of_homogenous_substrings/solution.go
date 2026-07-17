// LeetCode 1759 - Count Number of Homogenous Substrings
// https://leetcode.com/problems/count-number-of-homogenous-substrings/

func countHomogenous(s string) int {
	const mod = 1000000007
	ans := 0
	i := 0
	for i < len(s) {
		j := i
		for j < len(s) && s[j] == s[i] {
			j++
		}
		length := j - i
		ans = (ans + length*(length+1)/2) % mod
		i = j
	}
	return ans
}
