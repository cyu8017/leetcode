// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

import "sort"

func maxFrequency(nums []int, k int, numOperations int) int {
	sort.Ints(nums)
	n := len(nums)
	freq := map[int]int{}
	for _, x := range nums {
		freq[x]++
	}
	ans := 1
	candidates := []int{}
	seen := map[int]bool{}
	for _, x := range nums {
		for _, t := range []int{x - k, x, x + k} {
			if !seen[t] {
				seen[t] = true
				candidates = append(candidates, t)
			}
		}
	}
	for _, t := range candidates {
		lo := sort.SearchInts(nums, t-k)
		hi := sort.Search(n, func(i int) bool { return nums[i] > t+k })
		can := hi - lo
		f := freq[t]
		use := can
		if use > f+numOperations {
			use = f + numOperations
		}
		if use > ans {
			ans = use
		}
	}
	return ans
}
