// LeetCode 1590 - Make Sum Divisible by P
// https://leetcode.com/problems/make-sum-divisible-by-p/

func minSubarray(nums []int, p int) int {
	total := 0
	for _, x := range nums {
		total = (total + x) % p
	}
	if total == 0 {
		return 0
	}
	target := total
	seen := map[int]int{0: -1}
	prefix, answer := 0, len(nums)
	for i, x := range nums {
		prefix = (prefix + x) % p
		need := (prefix - target + p) % p
		if idx, ok := seen[need]; ok {
			if i-idx < answer {
				answer = i - idx
			}
		}
		seen[prefix] = i
	}
	if answer < len(nums) {
		return answer
	}
	return -1
}
