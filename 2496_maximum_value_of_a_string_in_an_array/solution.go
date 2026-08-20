// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

func maximumValue(strs []string) int {
	ans := 0
	for _, s := range strs {
		allDigit := true
		val := 0
		for i := 0; i < len(s); i++ {
			if s[i] < '0' || s[i] > '9' {
				allDigit = false
				break
			}
			val = val*10 + int(s[i]-'0')
		}
		if !allDigit {
			val = len(s)
		}
		if val > ans {
			ans = val
		}
	}
	return ans
}
