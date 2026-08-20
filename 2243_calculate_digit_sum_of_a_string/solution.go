// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

func digitSum(s string, k int) string {
	for len(s) > k {
		next := ""
		for i := 0; i < len(s); i += k {
			end := i + k
			if end > len(s) {
				end = len(s)
			}
			sum := 0
			for j := i; j < end; j++ {
				sum += int(s[j] - '0')
			}
			next += itoa2243(sum)
		}
		s = next
	}
	return s
}

func itoa2243(x int) string {
	if x == 0 {
		return "0"
	}
	b := []byte{}
	for x > 0 {
		b = append([]byte{byte('0' + x%10)}, b...)
		x /= 10
	}
	return string(b)
}
