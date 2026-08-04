// LeetCode 1363 - Largest Multiple of Three
// https://leetcode.com/problems/largest-multiple-of-three/

func largestMultipleOfThree(digits []int) string {
	cnt := [10]int{}
	sum := 0
	for _, d := range digits {
		cnt[d]++
		sum += d
	}
	rem := sum % 3
	remove := func(r, k int) bool {
		for d := r; d < 10; d += 3 {
			for cnt[d] > 0 && k > 0 {
				cnt[d]--
				k--
			}
			if k == 0 {
				return true
			}
		}
		return false
	}
	if rem != 0 && !remove(rem, 1) {
		remove(3-rem, 2)
	}
	var s []byte
	for d := 9; d >= 0; d-- {
		for i := 0; i < cnt[d]; i++ {
			s = append(s, byte('0'+d))
		}
	}
	if len(s) == 0 {
		return ""
	}
	if s[0] == '0' {
		return "0"
	}
	return string(s)
}
