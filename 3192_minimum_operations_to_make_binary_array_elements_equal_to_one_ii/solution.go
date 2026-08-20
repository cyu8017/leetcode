// LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

func minOperations(nums []int) (ans int) {
	v := 0
	for _, x := range nums {
		x ^= v
		if x == 0 {
			v ^= 1
			ans++
		}
	}
	return
}
