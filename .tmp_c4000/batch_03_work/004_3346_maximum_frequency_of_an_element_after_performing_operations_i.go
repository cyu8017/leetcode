// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

import "sort"

func maxFrequency(nums []int, k int, numOperations int) int {
	sort.Ints(nums)
	n := len(nums)
	freq := map[int]int{}
	for _, x := range nums {
		freq[x]++
	}
	ans := 1
	// candidates: existing values
	for t, f := range freq {
		// count how many can reach t with |x-t|<=k
		lo := sort.SearchInts(nums, t-k)
		hi := sort.Search(n, func(i int) bool { return nums[i] > t+k })
		can := hi - lo
		use := can
		if use > f+numOperations {
			use = f + numOperations
		}
		if use > ans {
			ans = use
		}
	}
	// also consider targets not in array via sliding window of size numOperations on values within 2k
	l := 0
	for r := 0; r < n; r++ {
		for nums[r]-nums[l] > 2*k {
			l++
		}
		window := r - l + 1
		if window > numOperations {
			window = numOperations
		}
		// if target not in nums, all need ops
		if window > ans {
			ans = window
		}
	}
	return ans
}
