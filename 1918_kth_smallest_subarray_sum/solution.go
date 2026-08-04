// LeetCode 1918 - Kth Smallest Subarray Sum
// https://leetcode.com/problems/kth-smallest-subarray-sum/

func kthSmallestSubarraySum(nums []int, k int) int {
	count := func(limit int) int {
		total, left, ans := 0, 0, 0
		for right, value := range nums {
			total += value
			for total > limit {
				total -= nums[left]
				left++
			}
			ans += right - left + 1
		}
		return ans
	}
	lo, hi := nums[0], 0
	for _, x := range nums {
		if x < lo {
			lo = x
		}
		hi += x
	}
	for lo < hi {
		mid := (lo + hi) / 2
		if count(mid) >= k {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
