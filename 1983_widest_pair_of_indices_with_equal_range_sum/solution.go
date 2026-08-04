// LeetCode 1983 - Widest Pair of Indices With Equal Range Sum
// https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/

func widestPairOfIndices(nums1 []int, nums2 []int) int {
	first := map[int]int{0: -1}
	ans, s := 0, 0
	for i := 0; i < len(nums1); i++ {
		s += nums1[i] - nums2[i]
		if idx, ok := first[s]; ok {
			if i-idx > ans {
				ans = i - idx
			}
		} else {
			first[s] = i
		}
	}
	return ans
}
