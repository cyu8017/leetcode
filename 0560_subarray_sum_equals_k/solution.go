// LeetCode 0560 - Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

func subarraySum(nums []int, k int) int {
	counts := map[int]int{0: 1}
	prefix := 0
	answer := 0
	for _, num := range nums {
		prefix += num
		answer += counts[prefix-k]
		counts[prefix]++
	}
	return answer
}
