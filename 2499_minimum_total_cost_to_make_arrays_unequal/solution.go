// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

func minimumTotalCost(nums1 []int, nums2 []int) int64 {
	n := len(nums1)
	freq := map[int]int{}
	var ans int64
	same := 0
	for i := 0; i < n; i++ {
		if nums1[i] == nums2[i] {
			same++
			freq[nums1[i]]++
			ans += int64(i)
		}
	}
	maxFreq, maxVal := 0, 0
	for v, c := range freq {
		if c > maxFreq {
			maxFreq = c
			maxVal = v
		}
	}
	need := maxFreq*2 - same
	if need <= 0 {
		return ans
	}
	for i := 0; i < n && need > 0; i++ {
		if nums1[i] != nums2[i] && nums1[i] != maxVal && nums2[i] != maxVal {
			ans += int64(i)
			need--
		}
	}
	if need > 0 {
		return -1
	}
	return ans
}
