// LeetCode 1433 - Check If a String Can Break Another String
// https://leetcode.com/problems/check-if-a-string-can-break-another-string/

import "sort"

func checkIfCanBreak(s1 string, s2 string) bool {
	a := []byte(s1)
	b := []byte(s2)
	sort.Slice(a, func(i, j int) bool { return a[i] < a[j] })
	sort.Slice(b, func(i, j int) bool { return b[i] < b[j] })
	ge, le := true, true
	for i := range a {
		if a[i] < b[i] {
			ge = false
		}
		if a[i] > b[i] {
			le = false
		}
	}
	return ge || le
}
