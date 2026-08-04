// LeetCode 1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
// https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

func maxNonOverlapping(nums []int, target int) int {
	seen := map[int]bool{0: true}
	prefix, answer := 0, 0
	for _, value := range nums {
		prefix += value
		if seen[prefix-target] {
			answer++
			prefix = 0
			seen = map[int]bool{0: true}
		} else {
			seen[prefix] = true
		}
	}
	return answer
}
