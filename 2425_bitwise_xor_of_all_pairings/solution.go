// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

func xorAllNums(nums1 []int, nums2 []int) int {
	ans := 0
	if len(nums2)%2 == 1 {
		for _, x := range nums1 {
			ans ^= x
		}
	}
	if len(nums1)%2 == 1 {
		for _, x := range nums2 {
			ans ^= x
		}
	}
	return ans
}
