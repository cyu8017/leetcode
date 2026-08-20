// LeetCode 2874 - Maximum Value of an Ordered Triplet II
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

func maximumTripletValue(nums []int) int64 {
	var ans, maxI, maxDiff int64
	for _, v := range nums {
		val := int64(v)
		if maxDiff*val > ans {
			ans = maxDiff * val
		}
		if maxI-val > maxDiff {
			maxDiff = maxI - val
		}
		if val > maxI {
			maxI = val
		}
	}
	return ans
}
