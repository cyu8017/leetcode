// LeetCode 0862 - Shortest Subarray with Sum at Least K
// https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

func shortestSubarray(nums []int, k int) int {
	n := len(nums)
	prefix := make([]int, n+1)
	for i, x := range nums {
		prefix[i+1] = prefix[i] + x
	}
	dq := []int{}
	ans := n + 1
	for i, p := range prefix {
		for len(dq) > 0 && p-prefix[dq[0]] >= k {
			if i-dq[0] < ans {
				ans = i - dq[0]
			}
			dq = dq[1:]
		}
		for len(dq) > 0 && p <= prefix[dq[len(dq)-1]] {
			dq = dq[:len(dq)-1]
		}
		dq = append(dq, i)
	}
	if ans <= n {
		return ans
	}
	return -1
}
