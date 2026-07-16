// LeetCode 0008 - String to Integer (atoi)
// https://leetcode.com/problems/string-to-integer-atoi/

func myAtoi(s string) int {
	i := 0
	for i < len(s) && s[i] == ' ' {
		i++
	}
	if i >= len(s) {
		return 0
	}

	sign := 1
	if s[i] == '-' {
		sign = -1
		i++
	} else if s[i] == '+' {
		i++
	}

	result := 0
	for i < len(s) && s[i] >= '0' && s[i] <= '9' {
		digit := int(s[i] - '0')
		if result > (mathMaxInt-digit)/10 {
			if sign == -1 {
				return mathMinInt
			}
			return mathMaxInt
		}
		result = result*10 + digit
		i++
	}

	return sign * result
}

const mathMaxInt = 1<<31 - 1
const mathMinInt = -1 << 31
