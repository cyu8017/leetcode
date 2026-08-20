// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

func maximumTop(nums []int, k int) int {
	n := len(nums)
	if n == 1 {
		if k%2 == 1 {
			return -1
		}
		return nums[0]
	}
	if k == 0 {
		return nums[0]
	}
	ans := -1
	limit := k - 1
	if limit > n {
		limit = n
	}
	for i := 0; i < limit; i++ {
		if nums[i] > ans {
			ans = nums[i]
		}
	}
	if k < n && nums[k] > ans {
		ans = nums[k]
	}
	return ans
}
