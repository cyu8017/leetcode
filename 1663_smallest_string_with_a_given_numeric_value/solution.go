// LeetCode 1663 - Smallest String With A Given Numeric Value
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

func getSmallestString(n, k int) string {
	a := make([]byte, n)
	for i := range a {
		a[i] = 'a'
	}
	k -= n
	for i := n - 1; i >= 0; i-- {
		d := 25
		if k < d {
			d = k
		}
		a[i] = byte('a' + d)
		k -= d
	}
	return string(a)
}
