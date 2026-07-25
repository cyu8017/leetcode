// LeetCode 1673 - Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/

func mostCompetitive(nums []int, k int) []int {
	st := make([]int, 0, k)
	for i, x := range nums {
		for len(st) > 0 && st[len(st)-1] > x && len(st)-1+len(nums)-i >= k {
			st = st[:len(st)-1]
		}
		if len(st) < k {
			st = append(st, x)
		}
	}
	return st
}
