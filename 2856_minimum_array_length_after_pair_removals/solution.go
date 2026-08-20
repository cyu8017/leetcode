// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

func minLengthAfterRemovals(nums []int) int {
	n := len(nums)
	freq := map[int]int{}
	mx := 0
	for _, v := range nums {
		freq[v]++
		if freq[v] > mx {
			mx = freq[v]
		}
	}
	if mx <= n/2 {
		return n % 2
	}
	return 2*mx - n
}
