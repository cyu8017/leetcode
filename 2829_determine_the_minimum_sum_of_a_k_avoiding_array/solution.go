// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

func minimumSum(n int, k int) int {
	used := map[int]bool{}
	sum, x := 0, 1
	for len(used) < n {
		if !used[k-x] {
			used[x] = true
			sum += x
		}
		x++
	}
	return sum
}
