// LeetCode 0067 - Add Binary
// https://leetcode.com/problems/add-binary/

func addBinary(a string, b string) string {
	i := len(a) - 1
	j := len(b) - 1
	carry := 0
	result := make([]byte, 0, len(a)+len(b)+1)

	for i >= 0 || j >= 0 || carry != 0 {
		total := carry
		if i >= 0 {
			total += int(a[i] - '0')
			i--
		}
		if j >= 0 {
			total += int(b[j] - '0')
			j--
		}
		result = append(result, byte('0'+total%2))
		carry = total / 2
	}

	for left, right := 0, len(result)-1; left < right; left, right = left+1, right-1 {
		result[left], result[right] = result[right], result[left]
	}

	return string(result)
}
