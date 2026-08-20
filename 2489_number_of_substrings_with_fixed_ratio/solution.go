// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

func fixedRatio(s string, num1 int, num2 int) int64 {
	// zeros/ones = num1/num2 => zeros*num2 = ones*num1
	pref := map[int]int{0: 1}
	zeros, ones := 0, 0
	var ans int64
	for i := 0; i < len(s); i++ {
		if s[i] == '0' {
			zeros++
		} else {
			ones++
		}
		key := zeros*num2 - ones*num1
		ans += int64(pref[key])
		pref[key]++
	}
	return ans
}
