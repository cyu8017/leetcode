// LeetCode 0007 - Reverse Integer
// https://leetcode.com/problems/reverse-integer/

func reverse(x int) int {
	result := 0

	for x != 0 {
		pop := x % 10
		x /= 10

		if result > mathMaxInt/10 || (result == mathMaxInt/10 && pop > 7) {
			return 0
		}
		if result < mathMinInt/10 || (result == mathMinInt/10 && pop < -8) {
			return 0
		}

		result = result*10 + pop
	}

	return result
}

const mathMaxInt = 1<<31 - 1
const mathMinInt = -1 << 31
