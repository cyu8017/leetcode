// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

func getMaximumXor(nums []int, maximumBit int) []int {
	limit := (1 << maximumBit) - 1
	current := 0
	for _, num := range nums {
		current ^= num
	}

	result := make([]int, len(nums))
	for i := len(nums) - 1; i >= 0; i-- {
		result[len(nums)-1-i] = current ^ limit
		current ^= nums[i]
	}
	return result
}
