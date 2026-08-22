// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

import (
	"sort"
)

func simpleGraphExists(degrees []int) bool {
	n := len(degrees)
	d := append([]int(nil), degrees...)
	sort.Sort(sort.Reverse(sort.IntSlice(d)))
	var sum int64
	for _, x := range d {
		if x < 0 || x >= n {
			return false
		}
		sum += int64(x)
	}
	if sum%2 == 1 {
		return false
	}
	prefix := make([]int64, n+1)
	for i := 0; i < n; i++ {
		prefix[i+1] = prefix[i] + int64(d[i])
	}
	for k := 1; k <= n; k++ {
		var right int64
		for i := k; i < n; i++ {
			if d[i] < k {
				right += int64(d[i])
			} else {
				right += int64(k)
			}
		}
		if prefix[k] > int64(k*(k-1))+right {
			return false
		}
	}
	return true
}
