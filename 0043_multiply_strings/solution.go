// LeetCode 0043 - Multiply Strings
// https://leetcode.com/problems/multiply-strings/

func multiply(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}

	m, n := len(num1), len(num2)
	positions := make([]int, m+n)

	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			product := int(num1[i]-'0') * int(num2[j]-'0')
			low := i + j + 1
			high := i + j
			total := product + positions[low]
			positions[low] = total % 10
			positions[high] += total / 10
		}
	}

	start := 0
	for start < len(positions)-1 && positions[start] == 0 {
		start++
	}

	result := make([]byte, len(positions)-start)
	for k := start; k < len(positions); k++ {
		result[k-start] = byte('0' + positions[k])
	}
	if len(result) == 0 {
		return "0"
	}
	return string(result)
}
