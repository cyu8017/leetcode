// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

func subarrayLCM(nums []int, k int) int {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	lcm := func(a, b int) int {
		return a / gcd(a, b) * b
	}
	ans := 0
	n := len(nums)
	for i := 0; i < n; i++ {
		cur := 1
		for j := i; j < n; j++ {
			cur = lcm(cur, nums[j])
			if cur > k {
				break
			}
			if cur == k {
				ans++
			}
		}
	}
	return ans
}
