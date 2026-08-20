// LeetCode 3260 - Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

func largestPalindrome(n int, k int) string {
	digits := make([]byte, n)
	for i := range digits {
		digits[i] = '9'
	}
	half := (n + 1) / 2
	switch k {
	case 1, 3, 9:
		return string(digits)
	case 2:
		digits[0] = '8'
		digits[n-1] = '8'
		return string(digits)
	case 4:
		if n == 1 {
			return "8"
		}
		digits[0], digits[1] = '8', '8'
		digits[n-1], digits[n-2] = '8', '8'
		return string(digits)
	case 5:
		digits[0], digits[n-1] = '5', '5'
		return string(digits)
	case 8:
		if n <= 2 {
			return stringsRepeat8(n)
		}
		digits[0], digits[1], digits[2] = '8', '8', '8'
		digits[n-1], digits[n-2], digits[n-3] = '8', '8', '8'
		return string(digits)
	case 6:
		if n == 1 {
			return "6"
		}
		digits[0], digits[n-1] = '8', '8'
		sum := 16 + 9*(n-2)
		need := sum % 3
		if need != 0 {
			pos := half - 1
			digits[pos] = byte('0' + int(digits[pos]-'0') - need)
			if n%2 == 0 || pos != n-1-pos {
				digits[n-1-pos] = digits[pos]
			}
		}
		return string(digits)
	case 7:
		return largestPal7(n)
	}
	return string(digits)
}

func stringsRepeat8(n int) string {
	b := make([]byte, n)
	for i := range b {
		b[i] = '8'
	}
	return string(b)
}

func largestPal7(n int) string {
	halfLen := (n + 1) / 2
	half := make([]byte, halfLen)
	for i := range half {
		half[i] = '9'
	}
	for {
		pal := make([]byte, n)
		copy(pal[:halfLen], half)
		for i := 0; i < n/2; i++ {
			pal[n-1-i] = pal[i]
		}
		if mod7(pal) == 0 {
			return string(pal)
		}
		i := halfLen - 1
		for i >= 0 && half[i] == '0' {
			half[i] = '9'
			i--
		}
		if i < 0 {
			break
		}
		half[i]--
	}
	return ""
}

func mod7(s []byte) int {
	r := 0
	for _, c := range s {
		r = (r*10 + int(c-'0')) % 7
	}
	return r
}
