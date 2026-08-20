// LeetCode 0974 - Subarray Sums Divisible by K
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

func subarraysDivByK(nums []int, k int) int {
	count := map[int]int{0: 1}
	prefix, ans := 0, 0
	for _, x := range nums {
		prefix = (prefix + x) % k
		if prefix < 0 {
			prefix += k
		}
		ans += count[prefix]
		count[prefix]++
	}
	return ans
}
