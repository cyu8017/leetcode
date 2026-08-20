// LeetCode 0908 - Smallest Range I
// https://leetcode.com/problems/smallest-range-i/

func smallestRangeI(nums []int, k int) int {
	mn, mx := nums[0], nums[0]
	for _, x := range nums {
		if x < mn {
			mn = x
		}
		if x > mx {
			mx = x
		}
	}
	diff := mx - mn - 2*k
	if diff < 0 {
		return 0
	}
	return diff
}
