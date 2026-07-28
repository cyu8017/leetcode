// LeetCode 1071 - Greatest Common Divisor of Strings
// https://leetcode.com/problems/greatest-common-divisor-of-strings/

func gcdOfStrings(str1 string, str2 string) string {
	if str1+str2 != str2+str1 {
		return ""
	}
	return str1[:gcd1071(len(str1), len(str2))]
}

func gcd1071(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
