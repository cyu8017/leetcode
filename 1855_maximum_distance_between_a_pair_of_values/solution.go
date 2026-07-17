// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

func maxDistance(nums1 []int, nums2 []int) int {
	answer := 0
	j := 0

	for i, value := range nums1 {
		for j < len(nums2) && value <= nums2[j] {
			j++
		}
		if j-i-1 > answer {
			answer = j - i - 1
		}
	}

	return answer
}
