// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/


func smallestString(s string) string {
	b := []byte(s)
	i := 0
	for i < len(b) && b[i] == 'a' {
		i++
	}
	if i == len(b) {
		b[len(b)-1] = 'z'
		return string(b)
	}
	for i < len(b) && b[i] != 'a' {
		b[i]--
		i++
	}
	return string(b)
}
