// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

func maxSum(nums []int, m int, l int, r int) int64 {
	n := len(nums)
	prefix := make([]int64, n+1)
	for i, x := range nums {
		prefix[i+1] = prefix[i] + int64(x)
	}
	dp := make([]int64, n+1)
	bestSelected := int64(-1 << 62)
	for count := 1; count <= m; count++ {
		next := append([]int64(nil), dp...)
		deque := make([]int, 0, n)
		for end := 1; end <= n; end++ {
			addIndex := end - l
			if addIndex >= 0 {
				value := dp[addIndex] - prefix[addIndex]
				for len(deque) > 0 {
					last := deque[len(deque)-1]
					if dp[last]-prefix[last] > value {
						break
					}
					deque = deque[:len(deque)-1]
				}
				deque = append(deque, addIndex)
			}
			minIndex := end - r
			for len(deque) > 0 && deque[0] < minIndex {
				deque = deque[1:]
			}
			if len(deque) > 0 {
				candidate := prefix[end] + dp[deque[0]] - prefix[deque[0]]
				if candidate > next[end] {
					next[end] = candidate
				}
				if candidate > bestSelected {
					bestSelected = candidate
				}
			}
			if next[end-1] > next[end] {
				next[end] = next[end-1]
			}
		}
		dp = next
	}
	return bestSelected
}