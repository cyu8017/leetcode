// LeetCode 2541 - Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/


func minOperations(nums1 []int, nums2 []int, k int) int64 {
	if k == 0 {
		for i := range nums1 {
			if nums1[i] != nums2[i] {
				return -1
			}
		}
		return 0
	}
	var pos, neg int64
	for i := range nums1 {
		d := nums1[i] - nums2[i]
		if d%k != 0 {
			return -1
		}
		if d > 0 {
			pos += int64(d / k)
		} else {
			neg += int64(-d / k)
		}
	}
	if pos != neg {
		return -1
	}
	return pos
}
