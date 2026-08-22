// LeetCode 3526 - Range XOR Queries With Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

func getResults(nums []int, queries [][]int) []int {
	a := append([]int(nil), nums...)
	var ans []int
	for _, q := range queries {
		typ := q[0]
		if typ == 1 {
			l, r := q[1], q[2]
			for l < r {
				a[l], a[r] = a[r], a[l]
				l++
				r--
			}
		} else if typ == 2 {
			l, r := q[1], q[2]
			x := 0
			for i := l; i <= r; i++ {
				x ^= a[i]
			}
			ans = append(ans, x)
		} else {
			idx, val := q[1], q[2]
			a[idx] = val
		}
	}
	return ans
}
