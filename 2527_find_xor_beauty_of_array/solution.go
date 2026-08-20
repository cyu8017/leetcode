// LeetCode 2527 - Find Xor-Beauty of Array
// https://leetcode.com/problems/find-xor-beauty-of-array/

func xorBeauty(nums []int) int {
	ans := 0
	for _, x := range nums {
		ans ^= x
	}
	return ans
}
