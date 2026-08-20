// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

func maxSubstringLength(s string, k int) bool {
	n := len(s)
	first := make([]int, 26)
	last := make([]int, 26)
	for i := range first {
		first[i] = n
		last[i] = -1
	}
	for i, c := range s {
		ci := c - 'a'
		if first[ci] == n {
			first[ci] = i
		}
		last[ci] = i
	}
	type seg struct{ l, r int }
	segs := []seg{}
	for c := 0; c < 26; c++ {
		if last[c] == -1 {
			continue
		}
		l, r := first[c], last[c]
		for i := l; i <= r; i++ {
			ci := int(s[i] - 'a')
			if first[ci] < l {
				l = first[ci]
				i = l - 1
				continue
			}
			if last[ci] > r {
				r = last[ci]
			}
		}
		if !(l == 0 && r == n-1) {
			segs = append(segs, seg{l, r})
		}
	}
	// unique segs
	uniq := map[[2]int]bool{}
	arr := []seg{}
	for _, sg := range segs {
		key := [2]int{sg.l, sg.r}
		if !uniq[key] {
			uniq[key] = true
			arr = append(arr, sg)
		}
	}
	// max non-overlapping
	// sort by end
	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			if arr[j].r < arr[i].r {
				arr[i], arr[j] = arr[j], arr[i]
			}
		}
	}
	cnt, end := 0, -1
	for _, sg := range arr {
		if sg.l > end {
			cnt++
			end = sg.r
		}
	}
	return cnt >= k
}
