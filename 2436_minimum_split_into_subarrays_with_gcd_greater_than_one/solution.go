// LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
// https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

func minimumSplits(nums []int) int {
	ans := 1
	g := nums[0]
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	for i := 1; i < len(nums); i++ {
		ng := gcd(g, nums[i])
		if ng == 1 {
			ans++
			g = nums[i]
		} else {
			g = ng
		}
	}
	return ans
}
