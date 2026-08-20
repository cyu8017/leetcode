// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

func closestFair(n int) int {
	for x := n; ; x++ {
		s := itoa(x)
		if len(s)%2 != 0 {
			// jump to smallest even-length with more digits
			pow := 1
			for i := 0; i < len(s)+1; i++ {
				pow *= 10
			}
			// 10^len(s)
			p := 1
			for i := 0; i < len(s); i++ {
				p *= 10
			}
			return closestFair(p)
		}
		even, odd := 0, 0
		for i := 0; i < len(s); i++ {
			d := int(s[i] - '0')
			if d%2 == 0 {
				even++
			} else {
				odd++
			}
		}
		if even == odd {
			return x
		}
	}
}

func itoa(x int) string {
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
