// LeetCode 3876 - Construct Uniform Parity Array Ii
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

func uniformArray(nums1 []int) bool {
	mn := int(^uint(0) >> 1)
	for _, x := range nums1 {
		if x%2 == 1 && x < mn {
			mn = x
		}
	}
	for _, x := range nums1 {
		if x%2 == 0 && mn != int(^uint(0)>>1) && x < mn {
			return false
		}
	}
	return true
}
