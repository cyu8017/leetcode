// LeetCode 0215 - Kth Largest Element in an Array
// https://leetcode.com/problems/kth-largest-element-in-an-array/

import "math/rand"

func findKthLargest(nums []int, k int) int {
	target := len(nums) - k
	left, right := 0, len(nums)-1
	for left <= right {
		pivotIndex := partition(nums, left, right)
		switch {
		case pivotIndex == target:
			return nums[pivotIndex]
		case pivotIndex < target:
			left = pivotIndex + 1
		default:
			right = pivotIndex - 1
		}
	}
	return nums[left]
}

func partition(nums []int, left, right int) int {
	pivotIndex := left + rand.Intn(right-left+1)
	nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
	store := left
	for i := left; i < right; i++ {
		if nums[i] <= nums[right] {
			nums[store], nums[i] = nums[i], nums[store]
			store++
		}
	}
	nums[store], nums[right] = nums[right], nums[store]
	return store
}
