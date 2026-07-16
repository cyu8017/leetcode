// LeetCode 0268 - Missing Number
// https://leetcode.com/problems/missing-number/

func missingNumber(nums []int) int {
	length := len(nums)
	expected := length * (length + 1) / 2
	total := 0
	for _, num := range nums {
		total += num
	}
	return expected - total
}
