// LeetCode 0315 - Count of Smaller Numbers After Self
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

func countSmaller(nums []int) []int {
	sortedNums := make([]int, 0, len(nums))
	result := make([]int, len(nums))

	for index := len(nums) - 1; index >= 0; index-- {
		num := nums[index]
		left, right := 0, len(sortedNums)
		for left < right {
			mid := left + (right-left)/2
			if sortedNums[mid] < num {
				left = mid + 1
			} else {
				right = mid
			}
		}
		result[index] = left
		sortedNums = append(sortedNums[:left], append([]int{num}, sortedNums[left:]...)...)
	}

	return result
}
