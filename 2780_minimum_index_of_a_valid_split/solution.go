// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

func minimumIndex(nums []int) int {
	freq := map[int]int{}
	dom, best := 0, 0
	for _, v := range nums {
		freq[v]++
		if freq[v] > best {
			best = freq[v]
			dom = v
		}
	}
	left := 0
	n := len(nums)
	for i := 0; i < n-1; i++ {
		if nums[i] == dom {
			left++
		}
		right := best - left
		if left*2 > i+1 && right*2 > n-i-1 {
			return i
		}
	}
	return -1
}
