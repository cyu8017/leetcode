// LeetCode 3525 - Find X Value Of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

func resultArray(nums []int, k int, queries [][]int) []int {
	n := len(nums)
	ans := make([]int, len(queries))
	for qi, q := range queries {
		idx, val, start, x := q[0], q[1], q[2], q[3]
		nums[idx] = val
		prod := 1
		cnt := 0
		for i := start; i < n; i++ {
			prod = prod * (nums[i] % k) % k
			if prod == x {
				cnt++
			}
		}
		ans[qi] = cnt
	}
	return ans
}
