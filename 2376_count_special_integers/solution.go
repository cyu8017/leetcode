// LeetCode 2376 - Count Special Integers
// https://leetcode.com/problems/count-special-integers/

func countSpecialNumbers(n int) int {
	s := []byte{}
	for x := n; x > 0; x /= 10 {
		s = append([]byte{byte('0' + x%10)}, s...)
	}
	m := len(s)
	// count numbers with fewer digits
	ans := 0
	perm := 9
	for i := 1; i < m; i++ {
		ans += perm
		perm *= (10 - i)
	}
	used := [10]bool{}
	for i := 0; i < m; i++ {
		start := 0
		if i == 0 {
			start = 1
		}
		digit := int(s[i] - '0')
		for d := start; d < digit; d++ {
			if used[d] {
				continue
			}
			rem := 10 - (i + 1)
			ways := 1
			for j := i + 1; j < m; j++ {
				ways *= rem
				rem--
			}
			ans += ways
		}
		if used[digit] {
			return ans
		}
		used[digit] = true
	}
	return ans + 1
}
