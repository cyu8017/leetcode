// LeetCode 1945 - Sum of Digits of String After Convert
// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

func getLucky(s string, k int) int {
	num := make([]byte, 0, len(s)*2)
	for i := 0; i < len(s); i++ {
		v := int(s[i] - 'a' + 1)
		if v >= 10 {
			num = append(num, byte('0'+v/10), byte('0'+v%10))
		} else {
			num = append(num, byte('0'+v))
		}
	}
	for t := 0; t < k; t++ {
		sum := 0
		for _, d := range num {
			sum += int(d - '0')
		}
		if t == k-1 {
			return sum
		}
		num = []byte{}
		if sum == 0 {
			num = append(num, '0')
		} else {
			tmp := []byte{}
			for sum > 0 {
				tmp = append(tmp, byte('0'+sum%10))
				sum /= 10
			}
			for i := len(tmp) - 1; i >= 0; i-- {
				num = append(num, tmp[i])
			}
		}
	}
	res := 0
	for _, d := range num {
		res = res*10 + int(d-'0')
	}
	return res
}
