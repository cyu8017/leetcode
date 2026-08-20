// LeetCode 2802 - Find The K-th Lucky Number
// https://leetcode.com/problems/find-the-k-th-lucky-number/

func kthLuckyNumber(k int) string {
	k++
	bits := ""
	for k > 1 {
		if k%2 == 0 {
			bits = "4" + bits
		} else {
			bits = "7" + bits
		}
		k /= 2
	}
	return bits
}
