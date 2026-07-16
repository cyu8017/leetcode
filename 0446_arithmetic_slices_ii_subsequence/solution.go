// LeetCode 0446 - Arithmetic Slices II - Subsequence
// https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

func numberOfArithmeticSlices(nums []int) int {
	total := 0
	differences := make([]map[int64]int, len(nums))
	for index := range differences {
		differences[index] = make(map[int64]int)
	}

	for index, value := range nums {
		for previous := 0; previous < index; previous++ {
			diff := int64(value - nums[previous])
			total += differences[previous][diff]
			differences[index][diff] += differences[previous][diff] + 1
		}
	}
	return total
}
