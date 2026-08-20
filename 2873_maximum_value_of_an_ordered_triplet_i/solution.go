// LeetCode 2873 - Maximum Value of an Ordered Triplet I
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

func maximumTripletValue(nums []int) int64 {
	n := len(nums)
	var ans int64
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k < n; k++ {
				cand := int64(nums[i]-nums[j]) * int64(nums[k])
				if cand > ans {
					ans = cand
				}
			}
		}
	}
	return ans
}
