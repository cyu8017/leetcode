// LeetCode 0283 - Move Zeroes
// https://leetcode.com/problems/move-zeroes/

func moveZeroes(nums []int) {
	insert := 0
	for _, num := range nums {
		if num != 0 {
			nums[insert] = num
			insert++
		}
	}
	for index := insert; index < len(nums); index++ {
		nums[index] = 0
	}
}
