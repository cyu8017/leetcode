// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/


func removeTrailingZeros(num string) string {
	i := len(num) - 1
	for i >= 0 && num[i] == '0' {
		i--
	}
	return num[:i+1]
}
