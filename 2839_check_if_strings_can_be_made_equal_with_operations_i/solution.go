// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

import "sort"

func canBeEqual(s1 string, s2 string) bool {
	a := []byte{s1[0], s1[2]}
	b := []byte{s2[0], s2[2]}
	c := []byte{s1[1], s1[3]}
	d := []byte{s2[1], s2[3]}
	sort.Slice(a, func(i, j int) bool { return a[i] < a[j] })
	sort.Slice(b, func(i, j int) bool { return b[i] < b[j] })
	sort.Slice(c, func(i, j int) bool { return c[i] < c[j] })
	sort.Slice(d, func(i, j int) bool { return d[i] < d[j] })
	return string(a) == string(b) && string(c) == string(d)
}
