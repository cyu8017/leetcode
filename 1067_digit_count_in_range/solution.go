// LeetCode 1067 - Digit Count in Range
// https://leetcode.com/problems/digit-count-in-range/

func digitsCount(d int, low int, high int) int {
	countUpto := func(n int) int {
		if n < 0 {
			return 0
		}
		s := []byte{}
		if n == 0 {
			s = []byte{'0'}
		} else {
			for x := n; x > 0; x /= 10 {
				s = append([]byte{byte('0' + x%10)}, s...)
			}
		}
		length := len(s)
		ans := 0
		for i := 0; i < length; i++ {
			left := 0
			if i > 0 {
				left = atoiDigits(s[:i])
			}
			right := 0
			if i+1 < length {
				right = atoiDigits(s[i+1:])
			}
			digit := int(s[i] - '0')
			power := pow10(length - i - 1)
			if d != 0 {
				ans += left * power
				if digit > d {
					ans += power
				} else if digit == d {
					ans += right + 1
				}
			} else {
				if i == 0 {
					continue
				}
				ans += (left - 1) * power
				if digit > 0 {
					ans += power
				} else {
					ans += right + 1
				}
			}
		}
		return ans
	}
	return countUpto(high) - countUpto(low-1)
}

func atoiDigits(s []byte) int {
	v := 0
	for _, c := range s {
		v = v*10 + int(c-'0')
	}
	return v
}

func pow10(n int) int {
	p := 1
	for i := 0; i < n; i++ {
		p *= 10
	}
	return p
}
