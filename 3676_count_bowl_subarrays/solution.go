// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

func bowlSubarrays(nums []int) int64 {
	n := len(nums)
	var ans int64
	ngr := make([]int, n)
	ngl := make([]int, n)
	for i := range ngr {
		ngr[i], ngl[i] = -1, -1
	}
	stack := []int{}
	for i := n - 1; i >= 0; i-- {
		for len(stack) > 0 && nums[stack[len(stack)-1]] < nums[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) > 0 {
			ngr[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	stack = stack[:0]
	for i := 0; i < n; i++ {
		for len(stack) > 0 && nums[stack[len(stack)-1]] < nums[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) > 0 {
			ngl[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	for i := 0; i < n; i++ {
		if ngr[i] != -1 && ngr[i]-i >= 2 {
			ans++
		}
		if ngl[i] != -1 && i-ngl[i] >= 2 {
			ans++
		}
	}
	return ans
}
