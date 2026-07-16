// LeetCode 0325 - Maximum Size Subarray Sum Equals k
// https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

func maxSubArrayLen(nums []int, k int) int {
	prefixIndex := map[int]int{0: -1}
	prefix := 0
	best := 0
	for index, num := range nums {
		prefix += num
		if startIndex, ok := prefixIndex[prefix-k]; ok {
			if index-startIndex > best {
				best = index - startIndex
			}
		}
		if _, ok := prefixIndex[prefix]; !ok {
			prefixIndex[prefix] = index
		}
	}
	return best
}
