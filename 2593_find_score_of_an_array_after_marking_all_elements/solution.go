// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/


import "sort"

func findScore(nums []int) int64 {
	n := len(nums)
	idx := make([]int, n)
	for i := range idx {
		idx[i] = i
	}
	sort.Slice(idx, func(i, j int) bool {
		if nums[idx[i]] != nums[idx[j]] {
			return nums[idx[i]] < nums[idx[j]]
		}
		return idx[i] < idx[j]
	})
	marked := make([]bool, n)
	var ans int64
	for _, i := range idx {
		if marked[i] {
			continue
		}
		ans += int64(nums[i])
		marked[i] = true
		if i > 0 {
			marked[i-1] = true
		}
		if i+1 < n {
			marked[i+1] = true
		}
	}
	return ans
}
