// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

func countDistinct(nums []int, k int, p int) int {
	n := len(nums)
	seen := map[string]struct{}{}
	for i := 0; i < n; i++ {
		div := 0
		key := ""
		for j := i; j < n; j++ {
			if nums[j]%p == 0 {
				div++
			}
			if div > k {
				break
			}
			key += string(rune(nums[j]+1)) + ","
			seen[key] = struct{}{}
		}
	}
	return len(seen)
}
