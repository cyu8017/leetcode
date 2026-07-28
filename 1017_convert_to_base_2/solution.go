// LeetCode 1017 - Convert to Base -2
// https://leetcode.com/problems/convert-to-base-2/

func baseNeg2(n int) string {
	if n == 0 {
		return "0"
	}
	ans := []byte{}
	for n != 0 {
		rem := n % -2
		n /= -2
		if rem < 0 {
			n++
			rem += 2
		}
		ans = append(ans, byte('0'+rem))
	}
	for i, j := 0, len(ans)-1; i < j; i, j = i+1, j-1 {
		ans[i], ans[j] = ans[j], ans[i]
	}
	return string(ans)
}
