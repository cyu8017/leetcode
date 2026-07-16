// LeetCode 0402 - Remove K Digits
// https://leetcode.com/problems/remove-k-digits/

func removeKdigits(num string, k int) string {
	stack := make([]byte, 0, len(num))

	for i := 0; i < len(num); i++ {
		digit := num[i]
		for k > 0 && len(stack) > 0 && stack[len(stack)-1] > digit {
			stack = stack[:len(stack)-1]
			k--
		}
		stack = append(stack, digit)
	}

	if k > 0 {
		stack = stack[:len(stack)-k]
	}

	start := 0
	for start < len(stack)-1 && stack[start] == '0' {
		start++
	}

	result := string(stack[start:])
	if result == "" {
		return "0"
	}
	return result
}
