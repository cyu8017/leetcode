// LeetCode 0713 - Subarray Product Less Than K
// https://leetcode.com/problems/subarray-product-less-than-k/

func numSubarrayProductLessThanK(nums []int, k int) int {
	if k <= 1 {
		return 0
	}
	product, left, ans := 1, 0, 0
	for right, num := range nums {
		product *= num
		for product >= k {
			product /= nums[left]
			left++
		}
		ans += right - left + 1
	}
	return ans
}
