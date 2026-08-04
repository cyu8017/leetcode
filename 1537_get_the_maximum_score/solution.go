// LeetCode 1537 - Get the Maximum Score
// https://leetcode.com/problems/get-the-maximum-score/

func maxSum(nums1 []int, nums2 []int) int {
	i, j := 0, 0
	first, second := 0, 0
	for i < len(nums1) || j < len(nums2) {
		if j == len(nums2) || (i < len(nums1) && nums1[i] < nums2[j]) {
			first += nums1[i]
			i++
		} else if i == len(nums1) || nums2[j] < nums1[i] {
			second += nums2[j]
			j++
		} else {
			if first > second {
				first = first + nums1[i]
				second = first
			} else {
				second = second + nums1[i]
				first = second
			}
			i++
			j++
		}
	}
	if first > second {
		return first % 1000000007
	}
	return second % 1000000007
}
