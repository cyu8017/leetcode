// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

func findMinimumOperations(s1 string, s2 string, s3 string) int {
	n := len(s1)
	if len(s2) < n {
		n = len(s2)
	}
	if len(s3) < n {
		n = len(s3)
	}
	i := 0
	for i < n && s1[i] == s2[i] && s2[i] == s3[i] {
		i++
	}
	if i == 0 {
		return -1
	}
	return len(s1) + len(s2) + len(s3) - 3*i
}
