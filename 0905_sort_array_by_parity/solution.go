// LeetCode 0905 - Sort Array By Parity
// https://leetcode.com/problems/sort-array-by-parity/

func sortArrayByParity(nums []int) []int {
	i := 0
	for j, x := range nums {
		if x%2 == 0 {
			nums[i], nums[j] = nums[j], nums[i]
			i++
		}
	}
	return nums
}
