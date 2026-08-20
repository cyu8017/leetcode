// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

func numSubarrayBoundedMax(nums []int, left int, right int) int {
	countAtMost := func(bound int) int {
		ans, cur := 0, 0
		for _, num := range nums {
			if num <= bound {
				cur++
				ans += cur
			} else {
				cur = 0
			}
		}
		return ans
	}
	return countAtMost(right) - countAtMost(left-1)
}
