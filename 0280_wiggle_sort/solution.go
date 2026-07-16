// LeetCode 0280 - Wiggle Sort
// https://leetcode.com/problems/wiggle-sort/

func wiggleSort(nums []int) {
	for index := 1; index < len(nums); index++ {
		if index%2 == 1 && nums[index] < nums[index-1] {
			nums[index], nums[index-1] = nums[index-1], nums[index]
		} else if index%2 == 0 && nums[index] > nums[index-1] {
			nums[index], nums[index-1] = nums[index-1], nums[index]
		}
	}
}
