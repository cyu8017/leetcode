// LeetCode 2789 - Largest Element in an Array after Merge Operations
// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

func maxArrayValue(nums []int) int64 {
	n := len(nums)
	cur := int64(nums[n-1])
	ans := cur
	for i := n - 2; i >= 0; i-- {
		if int64(nums[i]) <= cur {
			cur += int64(nums[i])
		} else {
			cur = int64(nums[i])
		}
		if cur > ans {
			ans = cur
		}
	}
	return ans
}
