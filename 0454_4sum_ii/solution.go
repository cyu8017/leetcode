// LeetCode 0454 - 4Sum II
// https://leetcode.com/problems/4sum-ii/

func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	pairSums := make(map[int]int)
	for _, a := range nums1 {
		for _, b := range nums2 {
			pairSums[a+b]++
		}
	}

	total := 0
	for _, c := range nums3 {
		for _, d := range nums4 {
			total += pairSums[-(c + d)]
		}
	}
	return total
}
