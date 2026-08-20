// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

func maxRemovals(source string, pattern string, targetIndices []int) int {
	n := len(source)
	removable := make([]bool, n)
	for _, i := range targetIndices {
		removable[i] = true
	}
	ok := func(removeFirst int) bool {
		mark := make([]bool, n)
		for i := 0; i < removeFirst; i++ {
			mark[targetIndices[i]] = true
		}
		j := 0
		for i := 0; i < n && j < len(pattern); i++ {
			if mark[i] {
				continue
			}
			if source[i] == pattern[j] {
				j++
			}
		}
		return j == len(pattern)
	}
	lo, hi := 0, len(targetIndices)
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if ok(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
