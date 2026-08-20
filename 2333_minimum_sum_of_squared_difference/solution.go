// LeetCode 2333 - Minimum Sum of Squared Difference
// https://leetcode.com/problems/minimum-sum-of-squared-difference/

func minSumSquareDiff(nums1 []int, nums2 []int, k1 int, k2 int) int64 {
	n := len(nums1)
	diff := make([]int, n)
	maxD := 0
	for i := 0; i < n; i++ {
		d := nums1[i] - nums2[i]
		if d < 0 {
			d = -d
		}
		diff[i] = d
		if d > maxD {
			maxD = d
		}
	}
	k := k1 + k2
	freq := make([]int, maxD+1)
	for _, d := range diff {
		freq[d]++
	}
	for d := maxD; d > 0 && k > 0; d-- {
		if freq[d] == 0 {
			continue
		}
		take := freq[d]
		if take > k {
			take = k
		}
		freq[d] -= take
		freq[d-1] += take
		k -= take
	}
	var ans int64
	for d, f := range freq {
		ans += int64(d) * int64(d) * int64(f)
	}
	return ans
}
