// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

func findKDistantIndices(nums []int, key int, k int) []int {
	n := len(nums)
	mark := make([]bool, n)
	for i, v := range nums {
		if v == key {
			l := i - k
			if l < 0 {
				l = 0
			}
			r := i + k
			if r >= n {
				r = n - 1
			}
			for j := l; j <= r; j++ {
				mark[j] = true
			}
		}
	}
	ans := []int{}
	for i, m := range mark {
		if m {
			ans = append(ans, i)
		}
	}
	return ans
}
