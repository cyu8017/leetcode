// LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

func minOperations(nums []int) (ans int) {
	for i, x := range nums {
		if x == 0 {
			if i+2 >= len(nums) {
				return -1
			}
			nums[i+1] ^= 1
			nums[i+2] ^= 1
			ans++
		}
	}
	return
}
