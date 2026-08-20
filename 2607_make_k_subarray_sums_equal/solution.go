// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/


import "sort"
func makeSubKSumEqual(arr []int, k int) int64 {
	n := len(arr)
	g := k
	a, b := n, k
	for b != 0 {
		a, b = b, a%b
	}
	g = a
	var ans int64
	for r := 0; r < g; r++ {
		group := []int{}
		for i := r; i < n; i += g {
			group = append(group, arr[i])
		}
		sort.Ints(group)
		med := group[len(group)/2]
		for _, x := range group {
			d := x - med
			if d < 0 {
				d = -d
			}
			ans += int64(d)
		}
	}
	return ans
}
