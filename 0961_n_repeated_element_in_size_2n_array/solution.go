// LeetCode 0961 - N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

func repeatedNTimes(nums []int) int {
	seen := map[int]bool{}
	for _, x := range nums {
		if seen[x] {
			return x
		}
		seen[x] = true
	}
	return -1
}
