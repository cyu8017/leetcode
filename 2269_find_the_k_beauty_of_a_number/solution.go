// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

func divisorSubstrings(num int, k int) int {
	s := ""
	n := num
	if n == 0 {
		s = "0"
	} else {
		for n > 0 {
			s = string(rune('0'+n%10)) + s
			n /= 10
		}
	}
	ans := 0
	for i := 0; i+k <= len(s); i++ {
		sub := 0
		for j := 0; j < k; j++ {
			sub = sub*10 + int(s[i+j]-'0')
		}
		if sub != 0 && num%sub == 0 {
			ans++
		}
	}
	return ans
}
