// LeetCode 0992 - Subarrays with K Different Integers
// https://leetcode.com/problems/subarrays-with-k-different-integers/

func subarraysWithKDistinct(nums []int, k int) int {
	atMost := func(m int) int {
		count := map[int]int{}
		left, ans := 0, 0
		for right, x := range nums {
			count[x]++
			for len(count) > m {
				count[nums[left]]--
				if count[nums[left]] == 0 {
					delete(count, nums[left])
				}
				left++
			}
			ans += right - left + 1
		}
		return ans
	}
	return atMost(k) - atMost(k-1)
}
