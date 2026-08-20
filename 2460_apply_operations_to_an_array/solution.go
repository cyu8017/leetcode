// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

func applyOperations(nums []int) []int {
	n := len(nums)
	for i := 0; i+1 < n; i++ {
		if nums[i] == nums[i+1] {
			nums[i] *= 2
			nums[i+1] = 0
		}
	}
	ans := make([]int, n)
	j := 0
	for _, x := range nums {
		if x != 0 {
			ans[j] = x
			j++
		}
	}
	return ans
}
