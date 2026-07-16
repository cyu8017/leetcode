// LeetCode 0041 - First Missing Positive
// https://leetcode.com/problems/first-missing-positive/

func firstMissingPositive(nums []int) int {
	n := len(nums)
	i := 0

	for i < n {
		value := nums[i]
		target := value - 1
		if value >= 1 && value <= n && nums[target] != value {
			nums[i], nums[target] = nums[target], nums[i]
		} else {
			i++
		}
	}

	for index := 0; index < n; index++ {
		if nums[index] != index+1 {
			return index + 1
		}
	}

	return n + 1
}
